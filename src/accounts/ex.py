import redis
import json

rd = redis.Redis(host='localhost', port=6379)

data = [{
    "id": 1,
    "name": "Lynn",
    "surname": "Burgess",
    "fullname": "Claire Holland",
    "email": "vicki@may.sg"
}]

with rd.pipeline() as pipe:
    for id, person in enumerate(data):
        pipe.hset(f'person{id}', mapping=person)
        pipe.hget('person0', 'name')
    result = pipe.execute()
# print(result[1].decode('ASCII'))
# dict = rd.hget('persons',0).decode()
# print(dict)

a = rd.expire('person2', 3000)



