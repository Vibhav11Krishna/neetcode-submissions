class DynamicArray:
    
    def __init__(self, capacity):
        """
        Initializes an empty array with a starting capacity.
        """
        self.capacity = capacity
        self.size = 0
        # Initialize a fixed-size list filled with 0s to represent raw memory
        self.arr = [0] * capacity

    def get(self, i):
        """
        Returns the element at index i.
        """
        return self.arr[i]

    def set(self, i, n):
        """
        Sets the element at index i to n.
        """
        self.arr[i] = n

    def pushback(self, n):
        """
        Pushes the element n to the end of the array.
        Resizes the array first if it is completely full.
        """
        if self.size == self.capacity:
            self.resize()
            
        # Place the element at the next available slot and increase size
        self.arr[self.size] = n
        self.size += 1

    def popback(self):
        """
        Pops and returns the element at the end of the array.
        """
        # The last element is at index (size - 1)
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def resize(self):
        """
        Doubles the capacity of the array.
        """
        # 1. Double the capacity tracker
        self.capacity = self.capacity * 2
        
        # 2. Create a brand new, larger array
        new_arr = [0] * self.capacity
        
        # 3. Copy all elements from the old array into the new array
        for i in range(self.size):
            new_arr[i] = self.arr[i]
            
        # 4. Tell our class to use the new array from now on
        self.arr = new_arr

    def getSize(self):
        """
        Returns the number of elements currently in the array.
        """
        return self.size

    def getCapacity(self):
        """
        Returns the current maximum capacity.
        """
        return self.capacity
