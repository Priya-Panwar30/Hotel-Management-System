from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector 
from tkinter import messagebox
class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("hotel management system")
        self.root.geometry("1295x550+230+220")

        #variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_fathername=StringVar()
        self.var_gender=StringVar()
        self.var_postcode=StringVar()
        self.var_Mobile=StringVar()
        self.var_EmailID=StringVar()
        self.var_Nationality=StringVar()
        self.var_IDproof=StringVar()
        self.var_IDnumber=StringVar()
        self.var_address=StringVar()
        


        #title
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("algerian",18),bg="white",fg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #logo
        img2=Image.open(r"C:\Users\FMT\OneDrive\Desktop\images\1690518105333.jpeg") 
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        #label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("algerian",12),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #labels and entry
        #custRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_ref,font=("arial",13),state="readonly")
        enty_ref.grid(row=0,column=1)

        #cust name
        cname=Label(labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13))
        txtcname.grid(row=1,column=1)

        #mother name
        lblmname=Label(labelframeleft,text="Father Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_fathername,width=29,font=("arial",13))
        txtmname.grid(row=2,column=1)

        #gender combobox
        label_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #postcode
        lblPostCode=Label(labelframeleft,text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)

        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_postcode,width=29,font=("arial",13))
        txtPostCode.grid(row=4,column=1)

        #mobilenumber
        lblMobile=Label(labelframeleft,text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)

        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_Mobile,width=29,font=("arial",13,))
        txtMobile.grid(row=5,column=1)

        #email
        lblEmail=Label(labelframeleft,text="Email ID:",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)

        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_EmailID,width=29,font=("arial",13))
        txtEmail.grid(row=6,column=1)

        #nationality
        lblNationality=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_Nationality,font=("arial",12),width=27,state="readonly")
        combo_Nationality["value"]=("Indian","American","British")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        #idproof type comobox
        lblIdProof=Label(labelframeleft,text="Id Proof Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_IDproof,font=("arial",12),width=27,state="readonly")
        combo_id["value"]=("Adhar Card","Driving Licence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        #id number
        lblIdNumber=Label(labelframeleft,text="ID Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)

        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_IDnumber,width=29,font=("arial",13))
        txtIdNumber.grid(row=9,column=1)

        #address
        lblAddress=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)

        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13))
        txtAddress.grid(row=10,column=1)

        #btns
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #Table frame search type
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("algerian",12),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12),width=24,state="readonly")
        combo_Search["value"]=("Ref","EmailID","name","address")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)


        #show data table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
 
        self.Cust_details_tables=ttk.Treeview(details_table,column=("ref","name","fathername","gender","postcode","Mobile","EmailID","Nationality","IDproof","IDnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_details_tables.xview)
        scroll_y.config(command=self.Cust_details_tables.yview)

        self.Cust_details_tables.heading("ref",text="Refer No")
        self.Cust_details_tables.heading("name",text="Name")
        self.Cust_details_tables.heading("fathername",text="Father Name")
        self.Cust_details_tables.heading("gender",text="Gender")
        self.Cust_details_tables.heading("postcode",text="PostCode")
        self.Cust_details_tables.heading("Mobile",text="Mobile")
        self.Cust_details_tables.heading("EmailID",text="EmailID")
        self.Cust_details_tables.heading("Nationality",text="Nationality")
        self.Cust_details_tables.heading("IDproof",text="ID Proof")
        self.Cust_details_tables.heading("IDnumber",text="ID number")
        self.Cust_details_tables.heading("address",text="Address")
        
        self.Cust_details_tables["show"]="headings"
        self.Cust_details_tables.column("ref",width=100)
        self.Cust_details_tables.column("name",width=100)
        self.Cust_details_tables.column("fathername",width=100)
        self.Cust_details_tables.column("gender",width=100)
        self.Cust_details_tables.column("postcode",width=100)
        self.Cust_details_tables.column("Mobile",width=100)
        self.Cust_details_tables.column("EmailID",width=100)
        self.Cust_details_tables.column("Nationality",width=100)
        self.Cust_details_tables.column("IDproof",width=100)
        self.Cust_details_tables.column("IDnumber",width=100)
        self.Cust_details_tables.column("address",width=100)
        
        self.Cust_details_tables.pack(fill=BOTH,expand=1)
        self.Cust_details_tables.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data() 



    def add_data(self):   
        if self.var_Mobile.get()=="" or self.var_fathername.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                   self.var_ref.get(),
                                                                                   self.var_cust_name.get(),
                                                                                   self.var_fathername.get(),
                                                                                   self.var_gender.get(),
                                                                                   self.var_postcode.get(),
                                                                                   self.var_Mobile.get(),
                                                                                   self.var_EmailID.get(),
                                                                                   self.var_Nationality.get(),
                                                                                   self.var_IDproof.get(),
                                                                                   self.var_IDnumber.get(),
                                                                                   self.var_address.get()

                                                                                            
                                                                                 ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es: 
                messagebox.showwarning("Warning",f"Somethhing went wroong:{str(es)}",parent=self.root)   
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_tables.delete(*self.Cust_details_tables.get_children())
            for i in rows:
                self.Cust_details_tables.insert("",END,values=i)
            conn.commit()
        conn.close()    

    def get_cuersor(self,event=""):
        cusrsor_row=self.Cust_details_tables.focus()
        content=self.Cust_details_tables.item(cusrsor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_fathername.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_postcode.set(row[4]),
        self.var_Mobile.set(row[5]),
        self.var_EmailID.set(row[6]),
        self.var_Nationality.set(row[7]),
        self.var_IDproof.set(row[8]),
        self.var_IDnumber.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_Mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set name=%s,fathername=%s,gender=%s,postcode=%s,Mobile=%s,EmailID=%s,Nationality=%s,IDproof=%s,IDnumber=%s,address=%s where ref=%s",(
                                                                                                                                                                               
                                                                                                                                                                                    self.var_cust_name.get(),
                                                                                                                                                                                    self.var_fathername.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_postcode.get(),
                                                                                                                                                                                    self.var_Mobile.get(),
                                                                                                                                                                                    self.var_EmailID.get(),
                                                                                                                                                                                    self.var_Nationality.get(),
                                                                                                                                                                                    self.var_IDproof.get(),
                                                                                                                                                                                    self.var_IDnumber.get(),
                                                                                                                                                                                    self.var_address.get() ,
                                                                                                                                                                                    self.var_ref.get()
                                                                                                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details has been updated successfully",parent=self.root)
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()      

    def reset(self):
       # self.var_ref.set(""),        
        self.var_cust_name.set(""),
        self.var_fathername.set(""),
       # self.var_gender.set(""),
        self.var_postcode.set(""),
        self.var_Mobile.set(""),
        self.var_EmailID.set(""),
       # self.var_Nationality.set(""),
       # self.var_IDproof.set(""),
        self.var_IDnumber.set(""),
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
        my_cursor=conn.cursor()
        

        my_cursor.execute("select * from customer where " + str(self.search_var.get()) +" LIKE '%" + str(self.txt_search.get()) + "%'")   
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_tables.delete(*self.Cust_details_tables.get_children())
            for i in rows:
                self.Cust_details_tables.insert("",END,values=i)
                conn.commit()
            conn.close()       
            

        
if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
