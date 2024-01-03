from tkinter import*
from PIL import Image,ImageTk    #pip install pillow 
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("hotel management system")
        self.root.geometry("1550x800+0+0")
        
        # 1st img
        img1=Image.open(r"C:\Users\FMT\OneDrive\Desktop\images\199016139_182574440591853_4926984891577297065_n.jpg") 
        img1=img1.resize((1550,310))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=280)

         #logo
        img2=Image.open(r"C:\Users\FMT\OneDrive\Desktop\images\1690518105333.jpeg") 
        img2=img2.resize((230,140))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)


        #title
        lbl_title=Label(self.root,text="FRONT OFFICE",font=("algerian",35),bg="white",fg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #main frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #menu
        lbl_menu=Label(main_frame,text="MENU",font=("verdana",20,),bg="white",fg="black",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #btn frame
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=30,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("verdana",14),bg="white",fg="black",bd=0,cursor="hand1")
        cust_btn.grid( row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("verdana",14,),bg="white",fg="black",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("verdana",14),bg="white",fg="black",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

       

        #logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("verdana",14,),bg="white",fg="black",bd=0,cursor="hand1")
        #ogout_btn.grid(row=3,column=0,pady=1)

        #right side image
        img3=Image.open(r"C:\Users\FMT\OneDrive\Desktop\images\319691620.jpg") 
        img3=img3.resize((1310,590))
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)    



      
 

      


if __name__ =="__main__":
     root=Tk()     
     obj=HotelManagementSystem(root)
     root.mainloop()