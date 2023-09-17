from encode.polynomial import GFPolynomial
from encode.utils import ANTILOG_LOOKUP, expand, find_cw_lengths, VERSION1


def _generator_polynomial(degree):
    gen_poly = GFPolynomial([1, 1])
    for i in range(1, degree):
        gen_poly *= GFPolynomial([1, ANTILOG_LOOKUP[i]])

    return gen_poly


def _pad(message, len1):
    message += "0000"

    if len(message) != len1 * 8:
        message += "11101100"  # 236

    while len(message) != len1 * 8:
        if message[-1] == "0":
            message += "00010001"  # 17
        else:
            message += "11101100"  # 236

    return message


def _generate_message_poly(bits):
    coeffs = []
    for i in range(len(bits) // 8):
        coeffs.append(int(bits[8*i: 8*(i+1)], 2))
    return coeffs


def _get_ec_level(message):
    length = len(message)
    limits = {}
    for level in VERSION1:
        limits[level] = ((VERSION1[level][0] * 8) - (4 + 8)) // 8

    for level in VERSION1:
        if length <= limits[level]:
            break

    return level


def encode(message: str) -> str:
    message = [ord(char) for char in message]
    len1, len2 = find_cw_lengths(message)

    byte_encoding_id = "0100"
    msg_len = expand(bin(len(message)))
    msg_bin = "".join([expand(bin(num)) for num in message])

    msg_bits = byte_encoding_id + msg_len + msg_bin
    msg_bits = _pad(msg_bits, len1)

    msg_poly_coeffs = _generate_message_poly(msg_bits)

    msg_poly = GFPolynomial(msg_poly_coeffs) * GFPolynomial([1] + [0] * len2)
    gen_poly = _generator_polynomial(len2)
    remainder = msg_poly % gen_poly

    enc_msg = msg_bits + "".join([expand(bin(r)) for r in remainder])

    return enc_msg


def encode_format_info(message: str) -> str:
    ec_level = _get_ec_level(message)
    ec = {"L": [0, 1], "M": [0, 0], "Q": [1, 1], "H": [1, 0]}

    mask = [0, 0, 0]  # Always choose mask pattern 0, kinda cheating.

    poly = GFPolynomial(ec[ec_level] + mask) * GFPolynomial([1] + [0] * 10)
    gen_poly = GFPolynomial([1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1])

    rem = poly % gen_poly

    f1 = int("".join(map(str, ec[ec_level] + mask + rem)), base=2)
    f2 = int("101010000010010", base=2)

    return expand(bin(f1 ^ f2), num_bits=15)
