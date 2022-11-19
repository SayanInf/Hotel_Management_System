from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import os
import MySQLdataget
from time import strftime
from datetime import datetime
import Price


host=MySQLdataget.mysqlhost
user=MySQLdataget.mysqluser
password=MySQLdataget.mysqlpassword
database=MySQLdataget.mysqldatabase

try:
    conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
except:
    messagebox.showerror("Error!", "Looks Like You Provided Wrong Inputs...Try Again With Correct Inputs. Or, The 'hotel_management' Database Schema Might Not Exist In The Provided Host, Follow The Standard Procdure To Add The 'hotel_management\' Schema In The Given Host Of Your MySQL Database. For Standard Procedures of Installation To Add The Schema, Visit \"https://github.com/SayanInf/Hotel_Management_System#installation\"")
    quit()





def pathget(img):
    global imgpathraw
    global image
    basedir = os.path.dirname(__file__)
    imgpath = basedir+f"\Images\{img}"
    imgpathraw=r'{0}'.format(imgpath)
    image=Image.open(imgpathraw)



class Room_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Room Details")
        self.root.geometry("1295x550+30+70")
        self.root["bg"] = "lightcyan1"



    #==============================Variables===============================

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_subtotal=StringVar()
        self.var_total=StringVar()


    # ================================Title=================================
        lbl_title = Label(self.root,text="ROOMBOOKING DETAILS", font=("times new roman",20,"bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=70,y=0, width=1225,height=60)

    # ================================Logo==================================
        
        pathget("logo3.png")
        img2 = image
        img2= img2.resize((70,60))
        self.photoimg2= ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg.place(x=0, y=0, width=70, height=60)

    #===============================Label===================================
        self.labelframeleft  = LabelFrame(self.root, bd=2, relief = RIDGE, text="Roombooking Details", padx=2, font=("times new roman",15,"bold"), bg="lightcyan1")
        self.labelframeleft.place(x=5, y=60, width=425, height=480)


    #===============================Labels and Entry=========================
        
        #Customer Contact
        lbl_cust_contact = Label(self.labelframeleft, text="Customer Contact:", font=("arial", 12, "bold"), padx=2, pady=6,bg="lightcyan1")
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        contact = ttk.Entry(self.labelframeleft, width=20, textvariable=self.var_contact, font=("arial", 13, "bold"))
        contact.grid(row=0, column=1,sticky=W)

        #Fetch Data Button
        btnfetchdata = Button(self.labelframeleft, text = "Fetch Data",command=self.Fetch_contact, font=("arial", 8, "bold"), bg="black", fg="gold", width=9)
        btnfetchdata.place(x=345,y=4, width=65)


        #Checkin Date
        check_in_date = Label(self.labelframeleft, text="Check In Date:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        check_in_date.grid(row=1, column=0, sticky=W)
        contact = ttk.Entry(self.labelframeleft, width=28,textvariable=self.var_checkin , font=("arial", 13, "bold"))
        contact.grid(row=1, column=1)

        #Checkout Date
        check_out_date = Label(self.labelframeleft, text="Check Out Date:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        check_out_date.grid(row=2, column=0, sticky=W)
        txt_check_out = ttk.Entry(self.labelframeleft,textvariable=self.var_checkout, width=28, font=("arial", 13, "bold"))
        txt_check_out.grid(row=2, column=1)

        #Room Type
        lbl_RoomType = Label(self.labelframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lbl_RoomType.grid(row=3, column=0, sticky=W)


        combo_RoomType = ttk.Combobox(self.labelframeleft, textvariable=self.var_roomtype,font=("arial", 12, "bold"), width=18, state='readonly')
        combo_RoomType["value"] = ("Select","Single","Double","Triple") #"Quad","Queen","King","Twin","Hollywood Twin Room","Double-double","Studio","Suite / Executive Suite","Mini Suite or Junior Suite","President Suite | Presidential Suite","Apartments / Room for Extended Stay","Connecting rooms","Murphy Room", "Villa","Cabana")
        combo_RoomType.current(1)
        combo_RoomType.grid(row=3, column=1, sticky=W)

        btncombobox = Button(self.labelframeleft, text = "Select", font=("arial", 8, "bold"), bg="black", fg="gold", width=9, command=self.RoomTypeSelection)
        btncombobox.place(x=345,y=110, width=65)

        

        #Available Rooms
        lbl_Room_Available = Label(self.labelframeleft, text="Available Rooms:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lbl_Room_Available.grid(row=4, column=0, sticky=W)
        
        combo_roomno = ttk.Combobox(self.labelframeleft, textvariable=self.var_roomavailable, font=("arial", 12, "bold"), width=26, state='readonly')
        combo_roomno["value"] = ("SelectRoomTypeFirst")
        combo_roomno.grid(row=4, column=1, sticky=W)
        
        


        #Meal
        lbl_meal = Label(self.labelframeleft, text="Meal Opted:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lbl_meal.grid(row=5, column=0, sticky=W)

        combo_Meal = ttk.Combobox(self.labelframeleft, textvariable=self.var_meal,font=("arial", 12, "bold"), width=26, state='readonly')
        combo_Meal["value"] = ("Breakfast","Lunch","Dinner")
        combo_Meal.current(1)
        combo_Meal.grid(row=5, column=1, sticky=W)

        #No. of Days of Stay
        lbl_No_Stay = Label(self.labelframeleft, text="No. Of Days:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lbl_No_Stay.grid(row=6, column=0, sticky=W)
        txt_No_Stay = ttk.Entry(self.labelframeleft, textvariable=self.var_noofdays, width=28, font=("arial", 13, "bold"))
        txt_No_Stay.grid(row=6, column=1)

        #Payable Tax
        lbl_tax_payable = Label(self.labelframeleft, text="Payable Tax:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lbl_tax_payable.grid(row=7, column=0, sticky=W)
        txt_tax_payable = ttk.Entry(self.labelframeleft, textvariable=self.var_paidtax, width=28, font=("arial", 13, "bold"))
        txt_tax_payable.grid(row=7, column=1)

        #Sub Total
        lbl_Sub_total = Label(self.labelframeleft, text="Sub Total:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lbl_Sub_total.grid(row=8, column=0, sticky=W)
        txt_Sub_total = ttk.Entry(self.labelframeleft, width=28,textvariable=self.var_subtotal, font=("arial", 13, "bold"))
        txt_Sub_total.grid(row=8, column=1)

        #Total Cost
        lbl_Total_Bill = Label(self.labelframeleft, text="Total Bill:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lbl_Total_Bill.grid(row=9, column=0, sticky=W)
        txt_Total_Bill = ttk.Entry(self.labelframeleft, textvariable=self.var_total, width=28, font=("arial", 13, "bold"))
        txt_Total_Bill.grid(row=9, column=1)


        #Bill Button
        btnAdd = Button(self.labelframeleft, text = "Bill", command=self.total, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=10,column=1)

        #===============================Buttons==============================

        btn_frame = Frame(self.labelframeleft, bd=2, relief=RIDGE, bg="lightcyan1")
        btn_frame.place(x=2,y=400, width=412,height=36)

        btnAdd = Button(btn_frame, text = "Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0,column=0, padx=1)

        btnUpdt = Button(btn_frame, text = "Update",command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdt.grid(row=0,column=1, padx=1) #

        btnDlt = Button(btn_frame, text = "Delete",command=self.mDelete, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDlt.grid(row=0,column=2, padx=1) #

        btnRst = Button(btn_frame, text = "Reset",command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnRst.grid(row=0,column=3, padx=1)

        #=======================================Room Picture===================
        pathget("img22.jpg")
        img3 = image
        img3= img3.resize((350,220))
        self.photoimg3= ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3, bd=0, relief=RIDGE, bg="lightcyan1")
        lblimg.place(x=930, y=65, width=350, height=220)



        #===============================Table Frame Search System===========================

        table_frame = LabelFrame(self.root, bd=2, relief = RIDGE, text="View Details and Search System", padx=2, font=("times new roman",15,"bold"), bg="lightcyan1")
        table_frame.place(x=435, y=280, width=855, height=260)

        lblsearch = Label(table_frame, text="Search By:", font=("arial", 13, "bold"), fg="black", bg="lightcyan1")
        lblsearch.grid(row=0, column=0)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=15, state='readonly')
        combo_search["value"] = ("contact", "roomtype")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=5)

        self.txt_search = StringVar()
        textsearch = ttk.Entry(table_frame, textvariable=self.txt_search, width=43, font=("arial", 13, "bold"))
        textsearch.grid(row=0, column=2, sticky=W, padx=5)

        btnSearch = Button(table_frame, text = "Search", command=self.search, font=("arial", 12, "bold"), bg="steelblue1", fg="black", width=8)
        btnSearch.grid(row=0,column=3, padx=1)

        btnShowAll = Button(table_frame, text = "Show All", command=self.fetch_data, font=("arial", 12, "bold"), bg="steelblue1", fg="black", width=8)
        btnShowAll.grid(row=0,column=4)

        self.showDataframe=LabelFrame(self.root, text="Customer Details",  font=("times new roman",15,"bold"), bd=2,relief=RIDGE, padx=2, bg="lightcyan1")
        self.showDataframe.place(x=440,y=70,width=460,height=210)

        


        #=====================================Show Data Table============================

        details_table = Frame(table_frame, bd=2, relief=RIDGE, bg="aliceblue")
        details_table.place(x=0,y=50, width=845,height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=("contact", "checkin","checkout","roomtype","roomavailable",
                                                                    "meal","noOfdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Chekck In")
        self.room_table.heading("checkout", text="Check Out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room Available")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="No Of Days")


        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=200)
        self.room_table.column("checkin", width=150)
        self.room_table.column("checkout", width=150)
        self.room_table.column("roomtype", width=150)
        self.room_table.column("roomavailable", width=250)
        self.room_table.column("meal", width=150)
        self.room_table.column("noOfdays", width=150)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

 
 
    #========================================All Data Fetch====================================
 
    def Fetch_contact(self):
            if self.var_contact.get()=="":
                messagebox.showerror("Error!", "Please Enter Contact No.", parent=self.root)
            else:
                conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                my_cursor = conn.cursor()
                query=("select Name from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                if row==None:
                    messagebox.showerror("Error!", "This Contact is not found",parent=self.root)
                else:
                    conn.commit()
                    conn.close()

                    
                    #Name
                    lblname=Label(self.showDataframe,text="Name:", font=("arial",12,"bold"), bg="lightcyan1")
                    lblname.place(x=0,y=0) 

                    lbl=Label(self.showDataframe,text=row, font=("arial",12,"bold"), bg="lightcyan1")
                    lbl.place(x=90,y=0)



                    #Gender
                    conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                    my_cursor = conn.cursor()
                    query=("select Gender from customer where Mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()

                    lblGender=Label(self.showDataframe,text="Gender:", font=("arial",12,"bold"), bg="lightcyan1")
                    lblGender.place(x=0,y=30) 

                    lbl2=Label(self.showDataframe,text=row, font=("arial",12,"bold"), bg="lightcyan1")
                    lbl2.place(x=90,y=30)

                    #Email
                    conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                    my_cursor = conn.cursor()
                    query=("select Email from customer where Mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()

                    lblGender=Label(self.showDataframe,text="Email:", font=("arial",12,"bold"), bg="lightcyan1")
                    lblGender.place(x=0,y=60) 

                    lbl2=Label(self.showDataframe,text=row, font=("arial",12,"bold"), bg="lightcyan1")
                    lbl2.place(x=90,y=60)

                    #Nationality
                    conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                    my_cursor = conn.cursor()
                    query=("select Nationality from customer where Mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()

                    lblGender=Label(self.showDataframe,text="Nationality:", font=("arial",12,"bold"), bg="lightcyan1")
                    lblGender.place(x=0,y=90) 

                    lbl2=Label(self.showDataframe,text=row, font=("arial",12,"bold"), bg="lightcyan1")
                    lbl2.place(x=90,y=90)

                    #Address
                    conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                    my_cursor = conn.cursor()
                    query=("select Address from customer where Mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()

                    lblGender=Label(self.showDataframe,text="Address:", font=("arial",12,"bold"), bg="lightcyan1")
                    lblGender.place(x=0,y=120) 

                    lbl2=Label(self.showDataframe,text=row, font=("arial",12,"bold"), bg="lightcyan1")
                    lbl2.place(x=90,y=120)

                    #Postcode
                    conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                    my_cursor = conn.cursor()
                    query=("select Postcode from customer where Mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()

                    lblGender=Label(self.showDataframe,text="Postcode:", font=("arial",12,"bold"), bg="lightcyan1")
                    lblGender.place(x=0,y=150) 

                    lbl2=Label(self.showDataframe,text=row, font=("arial",12,"bold"), bg="lightcyan1")
                    lbl2.place(x=90,y=150)


        #=======================================Functions======================================

    #Add
    def add_data(self) :

        if ((self.var_contact.get()=="") or (self.var_checkin.get()=="") or (self.var_checkout.get()=="")or(self.var_roomtype=="") or (self.var_meal.get()=="")) :
            
            messagebox.showerror("Error!","All Fields Are Required", parent = self.root)
        
        else :
            try:
                conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_contact.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailable.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get()

                                                                                ))
                                                                                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Is Successfully Booked", parent = self.root)

            except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)


    #Fetch
    def fetch_data(self):
        conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0 :
            self.room_table.delete(*self.room_table.get_children())

            for i in rows:
                self.room_table.insert("", END, values=i)
                conn.commit()
            conn.close()




    #Get Cursor
    def get_cursor(self,event="") :
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
        self.var_paidtax.set(row[7])
        self.var_subtotal.set(row[8])
        self.var_total.set(row[9])




    #Update    
    def update(self):

        if self.var_contact.get()=="":
            messagebox.showerror("Error!", "Please Select A Record", parent=self.root)
        else :
            try:
                conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                my_cursor = conn.cursor()
                my_cursor.execute("update room set checkin=%s, checkout=%s, roomtype=%s, roomavailable=%s, meal=%s, noOfdays=%s where contact=%s",(
                                                                                                                                    
                                                                                                                                    self.var_checkin.get(),
                                                                                                                                    self.var_checkout.get(),
                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                    self.var_roomavailable.get(),
                                                                                                                                    self.var_meal.get(),
                                                                                                                                    self.var_noofdays.get(),
                                                                                                                                    self.var_contact.get()
                                                                                                                                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "Details Have Been Updated Successfully", parent=self.root)
                
            except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)



    def mDelete(self):

        if self.var_contact.get()=="":
            messagebox.showerror("Error!", "Please Select A Record", parent=self.root)
        
        else :
            try:
                mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Record?", parent=self.root)
                    
                if mDelete > 0 :
                    conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                    my_cursor = conn.cursor()
                    query ="delete from room where contact=%s"
                    value = (self.var_contact.get(),)
                    my_cursor.execute(query,value)
                else:
                    if not mDelete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)


    def reset(self):
        self.var_contact.set(""), 
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_total.set("")


 #===================================Billing Calculation===========================
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        
        indate=datetime.strptime(inDate,"%d/%m/%Y")
        outdate=datetime.strptime(outDate,"%d/%m/%Y")

        self.var_noofdays.set(abs(outdate-indate).days)

        days=float(self.var_noofdays.get())
        print("days",days)

        
        if self.var_roomtype.get()=="Single":
            lps=Price.singleroom
            print("lps",lps)
        elif self.var_roomtype.get()=="Double":
            lps=Price.doubleroom
            print("lps",lps)
        elif self.var_roomtype.get()=="Triple":
            lps=Price.tripleroom
            print("lps",lps)
        else:
            messagebox.showerror("Error!", "No Room is selected")

        if self.var_meal.get()=="Breakfast":
            fps=Price.breakfast
            print("fps",fps)
        elif self.var_meal.get()=="Lunch":
            fps=Price.lunch
            print("lps",lps)
        elif self.var_meal.get()=="Dinner":
            fps=Price.dinner
            print("lps",lps)
        else:
            messagebox.showerror("Error!", "No Meal is selected")
        
        
        paidtax=((lps)*(Price.taxroom)+(fps)*(Price.taxfood)+((fps)+(lps))*(Price.taxsupport))*(days)
        subtotal=((fps)+(lps))*(days)
        total=(paidtax)+(subtotal)
        print("paidtax",paidtax)
        print("subtotal",subtotal)
        print("total",total)   

        tax="Rs. "+str("%.2f"%(paidtax))
        Subtotal="Rs. "+str("%.2f"%(subtotal))
        Total="Rs. "+str("%.2f"%(total))
        self.var_paidtax.set(tax)
        self.var_subtotal.set(Subtotal)
        self.var_total.set(Total)


    def search(self):
        conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
        my_cursor = conn.cursor()
        
        try:
            my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows) != 0 :
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("",END, values=i)
                conn.commit()
            conn.close()
        except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)






    #===================================RoomTypeSelection Function==================================
    
    def RoomTypeSelection(self):
        global rows
        
        try:
            conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
            my_cursor = conn.cursor()
            query=("select RoomNo from details where RoomType=%s and RoomNo NOT IN (select roomavailable from room)")
            value=(self.var_roomtype.get(),)
            my_cursor.execute(query,value)
            rows=my_cursor.fetchall()
        
        except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)

        combo_roomno = ttk.Combobox(self.labelframeleft, textvariable=self.var_roomavailable, font=("arial", 12, "bold"), width=26, state='readonly')
        combo_roomno["value"] = rows
        combo_roomno.grid(row=4, column=1, sticky=W)


        if self.var_roomtype.get()=="Single":
            pathget("room1.jpg")
            img3 = image
            img3= img3.resize((350,220))
            self.photoimg3= ImageTk.PhotoImage(img3)
            lblimg=Label(self.root,image=self.photoimg3, bd=0, relief=RIDGE, bg="lightcyan1")
            lblimg.place(x=930, y=65, width=350, height=220)

        if self.var_roomtype.get()=="Double":
            pathget("room2.jpg")
            img3 = image
            img3= img3.resize((350,220))
            self.photoimg3= ImageTk.PhotoImage(img3)
            lblimg=Label(self.root,image=self.photoimg3, bd=0, relief=RIDGE, bg="lightcyan1")
            lblimg.place(x=930, y=65, width=350, height=220)

        if self.var_roomtype.get()=="Triple":
            pathget("room3.jpg")
            img3 = image
            img3= img3.resize((350,220))
            self.photoimg3= ImageTk.PhotoImage(img3)
            lblimg=Label(self.root,image=self.photoimg3, bd=0, relief=RIDGE, bg="lightcyan1")
            lblimg.place(x=930, y=65, width=350, height=220)

        if self.var_roomtype.get()=="Select":
            pathget("img22.jpg")
            img3 = image
            img3= img3.resize((350,220))
            self.photoimg3= ImageTk.PhotoImage(img3)
            lblimg=Label(self.root,image=self.photoimg3, bd=0, relief=RIDGE, bg="lightcyan1")
            lblimg.place(x=930, y=65, width=350, height=220)
        

        










if __name__=="__main__":
    root=Tk()
    obj = Room_Win(root)
    root.mainloop()