class Queue():
    def __init__(self):
        self._queue = []
    
    def enqueue(self,x):
        self._queue.append(x)

    def dequeue(self):
        if self.is_empty():
            return None
        
        return self._queue.pop(0)

    def is_empty(self):
        return len(self._queue) == 0
    
    def size(self):
        return len(self._queue)
    
    def print_from_bottom(self):
        for i in range(self.size()):
            print(self._queue[i])




  

    