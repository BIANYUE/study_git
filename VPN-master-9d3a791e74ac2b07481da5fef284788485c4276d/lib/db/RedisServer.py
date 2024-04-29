import redis

from settings import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT, REDIS_DB


class RedisServer:
    def __init__(self):
        self.redis_db = redis.StrictRedis(host=REDIS_HOST, password=REDIS_PASSWORD, port=REDIS_PORT, db=REDIS_DB,
                                          decode_responses=True)

    # 提取任务
    def lpop(self, key):
        return self.redis_db.lpop(key)

    # 插入到list
    def rpush(self, key, values):
        self.redis_db.rpush(key, values)

    # 插入到list
    def lpush(self, key, values):
        self.redis_db.lpush(key, values)

    # 查询任务数量
    def llen(self, key):
        return self.redis_db.llen(key)

    def scard(self, key):
        '''查询集合元素数
        :param key:
        :return:
        '''
        return self.redis_db.scard(key)

    # 集合添加元素
    def sadd(self, key, values):
        return self.redis_db.sadd(key, values)

    def randmember(self, key):
        data = self.redis_db.srandmember(key, 1)
        if len(data) > 0:
            return data[0]

    # 删除集合中指定元素
    def srem(self, key, values):
        try:
            return self.redis_db.srem(key, values)
        except TypeError:
            pass

    # 删除key
    def delete(self, key):
        return self.redis_db.delete(key)

    # 返回集合所有成员
    def smembers(self, key):
        return self.redis_db.smembers(key)

    # 是否存在
    def sismember(self, key, value):
        return self.redis_db.sismember(key, value)


if __name__ == '__main__':
    s = RedisServer()
    print(s.rpush("vpn:pid", 6379))
    print(s.lpop("vpn:pid"))
