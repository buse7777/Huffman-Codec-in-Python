class PriorityQueue:
     def __init__(self):
       
         self.array = []
         self.number = 0
        

     def Push(self, element):
          


          
          self.array.append(element)
          self.number+=1

          if(len(self.array) > 1):
               self._sift_up(len(self.array) - 1)




     def _sift_up(self, index):
     
        parent_index = (index - 1) // 2

   
        if index <= 0:
           return
    
    
        if self.array[index].freq < self.array[parent_index].freq:
        
           self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
        
        
           self._sift_up(parent_index)


     def _sift_down(self, index):
          smallest = index
          left = 2 * index + 1
          right = 2 * index + 2
          n = len(self.array) 

    
          if left < n and self.array[left].freq < self.array[smallest].freq:
             smallest = left

   
          if right < n and self.array[right].freq < self.array[smallest].freq:
             smallest = right

    
          if smallest != index:
             self.array[index], self.array[smallest] = self.array[smallest], self.array[index]
             self._sift_down(smallest) 
               

     def Pop(self):
    
        en_kucuk = self.array[0] 
    
  
        sonuncu = self.array.pop() 
        if len(self.array) > 0:
             self.array[0] = sonuncu
        
        
             self._sift_down(0) 
        
        return en_kucuk



    