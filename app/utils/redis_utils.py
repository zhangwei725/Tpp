import redis

HOST = '127.0.0.1'
PORT = 6379
DB = 0

pool = None


# rds = redis.Redis()
def init_redis():
    pool = redis.ConnectionPool(host=HOST, port=PORT, db=DB)


def get_redis():
    if pool:
        rds = redis.Redis(connection_pool=pool)
    return rds
