import datetime
import json
import base64
import time
from colorama import Fore, Style

gray = Fore.LIGHTBLACK_EX
orange = Fore.LIGHTYELLOW_EX
lightblue = Fore.LIGHTBLUE_EX

class log:
    @staticmethod
    def slog(type, color, message, time):
        msg = f"{gray} [ {color}{type}{gray} ] [ {color}{message}{gray} ] [ {Fore.CYAN}{time:.2f}s{gray} ]"
        print(log.center(msg))
        
    @staticmethod
    def ilog(type, color, message):
        msg = f"{gray} [ {color}{type}{gray} ] [ {color}{message}{gray} ]"
        inputmsg = input(log.center(msg) + " ")
        return inputmsg

    @staticmethod
    def log(type, color, message):
        msg = f"{gray} [ {color}{type}{gray} ] [ {color}{message}{gray} ]{Style.RESET_ALL}"
        print(log.center(msg))

    @staticmethod
    def success(message, time):
        log.slog('+', Fore.GREEN, message, time)

    @staticmethod
    def fail(message):
        log.log('X', Fore.RED, message)

    @staticmethod
    def warn(message):
        log.log('!', Fore.YELLOW, message)

    @staticmethod
    def info(message):
        log.log('i', lightblue, message)
        
    @staticmethod
    def input(message):
        return log.ilog('i', lightblue, message)

    @staticmethod
    def working(message):
        log.log('-', orange, message)

    @staticmethod
    def center(text):
        return text

def hsl(token):
    if not hasattr(datetime.datetime, 'isoformat'):
        def r(n):
            s = str(n)
            return '0' + s if len(s) == 1 else s

        def toISOString(self):
            return f"{self.year}-{r(self.month)}-{r(self.day)}T{r(self.hour)}:{r(self.minute)}:{r(self.second)}.{str(self.microsecond // 1000).zfill(3)}Z"

        datetime.datetime.isoformat = toISOString

    class SHA1:
        @staticmethod
        def hash(message):
            if not isinstance(message, str):
                raise ValueError("Message Must Be String")

            k = [0x5a827999, 0x6ed9eba1, 0x8f1bbcdc, 0xca62c1d6]
            h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

            message = message.encode('utf-8')
            message += b'\x80'
            message += b'\x00' * ((56 - (len(message) % 64)) % 64)
            message += (len(message) * 8).to_bytes(8, 'big')

            for i in range(0, len(message), 64):
                chunk = message[i:i+64]
                w = [int.from_bytes(chunk[j:j+4], 'big') for j in range(0, 64, 4)]
                w += [0] * 64

                for j in range(16, 80):
                    w[j] = SHA1.rotate_left(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)

                a, b, c, d, e = h

                for j in range(80):
                    if j < 20:
                        f = (b & c) | ((~b) & d)
                        k_t = k[0]
                    elif j < 40:
                        f = b ^ c ^ d
                        k_t = k[1]
                    elif j < 60:
                        f = (b & c) | (b & d) | (c & d)
                        k_t = k[2]
                    else:
                        f = b ^ c ^ d
                        k_t = k[3]

                    temp = (SHA1.rotate_left(a, 5) + f + e + k_t + w[j]) & 0xffffffff
                    e = d
                    d = c
                    c = SHA1.rotate_left(b, 30)
                    b = a
                    a = temp

                h[0] = (h[0] + a) & 0xffffffff
                h[1] = (h[1] + b) & 0xffffffff
                h[2] = (h[2] + c) & 0xffffffff
                h[3] = (h[3] + d) & 0xffffffff
                h[4] = (h[4] + e) & 0xffffffff

            return h

        @staticmethod
        def digest(h):
            return [
                (h[0] >> 24) & 0xff, (h[0] >> 16) & 0xff, (h[0] >> 8) & 0xff, h[0] & 0xff,
                (h[1] >> 24) & 0xff, (h[1] >> 16) & 0xff, (h[1] >> 8) & 0xff, h[1] & 0xff,
                (h[2] >> 24) & 0xff, (h[2] >> 16) & 0xff, (h[2] >> 8) & 0xff, h[2] & 0xff,
                (h[3] >> 24) & 0xff, (h[3] >> 16) & 0xff, (h[3] >> 8) & 0xff, h[3] & 0xff,
                (h[4] >> 24) & 0xff, (h[4] >> 16) & 0xff, (h[4] >> 8) & 0xff, h[4] & 0xff
            ]

        @staticmethod
        def hex(h):
            return ''.join(f'{x:08x}' for x in h)

        @staticmethod
        def rotate_left(n, b):
            return ((n << b) | (n >> (32 - b))) & 0xffffffff

    ALPHABET = "0123456789/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def e(r, t):
        def find_solution(r, t):
            for e in range(25):
                i = [0] * e
                while increment(i):
                    if n(r, t + "::" + a(i)):
                        return a(i)
            return None

        e = find_solution(r, t)
        return f"1:{r}:{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}:{t}::{e}"

    def n(t, e):
        def check_hash(r, t):
            bits = []
            for byte in t:
                for i in range(8):
                    bits.append((byte >> i) & 1)
            a = bits[:r]
            return a[0] == 0 and (a.index(1) >= r - 1 if 1 in a else True)

        h = SHA1.hash(e)
        log.info(f"SHA1 Hash --> {h[:45]}")
        d = SHA1.digest(h)
        log.info(f"SHA1 Digest --> {d[:45]}")
        return check_hash(t, d)

    def increment(r):
        for e in range(len(r) - 1, -1, -1):
            if r[e] < len(ALPHABET) - 1:
                r[e] += 1
                return True
            r[e] = 0
        return False

    def a(r):
        return ''.join(ALPHABET[i] for i in r)

    def parseTok(token):
        log.info(f'Token --> {token[:50]}...')
        parts = token.split('.')
        data = {
            'header': json.loads(base64.b64decode(parts[0] + '==').decode('utf-8')),
            'payload': json.loads(base64.b64decode(parts[1] + '==').decode('utf-8')),
            'signature': base64.b64decode(parts[2].replace('_', '/').replace('-', '+') + '=='),
            'raw': {
                'header': parts[0],
                'payload': parts[1],
                'signature': parts[2]
            }
        }
        log.info(f"Token Header --> {data.get('header')}")
        log.info(f"Token Payload --> {data.get('payload')}")
        log.info(f"Token Signature --> {data.get('signature')}")
        return data

    def procTok(r):
        try:
            o = parseTok(r)
            a = o['payload']
            s = a['d']
            u = a['s']
            if not s or not u:
                raise TypeError("Invalid Spec")
            return e(u, s)
        except Exception as c:
            raise c

    return procTok(token)

# replace the value of `token` with your actual hsl token
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiIxMGowM2V1OXFqK1RyY2d0dlc5KzdBMFJjSm5va3VoVmFXb04yeGNTNlpLcEdTOG9NK0VmNG1NMGJ1VVVZQm1CRm4vcHpQQkdTRHVSZ0FGUnhNbFozOWVIdHN3QjJTRmhSYUpsZWc0RHV5TkdjV2VDZ3pzWTZvb29HeWNXbFdabWZ2WkNXT2tvSGlidTEwYjJrSG4yMU5Qa09GWUE0bXRuL3R0Z01MRXJmN3FOYkVXMHhMV1hJemlkejlCdG9nZ3dKVEJpWmJkRGFwNFFZSFd3SDNVOGErL0E2eE54WURUTWFhSXlveWVsS0g0cTNBYk9PUTlnRUFhSlpYSWRqbmtxK3hmN3Q3WHBWVFZhdXJUQiIsImwiOiJodHRwczovL25ld2Fzc2V0cy5oY2FwdGNoYS5jb20vYy9lNmMyNmNiYTg5MzJiMGYxOWFiYzE4ZmJmM2EyODk5ZjZkMjA1YTA0NjAyZGE4OWE4MTkxMDdiOTM0ZThkZDUwIiwiaSI6InNoYTI1Ni1NYVV4U1ZaZys3YWFwOFA0anNMZjU2RVRSMFNTdjU1N09BempYYXpyWW9VPSIsImUiOjE3MjM1NzE0OTEsIm4iOiJoc3ciLCJjIjoxMDAwfQ.Vcb9FGnQLZXSS4rVkU1PuOp1-1muwV2pOXzdCM2V_PI"
t = time.time()
enc = hsl(token)
log.success(f"Encrypted --> {enc[:40]}...", round(time.time()-t,2))
input()
