from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from CustomerWin import Cust_Win
from RoomWin import Room_Win
from ReportWin import Report
from Details import Details_Win
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


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


def pathget(img):
    global imgpathraw
    global image
    basedir = os.path.dirname(__file__)
    imgpath = basedir+f"\Images\{img}"
    imgpathraw=r'{0}'.format(imgpath)
    image=Image.open(imgpathraw)


    #________________________________________Login Window______________________________________

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1360x700+0+0")

        basedir = os.path.dirname(__file__)
        imgpath = basedir+"\Images\img29.jpg"
        imgpathraw=r'{0}'.format(imgpath)
        img=Image.open(imgpathraw)
        
        img=img.resize((1360,700))
        self.bg=ImageTk.PhotoImage(img)
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,width=1360,height=700)
        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=120,width=340,height=470)
        
        basedir = os.path.dirname(__file__)
        imgpath = basedir+"\Images\logo4.png"
        imgpathraw=r'{0}'.format(imgpath)
        img1=Image.open(imgpathraw)
        
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0,)
        lblimg1.place(x=620,y=125,width=100,height=100)


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=110)


        #===============================================label==============================================
        
        username=lbl=Label(frame,text="Username*",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=152)

        username1=lbl=Label(frame,text="*Registered Email",font=("times new roman",10,"bold"),fg="white",bg="black")
        username1.place(x=200,y=420)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=221)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)

       #========================================Show Password=====================================

        def my_show():
            if(c_v1.get())==1:
                self.txtpass.config(show="") #Password is visible
            else:
                self.txtpass.config(show="*") #Password is hidden

        c_v1=IntVar(value=0)
        showpass=Checkbutton(frame, text="Show Password",font=("times new roman",10,"bold"),bg="black",fg="white",selectcolor="black",variable=c_v1,onvalue=1,offvalue=0,command=my_show,highlightcolor="black",activebackground="black",activeforeground="white")
        showpass.place(x=40,y=285)



        #=======================================Icon images=======================================
        
        pathget("logo4.png")
        img2=Image.open(imgpathraw)    
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0,)
        lblimg2.place(x=540,y=272,width=25,height=25)

        pathget("password4.jpg")
        img3=image
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0,fg="black")
        lblimg3.place(x=540,y=342,width=25,height=25)
        
        
        #===================================login button=====================================
        
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="#d2e7ff",bg="#1c2f5c",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=330,width=120,height=35)

        #=================================register button=========================================
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=380,width=160,)

        #==============================forgot password button================================
        forgotpasswordbtn=Button(frame,text="Forgot password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpasswordbtn.place(x=8,y=400,width=160)



    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        

        





    #================================================Login Function=====================================

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        else:
            try:
                conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()
                                                                                            ))
                row = my_cursor.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Invalid Username and Password")
                else:
                    open_main=messagebox.askyesno("Warning!","Access only Admin")
                    if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=HotelmanagementSystem(self.new_window)
                    else:
                        if not open_main:
                            return
                conn.commit()
                conn.close()
                self.txtuser.delete(0,'end')
                self.txtpass.delete(0,'end')
            
            except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)


    #================================================Reset Password===================================================
    
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error!", "Please Select the Security Question",parent=self.root2)
        elif self.txt_Security_A.get()=="":
            messagebox.showerror("Error!", "Please Enter The Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error!", "Please Enter The New Password",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
                my_cursor=conn.cursor()
                query=("select * from register where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_Security_A.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error!", "Please Enter The Correct Answer",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get(),)
                    my_cursor.execute(query,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info", "Your Password Has Been Reset, Please Login With New Password",parent=self.root2)
                    self.root2.destroy()
            except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)




    #==============================================Forgot Password Window=============================================

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error!", "Please Enter The Username To Reset Password")
        else:
            conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error!", "Please Enter The Valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password?")
                self.root2.geometry("340x540+500+110")
                self.root2["bg"] = "black"
                

                l=Label(self.root2, text="Forgot Password?",font=("times new roman",15,"bold"),fg="red",bg="black")
                l.place(x=0,y=20,relwidth=1)

                Security_Q=Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="black", fg="red")
                Security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"]=("Select", "Your Birth Place", "Your Goal", "Your Pet Name")
                self.combo_security_Q.place(x=49, y=110)
                self.combo_security_Q.current(0)



                
                Security_A=Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="black", fg="red")
                Security_A.place(x=50,y=150)

                self.txt_Security_A=ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_Security_A.place(x=50,y=180, width=250)

                new_password=Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="black", fg="red")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50,y=250, width=250)


                btn=Button(self.root2,text="Reset", command=self.reset_pass, font=("times new roman", 15, "bold"), fg= "red", bg="black" )
                btn.place(x=140,y=290)















    #_________________________________________Registration Window_________________________________________

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1360x700+0+0")



        #===================================varriables===============================================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #========================================Background Image=======================================
        
        pathget("img29.jpg")
        img1=image
        img1=img1.resize((1360,700))
        self.bg=ImageTk.PhotoImage(img1)

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0,y=0, width=1360, height=700)



        #======================================Left Image=======================================
        
        pathget("img27.jpg")
        img2=image
        img2=img2.resize((470,550))
        self.left=ImageTk.PhotoImage(img2)

        left_lbl = Label(self.root, image=self.left)
        left_lbl.place(x=50, y=100, width=470, height=550)

        #========================================Main Frame====================================
        frame=Frame(self.root, bg="white")
        frame.pack()
        frame.place(x=520, y=100, width=790, height=550)

        pathget("img26.jpeg")
        img3=image
        img3=img3.resize((790,550))
        self.img3=ImageTk.PhotoImage(img3)
        frameimg_lbl=Label(frame, image=self.img3)
        frameimg_lbl.place(x=0, y=0, width=790, height=550)

        register_lbl=Label(frame,text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="dark blue")
        register_lbl.place(x=20, y=20)

        #======================================Labels and Entry Fills===========================

        #----------------row1---------------

        fname=Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="dark blue")
        fname.place(x=50,y=100)

        fname_Entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman", 15, "bold"))
        fname_Entry.place(x=49,y=130, width=250)

        lname=Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="dark blue")
        lname.place(x=400,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=399,y=130, width=250)

        #--------------row2-----------------

        contact=Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white", fg="dark blue")
        contact.place(x=50,y=200)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=49,y=230, width=250)

        email=Label(frame, text="Username/Email", font=("times new roman", 15, "bold"), bg="white", fg="dark blue")
        email.place(x=400,y=200)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=399,y=230, width=250)


        #--------------row3-----------------

        Security_Q=Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="dark blue")
        Security_Q.place(x=50,y=300)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"]=("Select", "Your Birth Place", "Your Goal", "Your Pet Name")
        self.combo_security_Q.place(x=49, y=330)
        self.combo_security_Q.current(0)



        
        Security_A=Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="dark blue")
        Security_A.place(x=400,y=300)

        self.txt_Security_A=ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_Security_A.place(x=399,y=330, width=250)


        #--------------row4-----------------

        password=Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="dark blue")
        password.place(x=50,y=400)

        self.txt_password=ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_password.place(x=49,y=430, width=250)

        conf_password=Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="dark blue")
        conf_password.place(x=400,y=400)

        self.txt_conf_password=ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_conf_password.place(x=399,y=430, width=250)

        
        
        
        #================================CheckButton========================
        
        self.var_cheak=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_cheak, text="I Agree To The Terms & Conditions", font=("times new roman", 12, "bold"), bg="white", fg="dark blue", onvalue=1, offvalue=0, command=self.terms)
        checkbtn.place(x=50, y=480)


        #===============================Button===========================

        pathget("Regbtn1.png")
        registerbtnimg=image
        registerbtnimg=registerbtnimg.resize((300,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(registerbtnimg)
        btn1=Button(frame, image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2", bg="light blue", fg="light blue")
        btn1.place(x=400, y=480, width=300)

        or_lbl=Label(frame, text="Already Have An Account?", font=("times new roman", 12, "bold"), bg="white", fg="dark blue")
        or_lbl.place(x=450,y=25)

        pathget("login.png")
        loginbtnimg=image         
        loginbtnimg=loginbtnimg.resize((100,30),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(loginbtnimg)
        btn1=Button(frame, image=self.photoimage1,command=self.login_window,borderwidth=0,cursor="hand2", bg="light blue", fg="light blue")
        btn1.place(x=650, y=20, width=100)


    #=============================================Register Function=======================================================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error!","Password And Confirm Password Must Be Same")
        elif self.var_cheak.get()==0:
            messagebox.showerror("Error!","Please Agree To The Terms and Conditions.", parent=self.root)
            messagebox.showinfo("Terms And Conditions", "Please visit site https://thehotelmanagement.co/terms-conditions/",parent=self.root)
        else:
            conn=mysql.connector.connect(host=f"{host}",user=f"{user}",password=f"{password}",database=f"{database}")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error!","User Already Exists. Please Try Another Email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                     ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered Successfully",parent=self.root)
            self.root.destroy()

    
    
    def login_window(self):
        self.root.destroy()

    def terms(self):
        self.open=open("Terms&Conditions.txt")
        self.read=StringVar()
        self.read=self.open.read()

        self.root3=Toplevel()
        self.root3.title("Terms and Conditions")
        self.root3.geometry("640x540+500+110")

        TextArea = Text(self.root3, font = "calibri 12")
        TextArea.pack(fill = "both", expand=True)
        TextArea.insert(1.0, self.read)
        TextArea.config(state=DISABLED)
        
        scroll_x = ttk.Scrollbar(TextArea, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(TextArea, orient=VERTICAL)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.TextArea.xview)
        scroll_y.config(command=self.TextArea.yview)







    #_________________________________________Hotel Management Window____________________________________

class HotelmanagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1360x700+0+0")

    
        #========================================1st image=========================================
        
        pathget("img17.jpg")
        img1=image
        img1=img1.resize((1360,140))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=2,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1360,height=140)
    
    

        #========================================logo=========================================
        
        pathget("logo3.png")
        img2=image
        img2=img2.resize((230,140))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=2, relief = RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
        
        #==========================================title=============================================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM", font=("times new roman",40,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1359,height=50)


        #========================================main frame===========================================
        main_frame=Frame(self.root,bd=2,bg="blue",relief=RIDGE)
        main_frame.place(x=0,y=190,width=1360,height=510)


        #===========================================menu===============================================
        lbl_menu=Label(main_frame,text="MENU", font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)


        #=========================================button frame===========================================
        btn_frame=Frame(main_frame,bd=2,bg="blue",relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=190)



        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details, width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)


        room_btn=Button(btn_frame,text="ROOMS",width=22, command=self.room_details, font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS", command= self.floor_details, width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)


        report_btn=Button(btn_frame,text="REPORT", command=self.report,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOG OUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)



        #======================================RIGHT SIDE IMAGE=============================================
        
        pathget("img2.jpg")
        img3=image
        img3=img3.resize((1132,510))
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=2,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1132,height=510)


        #============================================Down images============================================
        
        pathget("img25.jpg")
        img4=image
        img4=img4.resize((230,150))
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=225,height=145)


        pathget("img23.jpg")
        img5=image
        img5=img5.resize((230,150))
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=369,width=225,height=140)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)


    def report(self):
        self.new_window = Toplevel(self.root)
        self.app = Report(self.new_window)

    def logout(self):
        self.root.destroy()

    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_Win(self.new_window)

    def floor_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Details_Win(self.new_window)







if __name__== "__main__":
    main()