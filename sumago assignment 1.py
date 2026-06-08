a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("Addition=",(a+b))
print("Subtraction=",(a-b))
print("Multiplication=",(a*b))
print("Division=",(a/b))
print("Modulus=",(a%b))
print("Exponentiation=",(a**b))


name    = input("Enter student name: ")
marks1  = float(input("Enter marks in Subject 1: "))
marks2  = float(input("Enter marks in Subject 2: "))
marks3  = float(input("Enter marks in Subject 3: "))

total      = marks1 + marks2 + marks3
average    = total / 3
percentage = (total / 300) * 100

print("\n--- Result ---")
print("Student :", name)
print("Total   :", total)
print("Average :", average)
print("Percent :", percentage, "%")


basic  = float(input("Enter Basic Salary: "))
hra    = basic * 0.20   # 20% HRA
da     = basic * 0.10   # 10% DA
gross  = basic + hra + da

pf     = basic * 0.12   # 12% PF deduction
tax    = gross * 0.05   # 5% tax
deduction = pf + tax

net    = gross - deduction

print("\nGross Salary :", gross)
print("Deductions   :", deduction)
print("Net Salary   :", net)


p1   = float(input("Price of item 1: "))
q1   = int(input("Quantity of item 1: "))

p2   = float(input("Price of item 2: "))
q2   = int(input("Quantity of item 2: "))

p3   = float(input("Price of item 3: "))
q3   = int(input("Quantity of item 3: "))

total = (p1 * q1) + (p2 * q2) + (p3 * q3)
discount = total * 0.05   # 5% discount
bill  = total - discount

print("\nSubtotal :", total)
print("Discount :", discount)
print("Net Bill :", bill)


units = int(input("Enter units consumed: "))

# Slab rates
if units <= 100:
    bill = units * 3.50
elif units <= 300:
    bill = 100 * 3.50 + (units - 100) * 5.00
else:
    bill = 100 * 3.50 + 200 * 5.00 + (units - 300) * 7.00

tax   = bill * 0.10
total = bill + tax

print("Units    :", units)
print("Charges  :", bill)
print("Tax (10%):", tax)
print("Total    :", total)


age    = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))
score  = int(input("Enter credit score: "))

if age >= 21 and salary >= 25000 and score >= 700:
    print("✅ Eligible for loan")
elif age >= 21 and salary >= 15000:
    print("⚠️  Eligible for small loan only")
else:
    print(" Not eligible for loan")


age       = int(input("Enter age: "))
citizen   = input("Are you a citizen? (yes/no): ")
registered = input("Are you registered? (yes/no): ")

if age >= 18 and citizen == "yes" and registered == "yes":
    print("✅ You can vote!")
elif age < 18:
    print(" Too young to vote")
elif citizen != "yes":
    print(" Not a citizen")
else:
    print(" Not registered to vote")


years  = int(input("Years of experience: "))
rating = float(input("Performance rating (1-10): "))
absent = int(input("Days absent this year: "))

if years >= 2 and rating >= 8 and absent <= 5:
    print("✅ Eligible for 20% bonus")
elif years >= 1 and rating >= 6:
    print("⚠️  Eligible for 10% bonus")
else:
    print("❌ Not eligible for bonus")


percentage = float(input("Enter 12th percentage: "))
entrance   = int(input("Enter entrance score: "))

if percentage >= 75 and entrance >= 80:
    print("✅ Admitted to General Engineering")
elif percentage >= 60 and entrance >= 60:
    print("⚠️  Admitted to Management Quota")
elif percentage >= 50 or entrance >= 50:
    print("⚠️  Eligible for diploma program")
else:
    print("❌ Not eligible for admission")


marks  = float(input("Enter percentage: "))
income = float(input("Enter annual family income: "))
attend = float(input("Enter attendance %: "))

if marks >= 85 and income <= 200000 and attend >= 75:
    print("✅ Full scholarship awarded")
elif marks >= 75 and income <= 400000:
    print("⚠️  Partial scholarship awarded")
else:
    print("❌ Not eligible for scholarship")


students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

name = input("Enter student name to search: ")

if name in students:
    print(name, "is enrolled in the class.")
else:
    print(name, "is NOT found in the records.")


employees = ["E101", "E102", "E103", "E104", "E105"]

emp_id = input("Enter Employee ID: ")

if emp_id in employees:
    print("Employee", emp_id, "found in records.")
else:
    print("Employee", emp_id, "does NOT exist.")


products = ["Laptop", "Phone", "Tablet", "Watch", "Earbuds"]

item = input("Enter product name: ")

if item in products:
    print(item, "is available in store.")
else:
    print(item, "is not available.")


books = ["Python Basics", "Data Structures",
         "Algorithm Design", "Machine Learning"]

title = input("Enter book title: ")

if title in books:
    print("📚 Book is available in library.")
else:
    print("📚 Book not found in library.")


if title not in books:
    print("You may request this book.")


enrolled = ("Python", "Java", "C++", "Web Dev", "AI/ML")

course = input("Enter course name: ")
student = input("Enter student name: ")

if course in enrolled:
    print(student, "is enrolled in", course)
else:
    print(student, "is not enrolled in", course)


list1 = [1, 2, 3]
list2 = list1         
list3 = [1, 2, 3]     

print("list1 is list2:", list1 is list2)   
print("list1 is list3:", list1 is list3)   
print("list1 == list3:", list1 == list3)   
print("id(list1):", id(list1))
print("id(list3):", id(list3))


x = None
y = None
z = 10

if x is None:
    print("x is None — no value assigned")

print("x is y:", x is y)         
print("z is not None:", z is not None)  
print("x is not z:", x is not z)       


emp1 = {"id": "E101", "name": "Ravi"}
emp2 = emp1                       
emp3 = {"id": "E101", "name": "Ravi"}  

print("emp1 is emp2:", emp1 is emp2)   
print("emp1 is emp3:", emp1 is emp3)   
print("emp1 == emp3:", emp1 == emp3)   

if emp2 is emp1:
    print("emp2 points to the same record as emp1")


a = 100
b = 100
c = 1000
d = 1000

print("a is b (100):", a is b)   
print("c is d (1000):", c is d) 

print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))
print("id(d):", id(d))


# Variable Reference Analysis
x = [10, 20, 30]
y = x            
z = x[:]         

y.append(40)      

print("x:", x)  
print("y:", y)    
print("z:", z)    

print("x is y:", x is y)    
print("x is z:", x is z)    
print("x is not z:", x is not z)  