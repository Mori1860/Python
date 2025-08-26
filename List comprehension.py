numbers1 = [1,2,3,5,6,6,5,9,5,8,5,9,8,9]
number1 = [number * number for number in numbers1 ]
print(number1)
even_numbers1 = [number for number in number1 if number % 2 == 0 ]
print(even_numbers1)

list = [1,2,5,4,8,7,8,9,5,4,8,77,99,66,558,3326,5874500]
new_list = [(num+100)*3 for num in list ]
print(new_list)




numbers= [1,2,3,5,6,6,5,9,5,8,5,9,8,9]

double_num = []
for num in numbers:
    double_num.append(num*2)
    print(double_num)

numbers= [1,2,3,5,6,6,5,9,5,8,5,9,8,9]
double_num = [num*2 for num in numbers]
print(double_num)

