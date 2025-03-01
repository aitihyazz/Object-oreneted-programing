class paraot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
a =paraot("blu",10)
b=paraot("woo",9)
print("blu is a {}".format(a.species))
print("woo is a {}".format(b.species))
print("{} is {} years old".format(a.name,a.age))
print("{} is {} ears old".format(b.name,b.age))
    