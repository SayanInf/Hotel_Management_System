from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+25+60")
        self.root["bg"] = "lightcyan1"


        #============================variables==================================
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_father_name = StringVar()
        self.var_gender_name = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()


        # ================================Title=================================
        lbl_title = Label(self.root,text="CUSTOMER DETAILS", font=("times new roman",20,"bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=70,y=0, width=1225,height=60)

        # ================================Logo==================================
        img2 = Image.open(r"P:\Hotel Management\images\logo3.png")
        img2= img2.resize((70,60))
        self.photoimg2= ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg.place(x=0, y=0, width=70, height=60)


        #===============================Label===================================
        labelframeleft  = LabelFrame(self.root, bd=2, relief = RIDGE, text="Customer Details", padx=2, font=("times new roman",15,"bold"), bg="lightcyan1")
        labelframeleft.place(x=5, y=60, width=425, height=480)


        #===============================Labels and Entry=========================
        
        #Customer Ref
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref:", font=("arial", 12, "bold"), padx=2, pady=6,bg="lightcyan1")
        lbl_cust_ref.grid(row=0, column=0)

        entry_ref = ttk.Entry(labelframeleft, width=28, textvariable=self.var_ref, font=("arial", 13, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1, sticky=W, padx=10)

        #Customer Name
        cname = Label(labelframeleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        cname.grid(row=1, column=0)

        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, width=28, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1, sticky=W,padx=10)

        #Fathter's Name
        cfname = Label(labelframeleft, text="Father's Name:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        cfname.grid(row=2, column=0)

        txtcfname = ttk.Entry(labelframeleft, textvariable=self.var_father_name, width=28, font=("arial", 13, "bold"))
        txtcfname.grid(row=2, column=1, sticky=W,padx=10)

        #Gender Combobox
        lbl_gender = Label(labelframeleft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lbl_gender.grid(row=3, column=0)

        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender_name, font=("arial", 12, "bold"), width=27, state='readonly')
        combo_gender["value"] = ("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        #Post Name
        lblPostCode = Label(labelframeleft, text="Post Code:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lblPostCode.grid(row=4, column=0)

        lblPostCode = ttk.Entry(labelframeleft, textvariable=self.var_post, width=28, font=("arial", 13, "bold"))
        lblPostCode.grid(row=4, column=1, sticky=W, padx=10)

        #Mobilenumber
        lblmobile = Label(labelframeleft, text="Mobile No:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lblmobile.grid(row=5, column=0)

        lblmobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=28, font=("arial", 13, "bold"))
        lblmobile.grid(row=5, column=1, sticky=W, padx=10)

        #Email
        lblemail = Label(labelframeleft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lblemail.grid(row=6, column=0)

        lblemail = ttk.Entry(labelframeleft, textvariable=self.var_email, width=28, font=("arial", 13, "bold"))
        lblemail.grid(row=6, column=1, sticky=W, padx=10)

        #Nationality Combobox
        lblnationality = Label(labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lblnationality.grid(row=7, column=0)

        nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("arial", 12, "bold"), width=27, state='readonly')
        nationality["value"] = ('Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 
        'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 
        'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 
        'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 
        'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 
        'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 
        'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 
        'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean')
        nationality.current(83)
        nationality.grid(row=7, column=1)
        

        #idproof Combobox
        lblnationality = Label(labelframeleft, text="ID Proof Type:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lblnationality.grid(row=8, column=0)

        idproof = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=27, state='readonly')
        idproof["value"] = ("Aadhaar Card", "Voter Card", "Driving Licence","Passport", "Other")
        idproof.current(3)
        idproof.grid(row=8, column=1)



        #idnumber 
        lblidnum = Label(labelframeleft, text="Id Number:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lblidnum.grid(row=9, column=0)

        lblidnum = ttk.Entry(labelframeleft, textvariable=self.var_id_number, width=28, font=("arial", 13, "bold"))
        lblidnum.grid(row=9, column=1, sticky=W, padx=10)


        #Address
        lbladdress = Label(labelframeleft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6, bg="lightcyan1")
        lbladdress.grid(row=10, column=0)

        lbladdress = ttk.Entry(labelframeleft, textvariable=self.var_address, width=28, font=("arial", 13, "bold"))
        lbladdress.grid(row=10, column=1, sticky=W, padx=10)

        #===============================Buttons==============================

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE, bg="lightcyan1")
        btn_frame.place(x=2,y=400, width=412,height=36)

        btnAdd = Button(btn_frame, text = "Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0,column=0, padx=1)

        btnUpdt = Button(btn_frame, text = "Update",command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdt.grid(row=0,column=1, padx=1)

        btnDlt = Button(btn_frame, text = "Delete", command=self.mDelete, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDlt.grid(row=0,column=2, padx=1)

        btnRst = Button(btn_frame, text = "Reset", command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnRst.grid(row=0,column=3, padx=1)

        #===============================Table Frame Search System===========================

        table_frame = LabelFrame(self.root, bd=2, relief = RIDGE, text="View Details and Search System", padx=2, font=("times new roman",15,"bold"), bg="lightcyan1")
        table_frame.place(x=435, y=60, width=855, height=480)

        lblsearch = Label(table_frame, text="Search By:", font=("arial", 13, "bold"), fg="black", bg="lightcyan1")
        lblsearch.grid(row=0, column=0)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=15, state='readonly')
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=5)

        self.txt_search = StringVar()
        textsearch = ttk.Entry(table_frame, textvariable=self.txt_search, width=43, font=("arial", 13, "bold"))
        textsearch.grid(row=0, column=2, sticky=W, padx=5)

        btnSearch = Button(table_frame, text = "Search", command=self.search, font=("arial", 12, "bold"), bg="steelblue1", fg="black", width=8)
        btnSearch.grid(row=0,column=3, padx=1)

        btnShowAll = Button(table_frame, text = "Show All", command=self.fetch_data, font=("arial", 12, "bold"), bg="steelblue1", fg="black", width=8)
        btnShowAll.grid(row=0,column=4)

        
        #=====================================Show Data Table============================

        details_table = Frame(table_frame, bd=2, relief=RIDGE, bg="aliceblue")
        details_table.place(x=0,y=50, width=845,height=400)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_details_table = ttk.Treeview(details_table, column=("ref", "name","father","gender","post","mobile",
                                                                    "email","nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.Cust_details_table.xview)
        scroll_y.config(command=self.Cust_details_table.yview)
        

        self.Cust_details_table.heading("ref", text="Ref. No.")
        self.Cust_details_table.heading("name", text="Name")
        self.Cust_details_table.heading("father", text="Father's Name")
        self.Cust_details_table.heading("gender", text="Gender")
        self.Cust_details_table.heading("post", text="Post Code")
        self.Cust_details_table.heading("mobile", text="Mobile")
        self.Cust_details_table.heading("email", text="Email")
        self.Cust_details_table.heading("nationality", text="Nationality")
        self.Cust_details_table.heading("idproof", text="ID Proof")
        self.Cust_details_table.heading("idnumber", text="ID. No.")
        self.Cust_details_table.heading("address", text="Address")

        self.Cust_details_table["show"] = "headings"

        self.Cust_details_table.column("ref", width=100)
        self.Cust_details_table.column("name", width=200)
        self.Cust_details_table.column("father", width=200)
        self.Cust_details_table.column("gender", width=100)
        self.Cust_details_table.column("post", width=200)
        self.Cust_details_table.column("mobile", width=250)
        self.Cust_details_table.column("email", width=300)
        self.Cust_details_table.column("nationality", width=100)
        self.Cust_details_table.column("idproof", width=200)
        self.Cust_details_table.column("idnumber", width=200)
        self.Cust_details_table.column("address", width=500)
        
        self.Cust_details_table.pack(fill=BOTH, expand=1)
        self.Cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()




        
        #===========================Functions==================================

    def add_data(self) :
        
        if ((self.var_cust_name.get()=="") or (self.var_father_name.get()=="") or (self.var_post.get()=="") or
        (self.var_mobile.get()=="") or (self.var_email.get()=="") or (self.var_id_number.get()=="") or (self.var_address.get()=="")) :
            
            messagebox.showerror("Error!","All Fields Are Required", parent = self.root)
        
        else :
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="@SayanMySQL05", database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                        self.var_ref.get(),
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_father_name.get(),
                                                                                        self.var_gender_name.get(),
                                                                                        self.var_post.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_id_proof.get(),
                                                                                        self.var_id_number.get(),
                                                                                        self.var_address.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer Has Been Added", parent = self.root)

            except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@SayanMySQL05", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0 :
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())

            for i in rows:
                self.Cust_details_table.insert("", END, values=i)
                conn.commit()
            conn.close()


    def get_cursor(self,event="") :
        cursor_row=self.Cust_details_table.focus()
        content=self.Cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_father_name.set(row[2]),
        self.var_gender_name.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])


    
    def update(self):
            
        if self.var_mobile.get()=="":
            messagebox.showerror("Error!", "Please Select A Record", parent=self.root)
        else :
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="@SayanMySQL05", database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("update customer set Name=%s, Father=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, IDProof=%s, IDNumber=%s, Address=%s where Ref=%s",(
                                                                                                                                
                                                                                                                                
                                                                                                                                self.var_cust_name.get(),
                                                                                                                                self.var_father_name.get(),
                                                                                                                                self.var_gender_name.get(),
                                                                                                                                self.var_post.get(),
                                                                                                                                self.var_mobile.get(),
                                                                                                                                self.var_email.get(),
                                                                                                                                self.var_nationality.get(),
                                                                                                                                self.var_id_proof.get(),
                                                                                                                                self.var_id_number.get(),
                                                                                                                                self.var_address.get(),
                                                                                                                                self.var_ref.get()

                                                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "Customer Details Has Been Updated Successfully", parent=self.root)
            
            except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)


    def mDelete(self):

        if self.var_mobile.get()=="":
            messagebox.showerror("Error!", "Please Select A Record", parent=self.root)
        
        else :
            try:
                mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?", parent=self.root)
                    
                if mDelete > 0 :
                    conn = mysql.connector.connect(host="localhost", username="root",password="@SayanMySQL05", database="hotel_management")
                    my_cursor = conn.cursor()
                    query ="delete from customer where Ref=%s"
                    value = (self.var_ref.get(),)
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
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_father_name.set(""),
        #self.var_gender_name.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x = random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@SayanMySQL05", database="hotel_management")
        my_cursor = conn.cursor()


        try:
            my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows) != 0 :
                self.Cust_details_table.delete(*self.Cust_details_table.get_children())
                for i in rows:
                    self.Cust_details_table.insert("",END, values=i)
                conn.commit()
            conn.close()
        
        except Exception as es :
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent = self.root)










if __name__=="__main__":
    root=Tk()
    obj = Cust_Win(root)
    root.mainloop()