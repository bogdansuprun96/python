# s = "This is string"
# i = 1
# d = 1.5
# print(type(i))
# print(type(d))
#
# def sum(a,b):
#     return a+b
#
# print(sum(i, d))
#
# s = sum
#
# print(s(4,5))


class Man:
    def __init__(self):
        self.age = 17
        self.name = "Bohdan Suprun"


m = Man()

print(m.age, m.name)


class Man:
    def __init__(self):
        self.__age = 17
        self.__name = "Bohdan"


m = Man()

try:
    print(m.age, m.name)
except AttributeError:
    print("Exeption handled!")


# print(m._Man__age)

class Man:
    def __init__(self):
        self.__age = None
        self.__name = None

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def info(self):
        print(self.__age, self.__name)

    def __str__(self):
        return self.__name + " " + str(self.__age)


m = Man()
m.set_age(21)
m.set_name("Bohdan")
print(m)


class Developer(Man):
    def __init__(self):
        super()  # При ініціалізації класу Developer з початку буде ініціалізований клас Man
        self.__lang = None

    def set_lang(self, lang):
        self.__lang = lang

    def get_lang(self):
        return self.__lang

    def __str__(self):
        return super().__str__() + " " + self.__lang


d = Developer()
d.set_name("Богдан")
d.set_age(21)
d.set_lang("Python, PHP, SQL, JavaScript, HTML/CSS")
print(d)


def func(*args):
    # print(type(args))
    print(args[0], args[1])


func(1, 2, 3)


class Man:
    def __init__(self, age, name):
        self.__age = age
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def info(self):
        print(self.__age, self.__name)

    def __str__(self):
        return self.__name + " " + str(self.__age)


l = [2, 4, 55, "str", str(Man(30, "Bohdan"))]

user = ("Вася", "Пупкин")
point = {
    "x": 6,
    "y": 7
}

print(l)
print(user)
print(point)

# print(type(()))
# print(type([]))
# print(type({}))

l.append("Some...")

print(l)
print(len(l))
print(l[5])
l.reverse()
print(l)

print(user[0])
list_user = list(user)

print(point['x'], point['y'])


for i  in range(0,5):
    print(i)

s = "Hello Python"

for i in range(0, len(s)):
    print(s[i], end=" ")

print("\n")

for ch in s:
    print(ch, end="")

s = set([2,4,1])
print("\n")

# print(type(s))

if 5 in s:
    print(True)
elif 4 in s:
    print("Yes")
else:
    print(False)

# print(type(True))

if 1 >= 1 and 2 <= 2 or 3==4:
    print(True)

n = "bohdan"

s = "Hello " + n

if "Hello" in s:
    print(s)

index = 0
while True:
    if index == 10:
        break
    else:
        print(index, end=" ")
        index += 1

print("\n\n\n")

s = "Hello Python!"

print(s[0])
print(s[0:5])
print(s[::2])
# print(s[0:5:2])

l = list(range(0, 10))
print(l)
print(l[::2])

print(s[-1:])