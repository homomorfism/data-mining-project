import chardet
from typing import Optional


def decode_string(s: bytes, encoding: Optional[str] = "ISO-8859-1") -> str:
    """
    Decode the string
    :param s: Bytes string to be decoded
    :param encoding: Initial encoding to try
    :return: Decoded string
    """

    line_is_decoded = False
    while not line_is_decoded:
        try:
            s = s.decode(encoding)
            line_is_decoded = True
        except UnicodeDecodeError:
            encoding = chardet.detect(s)["encoding"]

    return s
