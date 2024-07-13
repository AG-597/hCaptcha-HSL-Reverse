import datetime
import json
import base64

CHARSET = "0123456789/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class cdt(datetime.datetime):
    def toISOString(self):
        def r(n):
            s = str(n)
            return '0' + s if len(s) == 1 else s

        return f"{self.year}-{r(self.month)}-{r(self.day)}T{r(self.hour)}:{r(self.minute)}:{r(self.second)}.{str(self.microsecond // 1000).zfill(3)}Z"

def mPxiC():
    datetime.datetime = cdt

    class SHA1:
        @staticmethod
        def hash(message):
            if not isinstance(message, str):
                raise ValueError("Message Must Be String")

            K = [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6]
            H = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

            message = message.encode('utf-8')
            ml = len(message) * 8
            message += b'\x80'
            message += b'\x00' * ((56 - (len(message) % 64)) % 64)
            message += ml.to_bytes(8, 'big')

            for i in range(0, len(message), 64):
                chunk = message[i:i+64]
                w = [int.from_bytes(chunk[j:j+4], 'big') for j in range(0, 64, 4)]
                w += [0] * 64

                for j in range(16, 80):
                    w[j] = SHA1.r_left(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)

                a, b, c, d, e = H

                for j in range(80):
                    if j < 20:
                        f = (b & c) | ((~b) & d)
                        k = K[0]
                    elif j < 40:
                        f = b ^ c ^ d
                        k = K[1]
                    elif j < 60:
                        f = (b & c) | (b & d) | (c & d)
                        k = K[2]
                    else:
                        f = b ^ c ^ d
                        k = K[3]

                    temp = SHA1.r_left(a, 5) + f + e + k + w[j] & 0xFFFFFFFF
                    e = d
                    d = c
                    c = SHA1.r_left(b, 30)
                    b = a
                    a = temp

                H[0] = (H[0] + a) & 0xFFFFFFFF
                H[1] = (H[1] + b) & 0xFFFFFFFF
                H[2] = (H[2] + c) & 0xFFFFFFFF
                H[3] = (H[3] + d) & 0xFFFFFFFF
                H[4] = (H[4] + e) & 0xFFFFFFFF

            return H

        @staticmethod
        def digest(hash_value):
            return [
                (hash_value[i] >> (24 - j * 8)) & 0xFF
                for i in range(5)
                for j in range(4)
            ]

        @staticmethod
        def hex(hash_value):
            return ''.join(f'{x:08x}' for x in hash_value)

        @staticmethod
        def r_left(n, b):
            return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

    def gen_proof(difficulty, prefix):
        def check_proof(difficulty, candidate):
            hash_result = SHA1.hash(candidate)
            digest = SHA1.digest(hash_result)
            bits = ''.join(f'{byte:08b}' for byte in digest[:difficulty // 8 + 1])
            return bits.startswith('0' * difficulty) or ('1' not in bits[:difficulty])

        for length in range(1, 26):
            suffix = [0] * length
            while True:
                candidate = f"{prefix}::{ats(suffix)}"
                if check_proof(difficulty, candidate):
                    return ats(suffix)
                if not increment_array(suffix):
                    break
        return None

    def chc(difficulty, prefix):
        proof = gen_proof(difficulty, prefix)
        timestamp = datetime.datetime.utcnow()
        return f"1:{difficulty}:{timestamp.toISOString()}:{prefix}::{proof}"

    def increment_array(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] < len(CHARSET) - 1:
                arr[i] += 1
                return True
            arr[i] = 0
        return False

    def ats(arr):
        return ''.join(CHARSET[i] for i in arr)

    def is_browser():
        try:
            return (lambda: True)() and not (lambda: False)() and not (lambda: False)()
        except:
            return False

    def p_token(token):
        def parse_jwt(jwt):
            try:
                header, payload, signature = jwt.split('.')
                return {
                    'header': json.loads(base64.b64decode(header + '==').decode('utf-8')),
                    'payload': json.loads(base64.b64decode(payload + '==').decode('utf-8')),
                    'signature': base64.b64decode(signature.replace('_', '/').replace('-', '+') + '==').decode('utf-8'),
                    'raw': {
                        'header': header,
                        'payload': payload,
                        'signature': signature
                    }
                }
            except:
                raise ValueError("Token is invalid.")

        try:
            decoded = parse_jwt(token)
            payload = decoded['payload']
            domain = ("" if is_browser() else "@") + payload['d']
            difficulty = payload['s']

            if not domain or difficulty is None:
                raise TypeError("Invalid Spec")

            return chc(difficulty, domain)
        except Exception as e:
            raise e

    return p_token

hsl = mPxiC()
print(hsl("hsl token"))