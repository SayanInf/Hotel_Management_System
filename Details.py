from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import os
import MySQLdataget




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






class Details_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Floor Details")
        self.root.geometry("1295x470+30+70")
        self.root["bg"] = "lightcyan1"






    # ================================Title=================================
        lbl_title = Label(self.root,text="Hotel Floors Details", font=("times new roman",20,"bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=70,y=0, width=1225,height=60)

    # ================================Logo==================================
        
        pathget("logo3.png")
        img2 = image
        img2= img2.resize((70,60))
        self.photoimg2= ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg.place(x=0, y=0, width=70, height=60)

    #===============================Label===================================
        labelframeleft  = LabelFrame(self.root, bd=2, relief = RIDGE, text="Floor Details", padx=2, font=("times new roman",15,"bold"), bg="lightcyan1")
        labelframeleft.place(x=5, y=60, width=545, height=400)


    #===============================Labels and Entry=========================
        
        #Floor
        lbl_hotel_floor = Label(labelframeleft, text="Floor:", font=("arial", 12, "bold"), padx=2, pady=6,bg="lightcyan1")
        lbl_hotel_floor.grid(row=0, column=0, sticky=W)

        self.var_floor=StringVar()
        floor = ttk.Entry(labelframeleft,textvariable=self.var_floor, width=20, font=("arial", 13, "bold"))
        floor.grid(row=0, column=1,sticky=W)

        #Room No.
        lbl_hotel_RoomNo = Label(labelframeleft, text="Room No:", font=("arial", 12, "bold"), padx=2, pady=6,bg="lightcyan1")
        lbl_hotel_RoomNo.grid(row=1, column=0, sticky=W)

        self.var_roomno=StringVar()
        RoomNo = ttk.Entry(labelframeleft, textvariable=self.var_roomno, width=20, font=("arial", 13, "bold"))
        RoomNo.grid(row=1, column=1,sticky=W)

        #Room Type.
        lbl_hotel_RoomType = Label(labelframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=6,bg="lightcyan1")
        lbl_hotel_RoomType.grid(row=2, column=0, sticky=W)

        self.var_roomtype=StringVar()
        RoomType = ttk.Entry(labelframeleft, textvariable=self.var_roomtype, width=20, font=("arial", 13, "bold"))
        RoomType.grid(row=2, column=1,sticky=W)


        #===============================Buttons==============================

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE, bg="lightcyan1")
        btn_frame.place(x=55,y=200, width=412,height=36)

        btnAdd = Button(btn_frame, text = "Add", command=self.add_data,  font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0,column=0, padx=1)

        btnUpdt = Button(btn_frame, text = "Update", command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdt.grid(row=0,column=1, padx=1) 

        btnDlt = Button(btn_frame, text = "Delete", command = self.mDelete, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDlt.grid(row=0,column=2, padx=1) 

        btnRst = Button(btn_frame, text = "Reset", command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnRst.grid(row=0,column=3, padx=1)




        #===============================Table Frame Search System===========================

        table_frame = LabelFrame(self.root, bd=2, relief = RIDGE, text="Show Floor Details", padx=2, font=("times new roman",15,"bold"), bg="lightcyan1")
        table_frame.place(x=600, y=60, width=680, height=400)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(table_frame, column=("floor","roomno","roomtype"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")


        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


        
    #=======================================Functions===============================

    #Add
    def add_data(self) :

        if ((self.var_floor.get()=="") or (self.var_roomtype.get()=="")) :
            
            messagebox.showerror("Error!","All Fields Are Required", parent = self.root)
        
        else :
            try:
                conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                    self.var_floor.get(),
                                                                                    self.var_roomno.get(),
                                                                                    self.var_roomtype.get()

                                                                                ))
                                                                                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Has Been Added", parent = self.root)

            except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)


    #Fetch
    def fetch_data(self):
        conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])


    #Update    
    def update(self):

        if self.var_floor.get()=="":
            messagebox.showerror("Error!", "Please Select A Record", parent=self.root)
        else :
            try:
                conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                my_cursor = conn.cursor()
                my_cursor.execute("update details set floor=%s, RoomType=%s where RoomNo=%s",(
                                                                                                                                    
                                                                                    self.var_floor.get(),
                                                                                    self.var_roomtype.get(), 
                                                                                    self.var_roomno.get()
                                                                                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "Room Details Has Been Updated Successfully", parent=self.root)
                
            except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)
                

    def mDelete(self):

        if self.var_floor.get()=="":
            messagebox.showerror("Error!", "Please Select A Record", parent=self.root)
        
        else :
            try:
                mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room ?", parent=self.root)
                    
                if mDelete > 0 :
                    conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                    my_cursor = conn.cursor()
                    query ="delete from details where RoomNo=%s"
                    value = (self.var_roomno.get(),)
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
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("")





   




    









if __name__=="__main__":
    root=Tk()
    obj = Details_Win(root)
    root.mainloop()