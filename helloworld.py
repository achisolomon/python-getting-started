
""" this
is a comment
"""


name = "Achi"
pi = 3.14159
print("hello world! " + name)


def add_num(a: int, b: int)-> int:
    return a+b


print(int(add_num(3, pi)))


print("Hello {0}".format(name) )

print(f"Hello again {name}")

alawys_true = True

nullIsNone = None


print(f"nullIsNone = {nullIsNone}")

if not alawys_true:
    print("yep!")
else:
    print("nop!")
