from tkinter import*


class Report:
    def __init__(self,root):
        self.root = root
        self.root.title("Report Window")
        self.root.geometry("960x520+200+100")
        self.root["bg"] = "lightcyan1"

        #=================================Labels===================================
        
        lbl=Label(self.root,text="Found A Bug?", font=("times new roman",20,"bold"), bg= "lightcyan1", fg="dark blue")
        lbl.place(x=5,y=5)

        lbltext=Label(self.root,text="- Send an Email to the developers describing your issue...", font=("times new roman",15,"bold"), bg="lightcyan1", fg="black")
        lbltext.place(x=20,y=70)

        email1=Label(self.root,text="- Developer Name: Sayan Ghosh, Email - sayanghosh1427@gmail.com", font=("times new roman",15,"bold"), bg= "lightcyan1", fg="green")
        email1.place(x=20,y=150)

        email2=Label(self.root,text="- Developer Name: Purab Jana, Email - purabjana@gmail.com", font=("times new roman",15,"bold"), bg= "lightcyan1", fg="green")
        email2.place(x=20,y=200)

        email3=Label(self.root,text="- Developer Name: Samriddha Karmakar, Email - samriddhakarmakar56@gmail.com", font=("times new roman",15,"bold"), bg= "lightcyan1", fg="green")
        email3.place(x=20,y=250)

        feedback=Label(self.root,text="- If you liked our Hotel Management System Project, do not forget to send a feedback...", font=("times new roman",15,"bold"), bg= "lightcyan1", fg="violet")
        feedback.place(x=20,y=350)

        theend=Label(self.root,text="Feel free to reach us out anytime...", font=("times new roman",15,"bold"), bg= "lightcyan1", fg="orange")
        theend.place(x=320,y=400)

        theend=Label(self.root,text="(c) MIT Opensource Licensed Software", font=("times new roman",15,"bold"), bg= "lightcyan1", fg="black")
        theend.place(x=305,y=450)

if __name__== "__main__" :
    root = Tk()
    obj = Report(root)
    root.mainloop()

     #=============================================The End========================================'''