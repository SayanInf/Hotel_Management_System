'''from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os



def pathget(img):
    global imgpathraw
    global image
    basedir = os.path.dirname(__file__)
    imgpath = basedir+f"\Images\{img}"
    imgpathraw=r'{0}'.format(imgpath)
    image=Image.open(imgpathraw)



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






        



if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()'''

