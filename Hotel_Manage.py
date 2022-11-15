from tkinter import*
from PIL import Image, ImageTk  
from CustomerHM_2 import Cust_Win


class HotelmanagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1360x700+0+0")

    
        #========================================1st image=========================================
        img1=Image.open(r"P:\Hotel Management\images\img17.jpg")
        img1=img1.resize((1360,140))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=2,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1360,height=140)
    
    

        #========================================logo=========================================
        img2=Image.open(r"P:\Hotel Management\images\logo3.png")
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


        room_btn=Button(btn_frame,text="ROOM",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)


        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOG OUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)



        #======================================RIGHT SIDE IMAGE=============================================
        img3=Image.open(r"P:\Hotel Management\images\img2.jpg")
        img3=img3.resize((1132,510))
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=2,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1132,height=510)


        #============================================Down images============================================
        img4=Image.open(r"P:\Hotel Management\images\img25.jpg")
        img4=img4.resize((230,150))
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=225,height=145)


        img5=Image.open(r"P:\Hotel Management\images\img23.jpg")
        img5=img5.resize((230,150))
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=369,width=225,height=140)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)




if __name__== "__main__" :
    root = Tk()
    obj = HotelmanagementSystem(root)
    root.mainloop()
