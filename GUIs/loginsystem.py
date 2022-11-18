from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1360x700+0+0")
        
        img=Image.open(r"P:\Hotel Management\Images\img29.jpg")
        img=img.resize((1360,700))
        self.bg=ImageTk.PhotoImage(img)
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,width=1360,height=700)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=140,width=340,height=450)


        img1=Image.open(r"P:\Hotel Management\Images\user.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0,)
        lblimg1.place(x=620,y=145,width=100,height=100)


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=110)


        #===============================================label==============================================
        
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=162)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=195,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=231)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=265,width=270)


        #=======================================Icon images=======================================
        
        img2=Image.open(r"P:\Hotel Management\Images\user.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0,)
        lblimg2.place(x=540,y=302,width=25,height=25)


        img3=Image.open(r"P:\Hotel Management\Images\password4.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0,fg="black")
        lblimg3.place(x=540,y=372,width=25,height=25)
        
        
        #===================================login button=====================================
        
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="dark blue",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=320,width=120,height=35)

        #=================================register button=========================================
        registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=370,width=160,)

        #==============================forgot password button================================
        forgotpasswordbtn=Button(frame,text="Forgot password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpasswordbtn.place(x=8,y=390,width=160)



    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        
        elif self.txtuser.get()=="purab" and self.txtpass.get()=="over9000":
            messagebox.showinfo("Success","Welcome to Phantom Hotel")
        
        else:
            messagebox.showerror("Invalid","Invalid username & password")








if __name__== "__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()

