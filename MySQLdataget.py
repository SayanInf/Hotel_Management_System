from tkinter import *
from tkinter import ttk





def getit():
    global mysqlhost
    global mysqluser
    global mysqlpassword
    global mysqldatabase

    mysqlhost=host=mysqlhost_Entry.get()
    mysqluser=user=mysqlusername_Entry.get()
    mysqlpassword=password=mysqlpassword_Entry.get()
    mysqldatabase=database=mysqldatabase_Entry.get()
        

        

    
    root.destroy()






root=Tk()
root = root
root.title("Hotel Management System")
root.geometry("500x550+450+90")
root["bg"] = "lightcyan1"






    #==================================Variables==============================

sqlhost=StringVar()
sqluser=StringVar()
sqlpass=StringVar()
sqldatabase=StringVar()

    #==============================Labels and Entries==========================
Welcome=Label(root, text="Welcome!", font=("times new roman", 20, "bold"), bg="lightcyan1", fg="black")
Welcome.place(x=200,y=20)


getready=Label(root, text="Initializing Your Database...", font=("times new roman", 15, "bold"), bg="lightcyan1", fg="black")
getready.place(x=140,y=470)


mysqlhost=Label(root, text="MySQL Host Name", font=("times new roman", 15, "bold"), bg="lightcyan1", fg="black")
mysqlhost.place(x=172,y=70)
mysqlhost_Entry=ttk.Entry(root, textvariable=sqlhost, font=("times new roman", 15, "bold"))
mysqlhost_Entry.insert(END,"localhost")
mysqlhost_Entry.place(x=135,y=100, width=250)

mysqlusername=Label(root, text="MySQL Username", font=("times new roman", 15, "bold"), bg="lightcyan1", fg="black")
mysqlusername.place(x=180,y=150)
mysqlusername_Entry=ttk.Entry(root, textvariable=sqluser, font=("times new roman", 15, "bold"))
mysqlusername_Entry.insert(END,"root")
mysqlusername_Entry.place(x=135,y=180, width=250)



        

mysqlpassword=Label(root, text="MySQL Password", font=("times new roman", 15, "bold"), bg="lightcyan1", fg="black")
mysqlpassword.place(x=180,y=230)
mysqlpassword_Entry=ttk.Entry(root, textvariable=sqlpass, font=("times new roman", 15, "bold"), show="*")
mysqlpassword_Entry.place(x=135,y=260, width=250)

def my_show():
    if(c_v1.get())==1:
        mysqlpassword_Entry.config(show="") #Password is visible
    else:
        mysqlpassword_Entry.config(show="*") #Password is hidden

c_v1=IntVar(value=0)
showpass=Checkbutton(root, text="Show Password",font=("times new roman",10,"bold"),bg="lightcyan1",fg="black",selectcolor="lightcyan1",variable=c_v1,onvalue=1,offvalue=0,command=my_show,highlightcolor="lightcyan1",activebackground="lightcyan1",activeforeground="black")
showpass.place(x=135,y=290)




mysqldatabase=Label(root, text="Database Name", font=("times new roman", 15, "bold"), bg="lightcyan1", fg="black")
mysqldatabase.place(x=190,y=330)
mysqldatabase_Entry=ttk.Entry(root, textvariable=sqldatabase, font=("times new roman", 15, "bold"))
mysqldatabase_Entry.insert(END,"hotel_management")
mysqldatabase_Entry.place(x=135,y=360, width=250)



btnAdd = Button(root, text = "Proceed", font=("arial", 12, "bold"), bg="dark blue", fg="white", width=9)
btnAdd.place(x=200,y=410, width=100)
btnAdd.configure(command=getit)
            
root.mainloop()





