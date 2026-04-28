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



     def _sift_down(self,index):
         left_child = 2 * index + 1
         right_child = 2 * index + 2

         
               




    