import random
def generate_surname():
    names = ["Smith" ,  "Johnson", "Williams" , "Black", "Hammer", "King", "Brown", "Jamieson", "Davis", "Rodrigers"]
    return random.choice(names)


students = [{'matriculation_id': 10000 + i , 'surname' : generate_surname()} for i in range(200)]

with open ("mock_student.txt" , 'w') as file:
    for student in students: 
        file.write(f"{student['matriculation_id']} ; {student['surname']}\n")

with open ('mock_student.txt' , 'r') as file:
    for line in file:
        matriculation_id, surname = line.strip().split(';')
        matriculation_id = int(matriculation_id)
        if matriculation_id == 10011:
            print(f"Surname of student with matriculation ID: {matriculation_id} {surname}")
            break