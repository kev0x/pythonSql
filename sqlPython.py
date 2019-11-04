import pymysql
from tkinter import *
from tkinter import ttk

root = Tk()

tree = ttk.Treeview(root)
tree.pack()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

#Connecting to a database
db = pymysql.connect("127.0.0.1", "root", "Smylesmila2", "university")
cursor = db.cursor()
sql = "select Student.Panther_ID, Student.Name, Student.DOB from Student"
cursor.execute(sql)
result = cursor.fetchall()

#Setting up the tree
tree["columns"] = ("Student_Name", "Student_DOB")
tree.column("#0", width=100)
tree.column("Student_Name", width=100)
tree.column("Student_DOB", width=100)

tree.heading("#0", text="Panther ID")
tree.heading("Student_Name", text="Name")
tree.heading("Student_DOB", text="Birth year")

for i in range(0, len(result)):
    tree.insert("", i, text=str(result[i][0]), values=(str(result[i][1]), str(result[i][2])))


def Student_Department():
    tree.delete(*tree.get_children())

    sql1 = "select Student.Panther_ID, Student.Name, Student.DOB, Department.Name from Student, Department " \
           "where Student.Department_ID = Department.Department_ID "
    cursor.execute(sql1)
    result1 = cursor.fetchall()

    tree["columns"] = ("Student_Name", "Student_DOB", "Department_Name")
    tree.column("#0", width=100)
    tree.column("Student_Name", width=100)
    tree.column("Student_DOB", width=100)
    tree.column("Department_Name", width=100)

    tree.heading("#0", text="Panther ID")
    tree.heading("Student_Name", text="Name")
    tree.heading("Student_DOB", text="Birth year")
    tree.heading("Department_Name", text="Department name")

    for i in range(0, len(result1)):
        tree.insert("", i, text=str(result1[i][0]), values=(str(result1[i][1]), str(result1[i][2]), str(result1[i][3])))

#Making button 1
b1 = Button(bottomframe, text="Student-Department", command=Student_Department, background ='orange')
b1.grid(row=0, column=0)

#Defining the instructor info
def Instructor_Info():
    tree.delete(*tree.get_children())
    
    #excecuting the query
    sql2 = "select * from Instructor"
    cursor.execute(sql2)
    result2 = cursor.fetchall()

    tree["columns"] = ("Instructor_Name", "Department_ID")
    tree.column("#0", width=100)
    tree.column("Instructor_Name", width=100)
    tree.column("Department_ID", width=100)

    tree.heading("#0", text="Instructor ID")
    tree.heading("Instructor_Name", text="Name")
    tree.heading("Department_ID", text="Department ID")
    
    #inserting the tupple
    for i in range(0, len(result2)):
        tree.insert("", i, text=str(result2[i][0]), values=(str(result2[i][1]), str(result2[i][2])))

#making button 2
b2 = Button(bottomframe, text="Instructor_Info", command=Instructor_Info, background ='orange')
b2.grid(row=0, column=1)

#defining the student method
def Student_Info():
    tree.delete(*tree.get_children())
    
    #making the query
    sql = "select Student.Panther_ID, Student.Name, Student.DOB from Student"
    cursor.execute(sql)
    result = cursor.fetchall()

    tree["columns"] = ("Student_Name", "Student_DOB")
    tree.column("#0", width=100)
    tree.column("Student_Name", width=100)
    tree.column("Student_DOB", width=100)

    tree.heading("#0", text="Panther ID")
    tree.heading("Student_Name", text="Name")
    tree.heading("Student_DOB", text="Birth year")
    
    #adding the tuple
    for i in range(0, len(result)):
        tree.insert("", i, text=str(result[i][0]), values=(str(result[i][1]), str(result[i][2])))

#making the third button
b3 = Button(bottomframe, text="Student_Info", command=Student_Info, background ='orange')
b3.grid(row=0, column=2)

root.mainloop()
db.close()