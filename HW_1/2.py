#Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов 
# сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#6 -> 1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

s=int(input("Ввести количество журавликов: "))
print(s//6, "количество журавликов, которое сделал Петя")
print(s//6*2*2, "количество журавликов, которое сделала Катя")
print(s//6, "количество журавликов, которое сделал Сережа")