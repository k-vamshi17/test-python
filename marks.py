noofsub=int(input("Enter no of Subjects:"))
Total_marks=0
for i in range(1,noofsub+1):
    sub=int(input("Enter marks of Subject"+str(i)+" marks:"))
    Total_marks+=sub
print(Total_marks)
if Total_marks/noofsub >=90:
    print("Total Marks =",Total_marks)
    print("Average =",Total_marks/noofsub)
    print("Grade = Execellent")
if Total_marks/noofsub >=50:
    print("Total Marks =",Total_marks)
    print("Average =",Total_marks/noofsub)
    print("Grade = Average")
if Total_marks/noofsub <50:
    print("Total Marks =",Total_marks)
    print("Average =",Total_marks/noofsub)
    print("Grade = Poor")