"""
Token bucket algorithm: A request will only be accepted if there are enough tokens in the bucket.

Implements the token bucket algorithm for rate limiting
- A bucket has a capacity of N tokens
- Tokens are added to the bucket at a fixed rate time period; If the bucket is full the token will be discarded
- A token is removed when a request is accepted
- When a request arrives and the bucket is empty, the request is denied
- The bucket should be per individual ip address
"""


class TokenBucket:
    def __init__(self):
        pass
