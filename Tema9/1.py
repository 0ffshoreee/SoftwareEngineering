class Kirill:
    __slots__ = ['name']
    def __init__(self, name):
        if name == 'Кирилл':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Кирилл"

person1 = Kirill("Андрей")
person2 = Kirill("Кирилл")

print(person1.name)
print((person2.name))