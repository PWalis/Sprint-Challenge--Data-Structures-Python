class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # if current is greater or equal to capacity reset current append and add 1 to current
    if self.current >= self.capacity:
      self.current = 0
      self.storage[self.current] = item
      self.current += 1
    # other wise just replace item at index current 
    else:
      self.storage[self.current] = item
      self.current += 1


  def get(self):
    # print everything expect None values
    return [i for i in self.storage if i != None]
    

rb = RingBuffer(3)
rb.append('a')
rb.append('b')
# rb.append('c')
# rb.append('d')
print(rb.get())