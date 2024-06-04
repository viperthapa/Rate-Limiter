import time
from datetime import datetime, timedelta

def token_bucket_algorithm(rate_limit, request_count):
    now = datetime.now()
    elapsed_time = (now - rate_limit.last_checked).total_seconds()
    new_tokens = elapsed_time * (rate_limit.limit_per_minute / 60)
    rate_limit.tokens = min(rate_limit.burst_limit, rate_limit.tokens + new_tokens)
    rate_limit.last_checked = now

    if rate_limit.tokens >= request_count:
        rate_limit.tokens -= request_count
        return True
    else:
        return False
