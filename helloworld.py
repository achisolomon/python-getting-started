
""" this
is a comment
"""


name = "Achi"
pi = 3.14159
print("hello world! " + name)


def add_num(a: int, b: int)-> int:
    return a+b


print(int(add_num(3, pi)))

num = 4

print("bigger" if pi > num else "smaller")

print("Hello {0}".format(name))

print(f"Hello again {name}")

alawys_true = True

nullIsNone = None


print(f"nullIsNone = {nullIsNone}")

if not alawys_true and  nullIsNone:
    print("yep!")
else:
    print("nop!")

if pi:
    print("pi is truthy")


students_names = ["first ", "2nd"]

print (f"index 1 is {students_names[1]}")

print (f"index -1 is {students_names[-1]}")

students_names.append("3rd")

print (f"index -1 is {students_names[-1]}")

print (f"students_names len is { len (students_names) }")

print (f"students_names contains {students_names}")

print(f"slicing the list students_names[1:-1] {students_names[1:-1]}")

del students_names[1]

print (f" after del [1] students_names contains {students_names}")

if "3rD" in students_names:
    print("Yey!")
else:
    print("oye, in is case senstive !")

print("printing in a for loop")

for it in students_names:
    print(f"the iterator is {it}")

for index in range(10):
    print(f"index is {index}")