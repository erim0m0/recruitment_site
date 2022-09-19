import redis


rd = redis.Redis(host='localhost', port=6379)


# print(rd.hvals('9336758938'))

print(type(rd.exists('rpk[o')))

