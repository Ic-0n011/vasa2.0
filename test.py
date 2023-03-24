print("Hello World")
var = "it is var"
var1 = 1
var2 = 2
print(var, var1 + var2)
print(id(var), type(var1))
def function_1():
    print("i'm function - def...")
    print(var2-var1)
function_1()
var3 = 3
if var3 == (var1 + var2):
    print(not False)
list_1 = [1, 2, 3, "imposter"]
print(list_1)
list_1.remove("imposter")
print(list_1)
list_1.clear()
list_1.append("clear")
print(list_1)
dict_1 = {1: 2, 2: 1}
print(dict_1[1])
print(hash(var))
a = 0
while True:
    print("i am the While!")
    a = a + 1
    if a == 6:
        print(a, "/6")
        break
    else:
        print(a, "/6")
class Creature:
    def __init__(self) -> None:
        self.name = "ZCS"
        self.hp = 100

    def speak(self):
        print("hello!")



p1 = Creature()
p2 = Creature()
print(p1.name)
print(p2.name)
print(p1.hp)
print(p2.hp)
p1.speak()
p2.speak()

del p2




class pan:
    def __init__(self, diameter=20) -> None:
        self.material = "cast_iron"
        self.diameter = diameter
        self.dirt = 0

    def fry(self):
        print("Жарю-жарю")
    
    def clean(self):
        print("Я чистая")
        self.dirt = 0
    
    def get_dirty(self):
        self.dirt += 10
        print("Эта сковорода испачканна на ", self.dirt, " процентов!")

pan1 = pan(diameter=500)

pan1.get_dirty()
pan1.clean()
print(pan1.material)
print(pan1.diameter)
print(pan1.dirt)

pan2 = pan()

pan2.get_dirty()
pan2.clean()
print(pan2.material)
print(pan2.diameter)
print(pan2.dirt)