#Countung instances

class Item():
    counter = 0

    def __init__(self):
        #print(id(Item))
        Item.counter += 1
        #print(id(self))
        self.counter = Item.counter

    def numbObjs(self):
        return self.counter

n = 5
for _ in range(1, n):
    obj = Item()
    print(obj.counter)
