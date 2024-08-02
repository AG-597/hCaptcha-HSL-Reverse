import base64
import json
import hashlib
import datetime

def hsl(token):
    def process(last, info):
        def lastC(dom, subKey):
            for indents in range(25):
                images = [0] * indents
                while _each(images):
                    if render(dom, subKey + "::" + next(images)):
                        return next(images)
            return None

        lastC_result = lastC(last, info)
        return f"1:{last}:{datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')}:{info}::{lastC_result}"

    def render(dom, property):
        def inner(mid, newlines):
            arr = [(newlines[i // 8] >> (i % 8)) & 1 for i in range(8 * len(newlines))]
            compare = arr[:mid]
            try:
                first_one_index = compare.index(1)
            except ValueError:
                first_one_index = -1
            return compare[0] == 0 and (first_one_index >= mid - 1 or first_one_index == -1)

        key = property
        k = keys['hash'](key)
        return inner(dom, keys['digest'](k))

    def _each(arr):
        for ct in range(len(arr) - 1, -1, -1):
            if arr[ct] < len(match) - 1:
                arr[ct] += 1
                return True
            arr[ct] = 0
        return False

    def next(codeSegments):
        return ''.join(match[codeSegments[i]] for i in range(len(codeSegments)))

    def parse_token(token):
        try:
            if '"' in token:
                token = token.replace('"', '')
            parts = token.split(".")
            if len(parts) != 3:
                raise ValueError("Token does not have the correct structure.")
            return {
                'header': json.loads(base64.urlsafe_b64decode(parts[0] + '==')),
                'payload': json.loads(base64.urlsafe_b64decode(parts[1] + '==')),
                'signature': base64.urlsafe_b64decode(parts[2] + '=='),
                'raw': {
                    'header': parts[0],
                    'payload': parts[1],
                    'signature': parts[2]
                }
            }
        except Exception as e:
            raise ValueError("Failed to parse token: " + str(e))

    keys = {
        'hash': lambda string: hashlib.sha1(string.encode()).digest(),
        'digest': lambda str: list(str),
        'hex': lambda resultItems: ''.join([f"{x:08x}" for x in resultItems]),
        'rotateLeft': lambda num, cnt: (num << cnt) | (num >> (32 - cnt)),
        'f': lambda keepData, a, b, c: {
            0: lambda: a & b ^ ~a & c,
            1: lambda: a ^ b ^ c,
            2: lambda: a & b ^ a & c ^ b & c,
            3: lambda: a ^ b ^ c
        }[keepData]()
    }

    match = "0123456789/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def getFunction():
        try:
            return (lambda: True)() and not (lambda: False)() and not (lambda: False)()
        except:
            return False

    def inner(token):
        try:
            d = parse_token(token)
            input = d.get('payload', {})
            info = ("" if getFunction() else "@") + input.get('d', '')
            last = input.get('s', '')
            if not info or not last:
                raise TypeError("Invalid Spec: 'd' or 's' missing in payload.")
            return process(last, info)
        except Exception as e:
            raise e

    rt = inner(token)
    return rt
