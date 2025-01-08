import base64
import hashlib
import hmac
import random
import string
import struct
import time
import urllib.parse

def secret(length=32):
    """Genera una clave secreta aleatoria en base32."""
    if length <= 0:
        raise ValueError("Length must be a positive integer")
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')
    return ''.join(random.choices(alphabet, k=length))

def hotp(secret: str, counter: int, digits=6):
    """Genera un código HOTP."""
    if digits <= 0:
        raise ValueError("Digits must be a positive integer")
    key = base64.b32decode(secret.upper() + "=" * ((8 - len(secret)) % 8))
    counter_bytes = struct.pack('>Q', counter)
    h = hmac.new(key, counter_bytes, hashlib.sha1).digest()
    offset = h[-1] & 0xf
    code = ((h[offset] & 0x7f) << 24 |
            (h[offset + 1] & 0xff) << 16 |
            (h[offset + 2] & 0xff) << 8 |
            (h[offset + 3] & 0xff))
    code = str(code % (10 ** digits))
    return code.zfill(digits)

def totp(secret: str, digits=6, period=30):
    """Genera un código TOTP."""
    if digits <= 0 or period <= 0:
        raise ValueError("Digits and period must be positive integers")
    counter = int(time.time() / period)
    return hotp(secret, counter, digits)

def verify_hotp(secret: str, token: str, counter: int, digits=6, window=1):
    """Verifica un código HOTP."""
    if digits <= 0 or window < 0:
        raise ValueError("Digits must be positive and window must be non-negative")
    for i in range(counter - window, counter + window + 1):
        if hmac.compare_digest(token, hotp(secret, i, digits)):
            return True
    return False

def verify_totp(secret: str, token: str, digits=6, period=30, window=1):
    """Verifica un código TOTP."""
    if digits <= 0 or period <= 0 or window < 0:
        raise ValueError("Digits and period must be positive and window must be non-negative")
    counter = int(time.time() / period)
    return verify_hotp(secret, token, counter, digits, window)

def url(secret: str, label: str, issuer: str = None, algorithm: str = 'SHA1', digits=6, period=30, type: str = 'totp'):
    """Genera una URL para un código OTP."""
    if digits <= 0 or period <= 0:
        raise ValueError("Digits and period must be positive integers")
    type = type.lower()
    if type not in ['totp', 'hotp']:
        raise ValueError("Type must be 'totp' or 'hotp'")
    label = urllib.parse.quote(label)
    params = {
        'secret': secret,
        'algorithm': algorithm,
        'digits': str(digits),
    }
    if issuer:
        params['issuer'] = issuer
    if type == 'totp':
        params['period'] = str(period)
    query = urllib.parse.urlencode(params)
    return f"otpauth://{type}/{label}?{query}"