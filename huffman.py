from priorityQueue import PriorityQueue
from priorityQueue import Node


class HuffmanCodec:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pq = PriorityQueue()  # Senin yazdığın o meşhur yapı
        self.codes = {}            # Karakter -> Binary eşleşmesi (a: 010 gibi)
        self.reverse_codes = {}    # Binary -> Karakter eşleşmesi (010: a gibi)

    def _get_frequencies(self):
        
    
           with open(self.file_path, 'r', encoding='utf-8') as file:
               text = file.read()

    
           frequencies = {}
    
   
           for char in text:
              if char not in frequencies:
                 frequencies[char] = 0
              frequencies[char] += 1
        
           return frequencies

    def _build_priority_queue(self, frequencies):

        for char, freq in frequencies.items():
            new_node = Node(char, freq)
            self.pq.Push(new_node)




    def _build_huffman_tree(self):
        
       while(self.pq.number > 1):

         left_node = self.pq.pop()
         right_node = self.pq.pop()

         merged_freq = left_node.freq + right_node.freq
         parent_node = Node(None, merged_freq)

         parent_node.left = left_node
         parent_node.right = right_node

         self.pq.Push(parent_node)

       return self.pq.Pop()

         





    def _generate_codes(self, node, current_code):
        
        
        if node is None:
            return

   
        if node.char is not None:
           self.codes[node.char] = current_code
           return

   
        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def encode(self):
        
        freqs = self._get_frequencies()
        
        self._build_priority_queue(freqs)
        
        root = self._build_huffman_tree()
        
        self._generate_codes(root, "")
        
        # 5. Orijinal metni 0-1 dizisine çevir
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        
        return encoded_text
    

    def decode(self, encoded_text):
        decoded_output = ""
        current_node = root  
    
        for bit in encoded_text:
           if bit == '0':
              current_node = current_node.left  
           else:
              current_node = current_node.right 
            
       
           if current_node.char is not None:
              decoded_output += current_node.char 
              current_node = root  #
            
        return decoded_output
    


