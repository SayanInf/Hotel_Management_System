'''from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os


def pathget(img):
    global imgpathraw
    global image
    basedir = os.path.dirname(__file__)
    imgpath = basedir+f"\Images\{img}"
    imgpathraw=r'{0}'.format(imgpath)
    image=Image.open(imgpathraw)



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
        #img2=Image.open(r"P:\Hotel Management\Images\logo4.png")  #"E:\hotel management pics\hotel images\288592.png"
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





if __name__== "__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()'''

