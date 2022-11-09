from huffman import HuffmanCoding
import sys

path = "sample.txt"

h = HuffmanCoding(path)

output_path = h.compress()
print("Путь сжатого файла: " + output_path)

#decom_path = h.decompress(output_path)
#print("Путь распакованного файла: " + decom_path)