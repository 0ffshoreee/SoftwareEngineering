with open('input.txt', 'a+') as f:
    f.write('\nMy name is Kirill')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
    

