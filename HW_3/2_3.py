#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5
#1 2 3 4 5
#6
#-> 5

N = int(input('Количество чисел: '))
lst_1=[int(input('Ввести число: ')) for i in range(N)]
x=int(input('Заданное число: '))
b=[abs(lst_1[i]-x) for i in range(len(lst_1))]
print(lst_1[b.index(min(b))])