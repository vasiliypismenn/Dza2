# Задание 1.4. Задайте список из N элементов, заполненных числами
#  из промежутка [-N, N].
# Найдите произведение элементов на позициях на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число '))
print("задан список: ")
spis = [i for i in (range(-N, N+1))]
print(spis)
    
f = open('file.txt','r')   # открытие файла для чтения
al =  (f.read(3))           # чтение 3 символов из file.txt
f.close()                  # закрытие файла

x = [int(a) for a in str(al)]
x1 = x[0]
x2 = x[1]
x3 = x[2]

print("выбираются индексы списка: ", x1, x2 ,x3)
al1 = spis[x1]
al2 = spis[x2]
al3 = spis[x3]
print("им соответствуют числа списка: ",al1,al2,al3)
pr = al1*al2*al3
print("произведение этих чисел равно: ",pr)