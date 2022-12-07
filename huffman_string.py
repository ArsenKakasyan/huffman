from math import *
from sys import *

global probabilities
probabilities = []
'''
Как работает код:
1.Получаем строку и вычисляем частоту каждого символа в строке
2.Используя частоту, получаем вероятности
3.Используя алгоритм, вычисляем коды Хаффмана
4.Для кодов Хаффмана вычисление означает длину, дисперсию и энтропию.

Как работает алгоритм для вычисления кодов Хафмана:
1.Сначала мы сортируем вероятности в порядке убывания. Это необходимо для присвоения кодов каждому символу в соответствии с их частотой.
2.Запустим цикл for от 0 до длины строки-2
3.Для первого символа назначим 1 в качестве кода по умолчанию.
4.Для следующих символов проверяем предыдущие символы
        Если 1- добавить 0
        Если 11- добавить 1
        Если 10 - добавить 0
        Если 111 - добавить 1
5.После того, как коды Хаффмана сгенерированы, прочитаем их в обратном порядке, чтобы получить final_code. Это делается для генерации кода, как это делается при обходе дерева.
6.final_code — это список, содержащий все коды Хаффмана в порядке вероятностей.
'''

class HuffmanCode:
    def __init__(self,probability):
        self.probability = probability

    def position(self, value, index): #используется для вставки битов в существующий код, вычисленный в n-3 предыдущих итерациях, где n — длина.
        for j in range(len(self.probability)):
            if(value >= self.probability[j]):
                return j
        return index-1

    def characteristics_huffman_code(self, code): #Эта функция генерирует среднюю длину кодов, энтропию, дисперсию и эффективность. 
        length_of_code = [len(k) for k in code]

        mean_length = sum([a*b for a, b in zip(length_of_code, self.probability)])

        print("Энтропия: %f" % mean_length)
        #print("Эффективность кода: %f" % (entropy_of_code/mean_length))

    def compute_code(self):
        num = len(self.probability)
        huffman_code = ['']*num

        for i in range(num-2):
            val = self.probability[num-i-1] + self.probability[num-i-2]
            if(huffman_code[num-i-1] != '' and huffman_code[num-i-2] != ''):
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            elif(huffman_code[num-i-1] != ''):
                huffman_code[num-i-2] = '0'
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
            elif(huffman_code[num-i-2] != ''):
                huffman_code[num-i-1] = '1'
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            else:
                huffman_code[num-i-1] = '1'
                huffman_code[num-i-2] = '0'

            position = self.position(val, i)
            probability = self.probability[0:(len(self.probability) - 2)]
            probability.insert(position, val)
            if(isinstance(huffman_code[num-i-2], list) and isinstance(huffman_code[num-i-1], list)):
                complete_code = huffman_code[num-i-1] + huffman_code[num-i-2]
            elif(isinstance(huffman_code[num-i-2], list)):
                complete_code = huffman_code[num-i-2] + [huffman_code[num-i-1]]
            elif(isinstance(huffman_code[num-i-1], list)):
                complete_code = huffman_code[num-i-1] + [huffman_code[num-i-2]]
            else:
                complete_code = [huffman_code[num-i-2], huffman_code[num-i-1]]

            huffman_code = huffman_code[0:(len(huffman_code)-2)]
            huffman_code.insert(position, complete_code)

        huffman_code[0] = ['0' + symbol for symbol in huffman_code[0]]
        huffman_code[1] = ['1' + symbol for symbol in huffman_code[1]]

        if(len(huffman_code[1]) == 0):
            huffman_code[1] = '1'

        count = 0
        final_code = ['']*num

        for i in range(2):
            for j in range(len(huffman_code[i])):
                final_code[count] = huffman_code[i][j]
                count += 1

        final_code = sorted(final_code, key=len)
        return final_code

string = input("Введите строку для кодирования Huffman: ")

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
length = len(string)

probabilities = [float("{:.2f}".format(frequency[1]/length)) for frequency in freq]
probabilities = sorted(probabilities, reverse=True)

huffmanClassObject = HuffmanCode(probabilities)
P = probabilities

huffman_code = huffmanClassObject.compute_code()
'''
# print huffman tree    
print('Huffman tree:')
for i in range(len(huffman_code)):
    print(freq[i][0] + ' : ' + huffman_code[i])

print("Символ\tЧастота\tКод")
for i in range(len(freq)):
    print("{}\t{}\t{}".format(freq[i][0], freq[i][1], huffman_code[i]))

''' 
print(' Huffman tree')
print('-------------------')

for id,char in enumerate(freq):
    if huffman_code[id]=='':
        print(' %-4r |%12s' % (char[0], 1))
        continue
    print(' %-4r |%12s' % (char[0], huffman_code[id]))
'''
print("Символ\tЧастота\tКод")
print('---------------------------------')

for i in range(len(freq)):
    print( "{}\t{}\t{}".format(freq[i][0], freq[i][1], huffman_code[i]))
'''

huffmanClassObject.characteristics_huffman_code(huffman_code)