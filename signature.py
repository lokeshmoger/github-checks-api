import hashlib
import hmac
import os

__author__ = "@Wietze"
__copyright__ = "Copyright 2019"

GITHUB_WEBHOOK_SECRET = os.environ.get('GITHUB_WEBHOOK_SECRET')
if not GITHUB_WEBHOOK_SECRET:
    raise Exception('Please set the GITHUB_WEBHOOK_SECRET environment variable.')


def verify_signature(request) -> bool:
    header_signature = request.headers.get('X-HUB-SIGNATURE')

    sha_name, signature = header_signature.split('=')
    if sha_name == 'sha1':
        mac = hmac.new(str.encode(GITHUB_WEBHOOK_SECRET), request.get_data(), hashlib.sha1)
        return hmac.compare_digest(mac.hexdigest(), signature)
    return False
