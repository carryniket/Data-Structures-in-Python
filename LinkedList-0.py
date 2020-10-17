lf.root = this_node.get_next()
                self.size -= 1
                return True		# data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
print("size="+str(myList.get_size()))
myList.remove(8)
print("size="+str(myList.get_size()))
print(myList.remove(12))
print("size="+str(myList.get_size()))
print(myList.find(5))
