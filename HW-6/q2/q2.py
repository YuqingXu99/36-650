class Queue:
    inner_list = []
    counter = 0
    def enqueue(self, value):
        self.inner_list.insert(0, value)
        self.counter = self.counter + 1
        return value
        
    def dequeue(self):
        self.counter = self.counter - 1
        value = self.inner_list.pop(self.counter)
        return value

    def delete(self, value):         
        for i in range(len(self.inner_list)):
            tmp = self.dequeue()
            if tmp != value:
                self.enqueue(tmp)
        return self

# test case
obj = Queue ()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)

obj.delete(7)
print(obj.dequeue())