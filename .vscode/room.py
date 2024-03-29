from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import mysql.connector 
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("hotel management system")
        self.root.geometry("1295x550+230+220")

        #variable
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar() 
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

         #title
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("algerian",18),bg="white",fg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #logo
        img2=Image.open(r"C:\Users\FMT\OneDrive\Desktop\images\1690518105333.jpeg") 
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
  
         #label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING Details",font=("algerian",12),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
         
         #labels and entrys
        #customer contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13))
        enty_contact .grid(row=0,column=1,sticky=W)

        #fetch data btn
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)
 
        #check in date
        check_in_date=Label(labelframeleft,text="Check_in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txt_check_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13))
        txt_check_in_date.grid(row=1,column=1)

        #check out date
        check_out_date=Label(labelframeleft,text="Check_Out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)
        txt_check_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13))
        txt_check_out_date.grid(row=2,column=1)

        #Room type
        label_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12),width=27,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

         #Avaiable Room
        lblRoomAvailable=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        #txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13))
        #txtRoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

         #Meal
        lblMeal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        combo_Meal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12),width=27,state="readonly")
        combo_Meal["value"]=("Breakfast","Lunch","Dinner")
        combo_Meal.current(0)
        combo_Meal.grid(row=5,column=1)

         #No of days
        lblNoOfDays=Label(labelframeleft,text="No Of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13))
        txtNoOfDays.grid(row=6,column=1)

         #Paid Tax
        lblNoOfDays=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13))
        txtNoOfDays.grid(row=7,column=1)

         #Sub Total
        lblNoOfDays=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13))
        txtNoOfDays.grid(row=8,column=1)

         #Total Cost
        lblIDNumber=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIDNumber.grid(row=9,column=0,sticky=W)
        txtIDNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13))
        txtIDNumber.grid(row=9,column=1)

        #bill btn
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

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

        #right side image
        img3=Image.open(r"C:\Users\FMT\OneDrive\Desktop\images\bed2.webp") 
        img3=img3.resize((530,230))
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=530,height=230)

        #Table frame search type
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("algerian",12),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
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
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
 
        self.room_table=ttk.Treeview(details_table,column=("contact","Checkin","Checkout","Roomtype","RoomAvailable","Meal","NoOfDays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("Checkin",text="Chech-in")
        self.room_table.heading("Checkout",text="Check-out")
        self.room_table.heading("Roomtype",text="Room Type")
        self.room_table.heading("RoomAvailable",text="Room No")
        self.room_table.heading("Meal",text="Meal")
        self.room_table.heading("NoOfDays",text="NoOfDays")
        
        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("Checkin",width=100)
        self.room_table.column("Checkout",width=100)
        self.room_table.column("Roomtype",width=100)
        self.room_table.column("RoomAvailable",width=100)
        self.room_table.column("Meal",width=100)
        self.room_table.column("NoOfDays",width=100)
      
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
     #add data
    def add_data(self):   
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
                my_cursor=conn.cursor()
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
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es: 
                messagebox.showwarning("Warning",f"Somethhing went wroong:{str(es)}",parent=self.root)   
 
     #fetch data                       
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
        for i in rows:
            self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
     #getcursor
    def get_cuersor(self,event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

     #udpate func
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Check_in=%s,Check_out=%s,Roomtype=%s,Roomavailable=%s,Meal=%s,NoOfDays=%s where Contact=%s",(
                                                                                                                                                                               
                                                                                                                                    
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
            messagebox.showinfo("Update","Room Details has been updated successfully",parent=self.root)  

        #delete      
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","do you want to delete the customer booking",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 

        #reset
    def reset(self):
        #self.var_contact.set(),
        self.var_checkin.set(),
        self.var_checkout.set(),
        #self.var_roomtype.set(),
        self.var_roomavailable.set(),
        self.var_meal.set(),
        self.var_noofdays.set()
        self.var_paidtax.set()
        self.var_actualtotal.set()
        self.var_total.set()

    
        
   #All data fetch
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
              messagebox.showerror("Error","This number Not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                #gender
                conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #email
                conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
                my_cursor=conn.cursor()
                query=("select EmailID from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmailID=Label(showDataframe,text="EmailID:",font=("arial",12,"bold"))
                lblEmailID.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                #Idproof
                conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
                my_cursor=conn.cursor()
                query=("select IDproof from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblIDproof=Label(showDataframe,text="IDprrof:",font=("arial",12,"bold"))
                lblIDproof.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                #IDnumber
                conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
                my_cursor=conn.cursor()
                query=("select IDnumber from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblIDnumber=Label(showDataframe,text="IDnumber:",font=("arial",12,"bold"))
                lblIDnumber.place(x=0,y=120)

                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)

                #address
                conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
                my_cursor=conn.cursor()
                query=("select address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=150)

                lbl6=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl6.place(x=90,y=150)

        #search systen
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Priya#1234",database="amitdb")
        my_cursor=conn.cursor()
        

        my_cursor.execute("select * from room where " + str(self.search_var.get()) +" LIKE '%" + str(self.txt_search.get()) + "%'")   
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
                conn.commit()
            conn.close()             
  

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y") 
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
          q1=float(700)
          q2=float(7000)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.18))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.18)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
          q1=float(1500)
          q2=float(7000)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.18))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.18)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)


        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
          q1=float(2000)
          q2=float(7000)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.18))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.18)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

          
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
          q1=float(700)
          q2=float(3000)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.18))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.18)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

          
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
          q1=float(1500)
          q2=float(3000)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.18))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.18)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)


          
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
          q1=float(2000)
          q2=float(3000)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.18))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.18)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

          
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
          q1=float(700)
          q2=float(5000)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.18))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.18)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

          
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
          q1=float(1500)
          q2=float(5000)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.18))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.18)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

          
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
          q1=float(2000)
          q2=float(5000)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.18))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.18)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

         










        
        



if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()        
