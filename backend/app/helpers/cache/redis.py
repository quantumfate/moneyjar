import os

import redis


class Cache:
    def __init__(self):
        self.client = redis.Redis(
                host=os.environ.get("REDIS_HOST"),
                port=os.environ.get("REDIS_PORT"),
                decode_responses=True,
        )
    
    def set(self, key, value, expiration=None):
        self.client.set(key, value, ex=expiration)
    
    def get(self, key):
        return self.client.get(key)
    
    def delete(self, key):
        self.client.delete(key)