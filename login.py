from datetime import datetime
from time import strftime
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import FaceRecognitionSystem
import mysql.connector
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import random
import os


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()



class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x800+0+0")


         # first image
        img=Image.open(r"d:\Users\Anjali\Desktop\Face Recognition System\college_images\facial-recognition_0.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        # second image
        img1=Image.open(r"d:\Users\Anjali\Desktop\Face Recognition System\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        # third image
        img2=Image.open(r"d:\Users\Anjali\Desktop\Face Recognition System\college_images\smart-attendance.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        # backgroung image
        img3=Image.open(r"d:\Users\Anjali\Desktop\Face Recognition System\college_images\2-AI-invades-automobile.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'), bg='white', fg='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=230,width=340,height=450)

        img4=Image.open(r"d:\Users\Anjali\Desktop\Face Recognition System\college_images\LoginIconAppl.png")
        img4=img4.resize((100,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg1=Label(image=self.photoimg4,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=235,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)


        # labels
        usernamelbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        usernamelbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        # password
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpassword=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpassword.place(x=40,y=250,width=270)

        #==========Icon Images==============
        img5=Image.open(r"d:\Users\Anjali\Desktop\Face Recognition System\college_images\LoginIconAppl.png")
        img5=img5.resize((25,25),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg1=Label(image=self.photoimg5,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=383,width=25,height=25)

        img6=Image.open(r"d:\Users\Anjali\Desktop\Face Recognition System\college_images\lock-512.png")
        img6=img6.resize((25,25),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        lblimg2=Label(image=self.photoimg6,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=453,width=25,height=25)


        #==================Login button============
        loginbtn=Button(frame,text="Login",borderwidth=3,relief=RIDGE,command=self.login,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #==================Register button==========
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),border=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #==================Forgot password=========
        forgotpassbtn=Button(frame,text="Forgot Password", command=self.forgot_password_window,font=("times new roman",10,"bold"),border=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=10,y=372,width=160)


        bottom_lbl=Label(self.root,text="Note: Enter valid username and Valid Password",font=("times new roman",25,"bold"),bg="white",fg="darkblue")
        bottom_lbl.place(x=0,y=745,width=1530,height=45)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error","All fildes are required")
        elif self.txtuser.get()=="Anju" and self.txtpassword.get()=="Ishika@11":
            messagebox.showinfo("Successfull","Welcome with anju")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Anjali123",database="facerecognitionsystem")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpassword.get()
                                                                                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=FaceRecognitionSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()


    def clear(self):
        self.txtuser.set("")
        self.txtpassword.set("")


    #**************************************Reset Password***************************
    def reset_pass(self):
        if self.combo_secur_que.get() == "select Question":
            messagebox.showerror("Error","Select the security Question",parent = self.root2)
        elif self.txt_secur_ans.get() =="":
            messagebox.showerror("Error","Please Enter the answer",parent = self.root2)
        elif self.txt_new_password.get() =="":
            messagebox.showerror("Error","Please Enter the New Password",parent = self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Anjali123",database="facerecognitionsystem")
            my_cursor=conn.cursor()
            query = ("select * from register where email=%s and Seq_que=%s and seq_ans=%s")
            value = (self.txtuser.get(), self.combo_secur_que.get(), self.txt_secur_ans)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","Please enter the Correct Answer",parent = self.root2)
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.txt_new_password.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()  
                messagebox.showinfo("Success","Your Password has been reset, Please login New Password",parent = self.root2)
                self.root2.destroy()



    #************************************** Forgot Password ***************************
    def forgot_password_window(self):
        if self.txtuser.get() =="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Anjali123",database="facerecognitionsystem")
            my_cursor=conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row == None:
                messagebox.showerror("Error","Please Enter the valid Username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                lbl = Label(self.root2, text="Forgot Password", font=("times new roman",20,"bold"),fg="red",bg="white")
                lbl.place(x=0,y=10,relwidth=1)


                secur_que=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                secur_que.place(x=50,y=80)

                self.combo_secur_que=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_secur_que["values"]=("Select Question","Your Birth Place.","Your Favourtie Actor","Your pet name","Your First school name","Your Favourite Teacher name")
                self.combo_secur_que.place(x=50,y=110,width=250)
                self.combo_secur_que.current(0)


                secur_ans=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                secur_ans.place(x=50,y=150)

                self.txt_secur_ans=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_secur_ans.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman",15,"bold"),bg="green", fg="white")
                btn.place(x=120, y=290, width=125)



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



class FaceRecognitionSystem:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # first image
        img=Image.open(r"college_images\Stanford.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        # second image
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        # third image
        img2=Image.open(r"college_images\u.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        # backgroung image
        img3=Image.open(r"college_images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3) 
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'), bg='white', fg='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # student button
        img4=Image.open(r"college_images\student-portal_1.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_l=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=200,y=300,width=220,height=40)


        # Detect face
        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)
        
        b2_l=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_l.place(x=500,y=300,width=220,height=40)


        # Attendence
        img6=Image.open(r"college_images\report.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=220,height=220)
        
        b3_l=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_l.place(x=800,y=300,width=220,height=40)


        # Help face button
        img7=Image.open(r"college_images\help-desk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b4.place(x=1100,y=100,width=220,height=220)
        
        b4_l=Button(bg_img,text="Help Disk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_l.place(x=1100,y=300,width=220,height=40)


        # Train Data button
        img8=Image.open(r"college_images\facialrecognition (1).png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=400,width=220,height=220)
        
        b5_l=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_l.place(x=200,y=600,width=220,height=40)


        # Photos button
        img9=Image.open(r"college_images\photo.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=400,width=220,height=220)
        
        b6_l=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_l.place(x=500,y=600,width=220,height=40)


        # Developer button
        img10=Image.open(r"college_images\developer1.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=800,y=400,width=220,height=220)
        
        b7_l=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_l.place(x=800,y=600,width=220,height=40)

        # Exit button
        img11=Image.open(r"college_images\exit1.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.IExit)
        b8.place(x=1100,y=400,width=220,height=220)
        
        b8_l=Button(bg_img,text="Exit",cursor="hand2",command=self.IExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_l.place(x=1100,y=600,width=220,height=40)


    def open_img(self):
        os.startfile("data")


    def IExit(self):
        self.IExit = messagebox.askyesno(
            "Face Recognition", "Are you sure exit this project", parent=self.root)
        if self.IExit > 0:
            self.root.destroy()
        else:
            return

    # ===================Function Button=======================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


    


if __name__ == "__main__":
    main()