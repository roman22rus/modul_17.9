sequence_str=(input("Введите последовательность чисел через пробел:"))
element = (input("Введите любое число :"))
sequence_str_list = list(sequence_str.split())
element_list = list(element.split())
number = [*sequence_str_list,*element_list]


for i in range(len(number)):
    for j in range(len(number)-i-1):
        if number[j]>number[j+1]:
            number[j],number[j+1]=number[j+1],number[j]
print("числа по возрастанию :",number)

def binary_search(number,element,left,right):
    if left>right:
        return False

    middle = (right+left)//2
    if number [middle]==element:
        return middle
    elif element<number[middle]:
        return binary_search(number,element,left,middle-1)
    else:
        return binary_search(number,element,middle+1,right)
element = int(input("введите число,индекс которого хотите узнать:"))
number=[ i for i in range(1,100)]
print("Индекс числа ",element ,":",binary_search(number,element,0,99))







