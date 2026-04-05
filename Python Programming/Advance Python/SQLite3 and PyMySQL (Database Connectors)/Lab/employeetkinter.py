from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_cone():
    return mysql.connector.connect(
        database="python_db",
        user="root",
        password="",
        host="localhost"
    )

def insert_data():
    if e_name.get()=="" or e_designation.get()=="" or e_salary.get()=="" or e_city.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        cone=create_cone()
        cursor=cone.cursor()
        query="insert into employee(name,designation,salary,city) values(%s,%s,%s,%s)"
        args=(e_name.get(),e_designation.get(),e_salary.get(),e_city.get())
        cursor.execute(query,args)
        cone.commit()
        cone.close()

        e_name.delete(0,'end')
        e_designation.delete(0,'end')
        e_salary.delete(0,'end')
        e_city.delete(0,'end')

        msg.showinfo("Insert Status","Data Inserted Successfully")

def search_data():
    e_name.delete(0,'end')
    e_designation.delete(0,'end')
    e_salary.delete(0,'end')
    e_city.delete(0,'end')

    if e_id.get()=="":
        msg.showinfo("Search Status","ID is Mandatory")
    else:
        cone=create_cone()
        cursor=cone.cursor()
        query="select * from employee where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()

        if row:
            e_name.insert(0,row[0][1])
            e_designation.insert(0,row[0][2])
            e_salary.insert(0,row[0][3])
            e_city.insert(0,row[0][4])
        else:
            msg.showinfo("Search","ID not found")

        cone.close()

def update_data():
    cone=create_cone()
    cursor=cone.cursor()
    query="update employee set name=%s,designation=%s,salary=%s,city=%s where id=%s"
    args=(e_name.get(),e_designation.get(),e_salary.get(),e_city.get(),e_id.get())
    cursor.execute(query,args)
    cone.commit()
    cone.close()

    msg.showinfo("Update","Data Updated Successfully")

def delete_data():
    cone=create_cone()
    cursor=cone.cursor()
    query="delete from employee where id=%s"
    args=(e_id.get(),)
    cursor.execute(query,args)
    cone.commit()
    cone.close()

    msg.showinfo("Delete","Data Deleted Successfully")

root=Tk()
root.geometry("500x500")
root.title("Employee Form")

Label(root,text="ID").place(x=50,y=50)
Label(root,text="NAME").place(x=50,y=100)
Label(root,text="DESIGNATION").place(x=50,y=150)
Label(root,text="SALARY").place(x=50,y=200)
Label(root,text="CITY").place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=200,y=50)

e_name=Entry(root)
e_name.place(x=200,y=100)

e_designation=Entry(root)
e_designation.place(x=200,y=150)

e_salary=Entry(root)
e_salary.place(x=200,y=200)

e_city=Entry(root)
e_city.place(x=200,y=250)

Button(root,text="INSERT",command=insert_data).place(x=50,y=300)
Button(root,text="SEARCH",command=search_data).place(x=120,y=300)
Button(root,text="UPDATE",command=update_data).place(x=195,y=300)
Button(root,text="DELETE",command=delete_data).place(x=270,y=300)

root.mainloop()