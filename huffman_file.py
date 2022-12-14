import heapq
import os
from math import log2

'''
Сжатие:
1. Создаем частотный словарь
2. Построить приоритетную очередь (используется MinHeap)
3. Создаем HuffmanTree, выбрав 2 мин. узла и объединив их.
4. Назначаем коды символам (обходя дерево от корня)
5. Закодировать введенный текст (путем замены символа его кодом)
6. Если общая длина финальных закодированных битовых потоков не кратна 8, добавляем к тексту отступы.
7. Сохраняем эту информацию заполнения (в 8 битах) в начале всего закодированного потока битов.
8. Запишем результат в выходной двоичный файл.

#TODO Декомпрессия:
1. Прочитать бинарный файл
2. Прочтите информацию об отступах. Удалите мягкие биты
3. Декодируйте биты - прочитайте биты и замените действительные биты кода Хаффмана символьными значениями.
4. Сохраните декодированные данные в выходной файл.
'''
class HuffmanCoding:
	def __init__(self, path):
		self.path = path
		self.heap = []
		self.codes = {}
		self.reverse_mapping = {}
	
	class HeapNode:
		def __init__(self, char, freq):
			self.char = char
			self.freq = freq
			self.left = None
			self.right = None

		#проверка частот нод (меньше чем)
		def __lt__(self, other):
			return self.freq < other.freq

        #проверка равности нод
		def __eq__(self, other):
			if(other == None):
				return False
			return self.freq == other.freq

	# функции для сжатия
	def make_frequency_dict(self, text): #частотный словарь - считает частоты и возвращает
		frequency = {}
		for character in text:
			if not character in frequency:
				frequency[character] = 0
			frequency[character] += 1
		return frequency

	def make_heap(self, frequency): #приоритетная очередь построенная с помощью сд.MinHeap 
		for key in frequency:
			node = self.HeapNode(key, frequency[key]) #создаем ноду которой передается символ и значение
			heapq.heappush(self.heap, node)             #пушим ноду в кучу

	def merge_nodes(self):                  #строит дерево huffmana. 
		while(len(self.heap)>1):    #пока длина кучи >1 ноды
			node1 = heapq.heappop(self.heap) #извлекаем 1 и 2 ноду из кучи
			node2 = heapq.heappop(self.heap)

			merged = self.HeapNode(None, node1.freq + node2.freq) #слияние нод, где параметры частоты обоих
			merged.left = node1
			merged.right = node2

			heapq.heappush(self.heap, merged) #пушим объед.ноду в кучу


	def make_codes_helper(self, root, current_code): #рекурсивный метод назначающий код символам
		if(root == None): #если ноды нет
			return

		if(root.char != None): #если символ ноды не none
			self.codes[root.char] = current_code #сохраняем значение кода текущего символа в словарь кодов
			self.reverse_mapping[current_code] = root.char
			return

		self.make_codes_helper(root.left, current_code + "0")
		self.make_codes_helper(root.right, current_code + "1")


	def make_codes(self): #назначает коды символам
		root = heapq.heappop(self.heap) #извлекаем root ноду из кучи
		current_code = ""
		self.make_codes_helper(root, current_code)


	def get_encoded_text(self, text): #заменяем символы кодом
		encoded_text = ""
		for character in text:
			encoded_text += self.codes[character]
		return encoded_text


	def pad_encoded_text(self, encoded_text): #отступы в закодированном файле
		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding):
			encoded_text += "0"

		padded_info = "{0:08b}".format(extra_padding)
		encoded_text = padded_info + encoded_text
		return encoded_text


	def get_byte_array(self, padded_encoded_text): #конвертируем биты в байты и возвращаем массив байтов
		if(len(padded_encoded_text) % 8 != 0): #если длина отформатированного закодированного текста не делится на 8
			print("Неправильные отступы в закодированном тексте")
			exit(0)

		b = bytearray()
		for i in range(0, len(padded_encoded_text), 8):
			byte = padded_encoded_text[i:i+8]
			b.append(int(byte, 2))
		return b


	def shannon(self, text): #считаем энтропию
		total = sum(text.values()) 
		return sum(freq / total * log2(total / freq) for freq in text.values())
		
	def compress(self):
		filename, file_extension = os.path.splitext(self.path) #разделяем расширение от имени файла
		output_path = filename + ".bin" #сохраняем как бинарный

		with open(self.path, 'r+') as file, open(output_path, 'wb') as output: #открываем input файл в read mode, output файл в write-binary
			text = file.read()
			text = text.rstrip() #удаляем ли	шние пробелы

			frequency = self.make_frequency_dict(text)
			self.make_heap(frequency)
			self.merge_nodes()
			self.make_codes()

			encoded_text = self.get_encoded_text(text)
			padded_encoded_text = self.pad_encoded_text(encoded_text)
			shannon_entropy = self.shannon(frequency)

			b = self.get_byte_array(padded_encoded_text) #делаем массив байтов
			output.write(bytes(b)) #записываем его в файл вывода
		
		
		print(f"Частотный словарь: \n{frequency}\n Коды символов: \n{self.codes}\n Закодированный текст: \n{encoded_text}\n Отформатированный закодированный текст: \n{padded_encoded_text}\n")
		
		print(f"Энтропия Шеннона: {shannon_entropy}")

		print("Файл сжат")

		print ("Размер входного файла: ", os.path.getsize(self.path), "byte")
		print ("Размер выходного файла: ", os.path.getsize(output_path), "byte")

		return output_path