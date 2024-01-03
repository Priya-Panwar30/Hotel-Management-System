from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk     #pip install plilow
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        #text variable
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


         #bg image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\FMT\OneDrive\Desktop\images\rcpoy.jpg") 
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

         #left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\FMT\OneDrive\Desktop\images\reg.jpg") 
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #main frame
        frame=Frame(self.root,bg="light blue")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("algerian",25,"bold"),fg="white",bg="light blue")
        register_lbl.place(x=20,y=20)

        #label and frame 
        #row1
        fname=Label(frame,text="First Name",font=("algerian",18,"bold"),fg="white",bg="light blue")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("arial",15))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("algerian",18,"bold"),fg="white",bg="light blue")
        l_name.place(x=370,y=100)

        self.txt_l_name_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("arial",15))
        self.txt_l_name_entry.place(x=370,y=130,width=250)

        #row2
        contact=Label(frame,text="Contact No",font=("algerian",18,"bold"),fg="white",bg="light blue")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("arial",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("algerian",18,"bold"),fg="white",bg="light blue")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("arial",15))
        self.txt_email.place(x=370,y=200,width=250)

        #row3
        security_Q=Label(frame,text="Select Security Question",font=("algerian",16,"bold"),fg="white",bg="light blue")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("arial",12),state="readonly")
        self.combo_security_Q["value"]=("Select","Birth Place","Girlfriend Name","Pet Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)

        security_A=Label(frame,text="Security Answer",font=("algerian",18,"bold"),bg="light blue",fg="white")
        security_A.place(x=370,y=240)

        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("arial",15))
        self.txt_security.place(x=370,y=270,width=250)


        #row4
        pswd=Label(frame,text="Password",font=("algerian",18,"bold"),fg="white",bg="light blue")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("arial",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("algerian",18,"bold"),fg="white",bg="light blue")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("arial",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #check btn
        self.var_check=IntVar()
        self.chechbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms And Conditions",font=("algerian",18,"bold"),bg="light blue",onvalue=1,offvalue=0)
        self.chechbtn.place(x=50,y=390)

        #btns
        img=Image.open(r"C:\Users\FMT\OneDrive\Desktop\images\regicon.jpeg")
        img=img.resize((200,55))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("arial",15,"bold"))
        b1.place(x=50,y=430,width=200)

        img1=Image.open(r"C:\Users\FMT\OneDrive\Desktop\images\loginicon.jpeg")
        img1=img1.resize((200,45))
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("arial",15,"bold"))
        b1.place(x=330,y=430,width=200)

        #function declartion
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree all terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Priya#1234",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another Email")
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
            messagebox.showinfo("Success","Register Successfully")    








        
         





if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()         