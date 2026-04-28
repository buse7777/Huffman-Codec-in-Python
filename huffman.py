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








        pass

    def _build_huffman_tree(self):
        """Kuyruktan ikişer çekip ağacı inşa eden o efsane döngü."""
        pass

    def _generate_codes(self, node, current_code):
        """Ağaç üzerinde gezip kimin kodu '01' kimin '10' onu belirler."""
        pass

    def encode(self):
        """Metni sıkıştırılmış (0101 şeklinde) bir string'e çevirir."""
        pass

    def decode(self, encoded_text):
        """O karmaşık 0101'leri tekrar okunabilir metne dönüştürür."""
        pass
    


