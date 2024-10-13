req = int(input())

dict = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': True},
    None: {'key': None, 'access': False},
}

response = dict.get(req)
if not response:
    response = dict[None]
key = response.get('key')
access = response.get('access')
print(key, access)

