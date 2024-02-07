from slowapi import Limiter
from slowapi.util import get_remote_address

# Create a Limiter instance. The key function is used to determine how to limit requests (by IP in this case).
limiter = Limiter(key_func=get_remote_address)
