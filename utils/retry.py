import time

def retry(func, retries=3, delay=2, logger=None):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            if logger:
                logger.warning(f"Retry {attempt+1}/{retries} failed: {e}")
            time.sleep(delay)
    raise Exception("All retries failed")
