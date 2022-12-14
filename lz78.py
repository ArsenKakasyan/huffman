s = 'mama_myla_ramy'
dict_max_size = 4
dictionary = {}
stack = []

address = 1
i = 0

# https://stackoverflow.com/questions/1756992/how-to-remove-the-oldest-element-from-a-dictionary
# https://stackoverflow.com/questions/2437617/how-to-limit-the-size-of-a-dictionary

arr_for_dict = [] #для хранения словаря в виде массива
arr_code = [] #хранение кода
arr_content = [] #хранение содержания считываемой строки
arr_adr = [] #хранение адресов

while(i < len(s)):
    from_dict_to_arr = str(list(dictionary.keys()))
    arr_for_dict.append(from_dict_to_arr[1:-1])

    if(s[i] in dictionary) == False: #если буквы нет в словаре
        dictionary[s[i]] = address #добавляем новую пару в словарь

        stack.append(s[i]) #добавляем в стек
        if len(stack) > dict_max_size:
            stack.pop(0)
            

        code = '<0, ' + s[i] + '>'
        arr_adr.append(address)
        arr_code.append(code)
        arr_content.append(s[i])

    else: # если символ есть в словаре
        str_temp = s[i]

        while(True):
            i = i + 1

            if (((str_temp in dictionary) == True) and (i> (len(s)-1))):
                code = '<' + str(dictionary[str_temp]) + ', #' + '>'
                arr_code.append(code)
                arr_content.append(str_temp)
                arr_adr.append(address)
                break
            str_temp = str_temp + s[i]

            if (str_temp in dictionary) == False:
                dictionary[str_temp] = address
                code = '<' + str(dictionary[str_temp[:-1]]) + ', ' + str_temp[-1] + '>'
                arr_adr.append(address)
                arr_code.append(code)
                arr_content.append(str_temp)
                break
    address = address + 1
    i = i + 1

arr_for_table = []
arr_for_table.append(['содержимое словаря', 'содержимое считываемой строки', 'код', 'адрес'])
ii = 0

for key in arr_content:
    att_tmp = []
    att_tmp.append(arr_for_dict[ii])
    att_tmp.append(arr_content[ii])
    att_tmp.append(arr_code[ii])
    att_tmp.append(arr_adr[ii])
    ii = ii + 1
    arr_for_table.append(att_tmp)


from terminaltables import AsciiTable

resultTable = AsciiTable(arr_for_table)
resultTable.inner_heading_row_border = True
resultTable.outer_border = False
resultTable.inner_row_border - False
print(resultTable.table)