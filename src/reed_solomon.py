from polynomial import GFPolynomial
from utils import ANTILOG_LOOKUP, expand_to_8_bits, find_cw_lengths


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


def encode(message: str):
    message = [ord(char) for char in message]
    len1, len2 = find_cw_lengths(message)

    byte_encoding_id = "0100"
    msg_len = expand_to_8_bits(bin(len(message)))
    msg_bin = "".join([expand_to_8_bits(bin(num)) for num in message])

    msg_bits = byte_encoding_id + msg_len + msg_bin
    msg_bits = _pad(msg_bits, len1)

    msg_poly_coeffs = _generate_message_poly(msg_bits)

    message_poly = GFPolynomial(msg_poly_coeffs) * GFPolynomial([1] + [0] * len2)
    gen_poly = _generator_polynomial(len2)
    remainder = message_poly % gen_poly
    
    enc_msg = msg_bits + "".join([expand_to_8_bits(bin(r)) for r in remainder])

    return enc_msg
