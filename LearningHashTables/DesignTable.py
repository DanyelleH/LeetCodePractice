class MyHashSet:
    def __init__(self):
        self.set=[]
        

    def add(self, key):
        if key not in self.set:
            self.set.append(key)
    

    def contains(self, key):
        if key in self.set:
            return True
        else:
            return False
        
    def remove(self,key):
        if key in self.set:
            self.set.remove(key)

# obj= MyHashSet()
# obj.add(1)
# obj.add(2)
# obj.add(2)
# print(obj.set)


class MyHashMap:
    def __init__(self):
        self.map=[]

    def put(self, key, value):
        for i, items in enumerate(self.map):
            if items[0] == key:
                self.map[i] = [key,value]
                return
        self.map.append([key, value])
        

    
    def get(self,key):
        for item in self.map:
            if item[0] == key:
                return(item[1])
        return -1


    def remove(self,key):
        for item in self.map:
            if item[0] == key:
                self.map.remove(item)

obj=MyHashMap()
obj.put(1,1)
print(obj.map)
obj.put(2,2)
obj.get(1)
obj.get(3)
obj.put(2,1)
obj.remove(2)
print(obj.map)
