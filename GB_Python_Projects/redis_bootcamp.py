import random
import redis

def redis_bootcamp_server():
    # redis connection
    pool = redis.ConnectionPool(host='localhost', port=32769, db=0, username='default', password='redispw')
    with redis.Redis(connection_pool=pool) as redis_server: # автоматически закрывает соединение
        redis_server.lpush("queue", random.randint(0, 10))

    # redis.set('mykey', 'Hello from Python!')
    # value = redis.get('mykey')
    # print(value)
    #
    # redis.zadd('vehicles', {'car': 0})
    # redis.zadd('vehicles', {'bike': 0})
    # vehicles = redis.zrange('vehicles', 0, -1) 0 - вывод с начала очереди, -1 - до конца очереди
    # print(vehicles)

def redis_bootcamp_client():
    # redis connection
    pool = redis.ConnectionPool(host='localhost', port=32769, db=0, username='default', password='redispw')
    with redis.Redis(connection_pool=pool) as redis_client: # автоматически закрывает соединение
        value = redis_client.brpop("queue")
    print(value[1]) # value - в байтах (ключ - значение)

# redis_bootcamp_server()