'''
def longest_common_substring(s1, s2):
    maxLongest = 0
    offset = 0
    for i in range(0, len(s1)):
        longest = 0
        if ((i == len(s1) - len(s2) - 2)):
            break
        for j in range(0, len(s2)):
            if (i+j < len(s1)):
                if s1[i+j] == s2[j]:
                    longest = longest + 1
                    if (maxLongest < longest):
                        maxLongest = longest
                        offset = i
                else:
                    break
            else:
                break
    return maxLongest, offset
'''

def encode_lz78(text):
    dictionary = dict()
    i = 0
    index = 1
    encodedNumbers = []
    encodedLetters = []
    while i < len(text):
        stringToBeSaved = text[i]
        indexInDictionary = 0
        while stringToBeSaved in dictionary:
            indexInDictionary = dictionary[stringToBeSaved]
            if (i == len(text) - 1):
                stringToBeSaved = " "
                break
            i = i + 1
            stringToBeSaved = stringToBeSaved + text[i]
        encodedNumbers.append(indexInDictionary)
        encodedLetters.append(stringToBeSaved[len(stringToBeSaved) - 1])
        if (stringToBeSaved not in dictionary):
            dictionary[stringToBeSaved] = index
            index = index + 1
        i = i + 1

    return encodedNumbers, encodedLetters, dictionary

l = []
def decode_lz78(encodedNumbers, encodedLetters, dictionary):
    i = 0
    while i < len(encodedNumbers):
        if (encodedNumbers[i] != 0):
            l.append(list(dictionary.keys())[list(dictionary.values()).index(encodedNumbers[i])])
        l.append(encodedLetters[i])
        i = i+1
    return l


print("LZ78 Алгоритм сжатия")
print("=================================================================")
h = int(input("Введите 1, если вы хотите ввести в командном окне, 2, если вы используете какой-либо файл:"))
if h == 1:
    stringToEncode = input("Введите строку, которую вы хотите сжать:")
elif h == 2:
    file = input("Введите имя файла:")
    with open(file, 'r') as f:
        stringToEncode = f.read()
else:
    print("Вы ввели неверный ввод")
print ("Введенная строка:",stringToEncode)
[encodedNumbers, encodedLetters, dictionary] = encode_lz78(stringToEncode)
a = [encodedNumbers, encodedLetters, dictionary]
print("Сжатый файл, создан как compressed.txt")
output = open("compressed.txt","w+")
output.write(str(a))
print("Закодированная строка: ", end="")
i = 0
while i < len(encodedNumbers):
    print ("{",encodedNumbers[i],":", encodedLetters[i],"}", end=" ")
    i = i + 1
print('\n')
decode_lz78(encodedNumbers, encodedLetters, dictionary)
print("Декодированная строка:", "".join(l))