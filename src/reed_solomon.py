from polynomial import GFPolynomial
from utils import ANTILOG_LOOKUP, expand_to_8_bits, find_cw_lengths


def _generator_polynomial():
    gen_poly = GFPolynomial([1, 1])
    for i in range(1, 7):
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


def encode(message: str):
    message = [ord(char) for char in message]
    len1, len2 = find_cw_lengths(message)

    byte_encoding_id = "0100"
    message_length = expand_to_8_bits(bin(len(message)))
    message_bin = "".join([expand_to_8_bits(bin(num)) for num in message])

    message = byte_encoding_id + message_length + message_bin
    message = _pad(message, len1)

    return message
