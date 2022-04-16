import requests
import hmac
import hashlib
import time
import sys
import struct
import json

from requests.auth import HTTPBasicAuth

root = "https://api.challenge.hennge.com/challenges/003"
content_type = "application/json"
userid = "hussain.almahmud1@outlook.com"
secret_suffix = "HENNGECHALLENGE003"
shared_secret = userid+secret_suffix

timestep = 30
T0 = 0

def HOTP(K, C, digits=10):
    """HTOP:
    K is the shared key
    C is the counter value
    digits control the response length
    """
    K_bytes = str.encode(K)
    C_bytes = struct.pack(">Q", C)
    hmac_sha512 = hmac.new(key = K_bytes, msg=C_bytes, digestmod=hashlib.sha512).hexdigest()
    return Truncate(hmac_sha512)[-digits:]

def Truncate(hmac_sha512):
    """truncate sha512 value"""
    offset = int(hmac_sha512[-1], 16)
    binary = int(hmac_sha512[(offset *2):((offset*2)+8)], 16) & 0x7FFFFFFF
    return str(binary)

def TOTP(K, digits=10, timeref = 0, timestep = 30):
    """TOTP, time-based variant of HOTP
    digits control the response length
    the C in HOTP is replaced by ( (currentTime - timeref) / timestep )
    """
    C = int ( time.time() - timeref ) // timestep
    return HOTP(K, C, digits = digits)

data = { "github_url": "https://gist.github.com/hennge/b859bd12e7a7fb418141", "contact_email": "hussain.almahmud1@outlook.com", "solution_language": "python" }

passwd = TOTP(shared_secret, 10, T0, timestep).zfill(10) 
resp = requests.post(root, auth=HTTPBasicAuth(userid, passwd), data=json.dumps(data))
print(resp.status_code)
print(resp.json())

## output 
## 200 
## {'message': 'Congratulations! You have achieved mission 3'}