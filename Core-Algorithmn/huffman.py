from PIL import Image
from collections import Counter, deque
import heapq
import os
import struct
from typing import Tuple, Dict

MAGIC = b'HUFIMG2' #this is the file identifier

class Node: 
    def __init__(self, freq: int, value: int = None, left=None, right=None):
        self.freq = freq
        self.value = value
        self.left = left
        self.right = right

    def __It__(self, other):
        return self.freq < other.freq
    
def image_to_raw_bytes(img: Image.Image, target_mode="RGBA") -> Tuple[bytes, Tuple[int, int], str]:
    if img.mode != target_mode:
        img = img.convert(target_mode)
    return img.tobytes(), img.size, target_mode

def build_freq_table(data: bytes) -> Counter
    return Counter(data)

def build_huffman_tree(freq_table: Counter) -> Node:
    heap = []
    for byte_val, freq in freq_table.items():
        node = Node(freq, value=byte_val)
        heapq.heappush(heap, (freq, node))
    
    if not heap: 
        return None
    if len(heap) == 1:
        #edge: single symbol -> add dummy node so tree has two cildren
        freq, only = heapq.heappop(heap)
        root = Node(freq, left=only, right=Node(0, value=(0)))
        return root
    while len(heap) > 1:
        f1, n1 = heapq.heappop(heap)
        f1, n2 = heapq.heappop(heap)
        merged = Node(f1 + f2, left=n1, right=n2)
        heapq.heappush(heap, (merged.freq, merged))
    return heapq.heappop(heap)[1]

def generate_codes(root: Node) -> Dict[int, str]:
    code = {}

    def _walk(node: Node, prefix: str):
        if node is None:
            return
        if node.value is not None:
            #leaf
            codes[node.value] = prefix if prefix != "" else "0"
            return
        _walk(node.left, prefix + "0")
        _walk(node.right, prefix + "1")

    _walk(root, "")
    return codes



        