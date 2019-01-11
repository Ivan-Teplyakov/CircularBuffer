'''
Created on 8 January. 2019 y.
This module contains the simple ring buffer realization 

@author: Ivan
'''

class RingBuffer():
    
    """ Class that implements ring buffer """
    def __init__(self, size_max = 5):
        """ Creation and initialization ring buffer parameters"""
        """
            max represents the length of ring buffer 
            volume expresses content of ring buffer
            headPointer indicates starting location
            tailPointer indicates ending location
        """
        #list.__init__([])
        self.max = size_max
        self.volume = [0 for value in range(size_max)]
        self.headPointer = 0
        self.tailPointer = 0
    
    def append(self, data):
        """Adding data to ring buffer"""
        if type(data) is int:
            if self.headPointer < self.max:
                self.volume[self.headPointer] = data
                self.headPointer += 1
            else:
                self.rewritten(data)
        else: raise TypeError("You should append integer type data to the ring buffer")         
    
    def rewritten(self, data):
        """Rewriting data to ring buffer if the last is full"""
        self.volume[abs(self.max - self.headPointer) % self.max] = data
        self.headPointer += 1
        if abs(self.max - self.headPointer)% self.max == 0:
            self.tailPointer = self.tailPointer
        else:
            self.tailPointer = abs(self.max - self.headPointer) % self.max
        if self.headPointer == 2*self.max:
            self.headPointer = self.max
    
    def get(self):
        """Getting data from ring buffer"""
        self.volume[self.tailPointer] -= self.volume[self.tailPointer]
        self.tailPointer += 1
        self.headPointer %= self.max
        if self.tailPointer >= self.max:
            self.tailPointer = 0
        if self.headPointer % self.max == self.tailPointer:
            self.tailPointer = 0
            self.headPointer = 0 
             
    def __len__(self):
        """Redefining of RingBuffer instance length"""
        return len(self.volume)
    def __repr__(self):
        """Redefining of string operation with RingBuffer instances"""
        return repr(self.volume)
    def __call__(self):
        """Redefining of function operation with RingBuffer instances"""
        temp = []
        temp.extend(self.volume)
        return temp

if __name__ == '__main__':
    myBuffer = RingBuffer(10)
    
    for item in range(1, 35):
        myBuffer.append(item*10)
    print myBuffer

   

            

            
        
