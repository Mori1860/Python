# First code
# List
ice_cream = [ 'cookie Dough' , 'Strawberry' , 'Chocolate']
print(ice_cream)
ice_cream.append('chocobar')
print(ice_cream)

# Nested_list(list within a list)   []
first_list = ['Vanilla' , '3' , ['Spoon' , 'Scopes'] , True ]
print(first_list[2][1])

# indexing  []
ice_cream[0] = 'Sugar'
print(ice_cream)

# Tuples are list but immutable  ()    so append could not be worked
tuple_scoops = (1,2,2,8,5)

# set   {}    contain no duplicates
my_daily_pints = {1,5,4,7,6,8,5,47}
print(my_daily_pints)
mah_daily_pints = {5,8,7,9,3,6,9,2,55,21,74}
print(my_daily_pints | mah_daily_pints)  # all unique values between two sets
print(my_daily_pints & mah_daily_pints)  # all in common values between two sets
print(my_daily_pints - mah_daily_pints)  # all different values between two sets
print(my_daily_pints ^ mah_daily_pints)  # different values in all sets 

print("\n  ################################################ \n")
# Dictionaries
# key/Value pair. 

First_dict = {"Name" : "Mori" , "SirName" : "Bakht" , "jobTotle" : "CEO" , "Age" : 38}
print(First_dict['Age'])
First_dict.update({"Name" : "Mah" , "Age" : 35 , "Weight" : 66})
print(First_dict)
del First_dict["Weight"]
print(First_dict)

# Operators
not (50>70)
    # Membership operators
        # in
        # returns true if a sequence with the specified value is present in the object
string_in = "I love chacolate ice cream"
print(string_in)
print("love" in string_in)
print("live" not in string_in)

# IF statement & nested
if 25 > 10 and "chocobar" in ice_cream:
    print("if worked!")
    if "Vanilla" in first_list:
        print("awesome.................") 
elif 25 > 10 and 4 in ice_cream:
    print("elif 1 worked!")
elif 25 < 10 and 5 in ice_cream:
    print("WOW!!")
else:
    print("else worked!!!..")


# For loop
for i in ice_cream:
    print(i + " -> " + i[2])

for i in First_dict.values():
    print(i)

for i in First_dict.keys():
    print(i)

for key , value in First_dict.items():
    print(key, '-->' , value)

print(first_list)

#        Nested For Loop
for one in ice_cream:
    for two in first_list:
        if two == "3":
            print(one , "by" , two)
        else:
            print(one , "with" , two)

print("\n #####################################")
# while loop
#  is use to iterate a block of code as long as a certain condition is met
# but in for loop iterate in an entire sequence regardless of the condition
number = 5
while number <= 10:
    number = number + 1
    
    if number == 8:
        continue
    print(number)
else:
    print("no linger exists")

print("\n #####################################")
# functions
def first_func():
    print("We will do it")
first_func()

def number_args(*number):
    print(number[2] * number[4])
number_args(1,2,2,6,56,8,69,5,9)

args_number = (3,3,4,5,6,7,8,99,3,4,6,77,33,3,)
def the_number(*numbers):
    print(numbers[2]+1)
the_number(*args_number)

def number_two(power, number):
    print(number ** power)
number_two(number = 3 , power= 5)


print("\n #########################################")
# Converting data types
int_num = 4
str_num = "7"
converted_str_to_int = int(str_num)
print(int_num * converted_str_to_int )

print(list(First_dict.values()))
print(list(First_dict.keys()))

print("\n #########################################")
# BML Calculator

weight = int(input("Enter your weight in pounds : "))
height = int(input("Enter your weight in inches : "))
BMI = (weight * 703) / (height  ** 2  )
print(BMI)
if 0 < BMI :
    if BMI < 18.5:
        print("Classification : Underwight      Health Risk : Minimal " )
    elif 24.9 > BMI >= 18.5 :
        print("Classification : Normal      Health Risk : Minimal " )
    elif 29.9 > BMI >= 25 :
        print("Classification : Overweight      Health Risk : Increased " )
    elif 34.9 > BMI >= 30 :
        print("Classification : Obese      Health Risk : High " )
    elif 39.9 > BMI >= 35 :
        print("Classification : Severely Obese      Health Risk : Very High " )
    else:
        print("Classification : Morbidly Obese      Health Risk : Extremely High " )
else:
    print("Enter a valid positive number.... ")


print("\n ############################################")
# Automatic file sorting in file explorer
import os, shutil
path = "/Users/default/Downloads/"
Files_name = os.listdir(path)
print(os.path.exists("CSV Files"))
Folder_names = ["CSV Files" , "Excel Files" , "Images" , "Text Files" , "Videos" , "PDF Files" , "DTA Files" , "Software" , "Music"]
for loop in range(0,9):
    if not os.path.exists(path + Folder_names[loop]):
        print(os.path.exists(path + Folder_names[loop]))
        os.makedirs(path + Folder_names[loop])

for file in Files_name:
    if ".csv" in file:
        shutil.move(path + file , path + "CSV Files/" + file)
    if ".xlsx" and ".xls" in file:
        shutil.move(path + file , path + "Excel Files/" + file)
    if ".docx" and ".txt" and ".TXT" in file:
        shutil.move(path + file , path + "Text Files/" + file)
    if ".txt" in file:
        shutil.move(path + file , path + "Text Files/" + file)
    if ".TXT" in file:
        shutil.move(path + file , path + "Text Files/" + file)
    if ".pdf" in file:
        shutil.move(path + file , path + "PDF Files/" + file)
    if ".MOV" and ".mp4" and ".MP4" in file:
        shutil.move(path + file , path + "Videos/" + file) 
    if ".jpeg" and ".heic" and ".HEIC" and "IMG_" and ".png" and ".jpg" and ".JPG" and ".JPEG" and ".PNG" and "HEIF" in file:
        shutil.move(path + file , path + "Images/" + file)
    if ".heic" in file:
        shutil.move(path + file , path + "Images/" + file)
    if ".HEIC" in file:
        shutil.move(path + file , path + "Images/" + file)
    if ".dta" and ".DTA" in file:
        shutil.move(path + file , path + "DTA Files/" + file)
    if "dmg" in file:
        shutil.move(path + file , path + "Software/" + file)
    if ".jpeg" in file:
        shutil.move(path + file , path + "Images/" + file)
    if ".png" in file:
        shutil.move(path + file , path + "Images/" + file)
    if ".mp3" in file:
        shutil.move(path + file , path + "Music/" + file)
     

