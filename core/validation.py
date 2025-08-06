import re

# Simple pattern for domain or full URL
def is_valid_url(url):
    pattern = re.compile(
        r'^(https?://)?'         # http or https (optional)
        r'(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})$'  # domain like example.com
    )
    return pattern.match(url) is not None
