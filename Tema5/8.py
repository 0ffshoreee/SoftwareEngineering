from random import randint

def list_maker():
    a = [randint(1, 100)] * randint(3, 10)
    return a

result = []
for i in range(randint(1, 5)):
    result.append(list_maker())

print(result)