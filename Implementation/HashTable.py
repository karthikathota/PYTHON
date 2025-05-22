class HashTable:
    def __init__(self,size = 7):
        self.data_map = [None]*size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash+ord(letter)*23)%len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)
    # Seperate 
    def set_item(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])
    
    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


mht = HashTable()
mht.set_item("car",2000)
mht.set_item("bike",1000)
mht.set_item("cycle",200)
mht.set_item("apple",20)
mht.set_item("mango",220)
mht.set_item("banana",10)
print(mht.get_item("car"))
print(mht.keys())
#mht.print_table()