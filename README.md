# huffman & lz78 algos (python) 3 <br>
huffman_string.py - для кодирорвания input строк и подсчета энтропии <br>
huffman_file.py - для кодирования и сжатия файлов <br>
lz78.py - алгоритм сжатия строки lz78 <br>
useHuffman.py - вызывает huffman_file.py <br>

<h1>Как работает Huffman </h1>

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


<h1>Как работает lz78 </h1>
Алгоритм LZ78 не использует буфер и скользящее окно. Вместо этого
он использует словарь.
Словарь – набор строк, которые встречаются в обрабатываемой
последовательности.<br>
Результат кодирования записывают в таблицу, содержащую 4 колонки:<br>
1. Содержимое словаря,<br>
2. Содержимое текущего пакета данных (содержимое считываемой строки),<br>
3. Пакет данных в виде <адрес словаря, следующий знак данных> (код),<br>
4. Адрес пакета данных.<br>

s – здесь хранится передаваемое сообщение.<br>
dictionary – создание изначально пустого словаря.<br>
i - переменная для передвижения по строке.<br>
arr_for_dict, arr_code, arr_content, arr_adr - в эти массивы будем
записывать информацию в ходе выполнения алгоритма и они нам будут
нужны в дальнейшем для красивого вывода результата работы алгоритма с
помощью библиотеки terminaltables, так как библиотека требует в аргументе
массив.<br>
Основной цикл while выполняется пока переменная i и не дойдет до
последнего символа передаваемого сообщения.<br>
Делаем проверку. Если символа нет в словаре, то тогда добавляем новую
пару в словарь. Создаем код. <0, символ>. 0 показывает, что данной буквы еще
никогда не было в словаре.<br>
Информацию в массивы добавляем с помощью встроенного метода
append<br>
Если же символ уже есть в словаре, то тогда создаем временную строку
str_temp, в которой будет храниться некоторая последовательность символов.
Добавляем в неё первый элемент. К переменной i прибавляем 1, что означает
что мы переходим к следующему символу в передаваемом сообщении. <br>
Если сочетание символов есть в словаре и переменная i стоит в конце сообщения,
тогда формируем код следующим образом <адрес словаря, #>, где # означает
конец сообщения.<br>
К str_temp прибавляем следующий символ из передаваемого сообщения.
Если такого сочетания символов нет в словаре, тогда добавляем новое
сочетание символов в словарь с определенным адресом и формируем код:
ставим адрес, соответствующий последнему найденному совпадению в
словаре и указываем следующий знак данных.<br>
Перед заходом на новую итерацию в главном цикле while, к адресу
прибавляем + 1, и к i тоже, что будет означать сдвиг вправо на единицу в
исходном сообщении.<br>
В этой части будем делать красивый вывод результата работы
алгоритма. Делаем это с помощью библиотеки terminaltables.<br>
В цикле for key in arr_content добавляем данные в массив arr_for_table,
который передадим аргументом в метод AsciiTable, и в результате на экран
выведется следующее:
