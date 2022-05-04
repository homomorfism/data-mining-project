import sys
import requests
from typing import Optional

import chardet

# бессовестно стащил отсюда: https://sumit-ghosh.com/articles/python-download-progress-bar/
def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')


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
