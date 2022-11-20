from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")



        #=========================variables=====================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_secur_que=StringVar()
        self.var_secur_ans=StringVar()
        self.var_password=StringVar()
        self.var_confirmpass=StringVar()


        # ========================bg image============
        self.bg=ImageTk.PhotoImage(file=r"d:\Users\Anjali\Desktop\Face Recognition System\college_images\employee_img2.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # ========================left image============
        self.bg1=ImageTk.PhotoImage(file=r"d:\Users\Anjali\Desktop\Face Recognition System\college_images\thought-good-morning-messages-LoveSove.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=80,y=100,width=470,height=550)

        #=============main frame=============
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        reg_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="darkgreen")
        reg_lbl.place(x=20,y=20)


        # ==================label and entry================

        #===================Row1==============
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)


        #=================Row2=====================
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)


        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)


        #=================Row3=====================
        secur_que=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        secur_que.place(x=50,y=240)

        self.combo_secur_que=ttk.Combobox(frame,textvariable=self.var_secur_que,font=("times new roman",15,"bold"),state="readonly")
        self.combo_secur_que["values"]=("Select Question","Your Birth Place.","Your Favourtie Actor","Your pet name","Your First school name","Your Favourite Teacher name")
        self.combo_secur_que.place(x=50,y=270,width=250)
        self.combo_secur_que.current(0)
        


        secur_ans=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        secur_ans.place(x=370,y=240)

        self.txt_secur_ans=ttk.Entry(frame,textvariable=self.var_secur_ans,font=("times new roman",15))
        self.txt_secur_ans.place(x=370,y=270,width=250)


        #=================Row4=====================
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=50,y=310)

        self.txt_passwd=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        self.txt_passwd.place(x=50,y=340,width=250)


        confirm_passwd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_passwd.place(x=370,y=310)

        self.txt_confirm_passwd=ttk.Entry(frame,textvariable=self.var_confirmpass,font=("times new roman",15))
        self.txt_confirm_passwd.place(x=370,y=340,width=250)


        #=================check button=====================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",10,"bold"),onvalue=1,offvalue=0,bg="white")
        checkbtn.place(x=50,y=380)


        #==================Login button============
        img=Image.open(r"d:\Users\Anjali\Desktop\Face Recognition System\college_images\register-now-button1.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=430,width=200)

        img1=Image.open(r"d:\Users\Anjali\Desktop\Face Recognition System\college_images\loginpng.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=350,y=430,width=200)



    #===========================Function declaration=====================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_secur_que.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_password.get()!=self.var_confirmpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same.")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree or terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Anjali123",database="facerecognitionsystem")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            values=(self.var_email.get(),)
            my_cursor.execute(query,values)
            row=my_cursor.fetchone()
            
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_secur_que.get(),
                                                                                        self.var_secur_ans.get(),
                                                                                        self.var_password.get()

                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("success","Register Successfully")


if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()