from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata = []

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # first image
        img=Image.open(r"college_images\smart-attendance.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)


        #=============variables================
        self.var_attend_id = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()
        

        # second image
        img1=Image.open(r"college_images\iStock.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)


        # backgroung image
        img3=Image.open(r"college_images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1500,height=650)


        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=795,height=580)

        img_left=Image.open(r"college_images\face-recognition.png")
        img_left=img_left.resize((780,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=780,height=130)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=780,height=370)

        #Label and Entry
        # Attendence_id
        attendence_id_label = Label(left_inside_frame, text="Attendence ID :", font=("times new roman", 13, "bold"), bg="white")
        attendence_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendence_id_entry = ttk.Entry(left_inside_frame,width=20, textvariable=self.var_attend_id, font=("times new roman", 13, "bold"))
        attendence_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Attendence_Roll
        rollLabel = Label(left_inside_frame, text="Roll :", font=("times new roman", 13, "bold"), bg="white")
        rollLabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        atten_roll = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_attend_roll, font=("times new roman", 13, "bold"))
        atten_roll.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Attendence_Name
        nameLabel = Label(left_inside_frame, text="Name :", font=("times new roman", 13, "bold"), bg="white")
        nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        atten_name = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_attend_name, font=("times new roman", 13, "bold"))
        atten_name.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Attendence_Department
        depLabel = Label(left_inside_frame, text="Department :", font=("times new roman", 13, "bold"), bg="white")
        depLabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        atten_dep = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_attend_dep, font=("times new roman", 13, "bold"))
        atten_dep.grid(row=1, column=3, padx=10, pady=5, sticky=W)

       # Attendence_time
        timeLabel = Label(left_inside_frame, text="Time :", font=("times new roman", 13, "bold"), bg="white")
        timeLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        atten_time = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_time, font=("times new roman", 13, "bold"))
        atten_time.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Attendence_date
        dateLabel = Label(left_inside_frame, text="Date :", font=("times new roman", 13, "bold"), bg="white")
        dateLabel.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        atten_date = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_attend_date, font=("times new roman", 13, "bold"))
        atten_date.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Attendance
        attendancelabel = Label(left_inside_frame, text="Attendance Status :", font=("times new roman", 13, "bold"), bg="white")
        attendancelabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_attend_attendance, font=("times new roman", 13, "bold"), state="readonly", width=18)
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        self.atten_status.current(0)

        # button Frame
        btn_frame=Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=8,y=300,width=750,height=36)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset", command=self.reset_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

    

        # right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=815,y=10,width=670,height=570)


        table_frame=Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5,y=5,width=650,height=445)

        #=====================Scroll Bar============================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=(
            "id", "roll", "name", "department", "time", "date", "attendanace"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance Id")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendanace", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendanace", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)


        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)


    #==========================fetch data========
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        filename = filedialog.askopenfilename(initialdir = os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(filename) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    #export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No Data Found to export", parent = self.root)
                return False
            filename = filedialog.asksaveasfilename(initialdir = os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(filename, mode="w", newline="") as myfile:
                export_write = csv.writer(myfile, delimiter = ",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(filename)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}", parent = self.root)

            

    #======get cursor========
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])



    #==========reset data========
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")






if __name__ == "__main__":  
    root=Tk()
    obj = Attendance(root)
    root.mainloop()