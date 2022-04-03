from importlib.resources import contents
from multiprocessing import parent_process
from optparse import Values
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
    def __init__(self, root):
          self.root=root
          self.root.geometry("1200x480+80+170")
          self.root.config(bg="white")
          self.root.title("Student Result Management System")
          self.root.focus_force()

    #=====title=======
          title=Label(self.root,text="Add Student Results" ,font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)

    #========widgets=========
    #========variables=======
          self.var_roll=StringVar()
          self.var_name=StringVar()
          self.var_course=StringVar()
          self.var_marks=StringVar()
          self.var_full_marks=StringVar()
          self.roll_list=[]

          lbl_select=Label(self.root,text="Select Student" ,font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
          lbl_name=Label(self.root,text="Name" ,font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
          lbl_course=Label(self.root,text="Course" ,font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
          lbl_marks=Label(self.root,text="Marks Obtained" ,font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
          lbl_full_marks=Label(self.root,text="Full Marks" ,font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)

          self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy odl style",15,'bold'),state='readonly',justify=CENTER)
          self.txt_student.place(x=280,y=100,width=200)
          self.txt_student.set("Select")
          btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4", fg="white", cursor="hand2").place(x=500,y=100,width =120,height=28)

          txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,'bold'),bg='lightyellow',state='readonly').place(x=280,y=160,width=320)
          txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,'bold'),bg='lightyellow', state='readonly').place(x=280,y=220,width=320)
          txt_marks=Entry(self.root,textvariable=self.var_marks,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=280,y=280,width=320)
          txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=280,y=340,width=320)

      #=====button=======
          btn_add=Button(self.root,text ="Submit", font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2").place(x=300,y=420,width=120,height=35)
          btn_add=Button(self.root,text ="Clear", font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2").place(x=430,y=420,width=120,height=35)

      #======images=======
          self.bg_img=Image.open("images/result.jpg")
          self.bg_img=self.bg_img.resize((500,300),Image.ANTIALIAS)
          self.bg_img=ImageTk.PhotoImage(self.bg_img)

          self.lbl_bg=Label(self.root,image=self.bg_img).place(x=650,y=100)

      #====================================================
    def search(self):
          con = sqlite3.connect(database="rms.db")
          cur = con.cursor()
          try:
                cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
                rows = cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                      self.CourseTable.insert('', END, values=row)
          except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")
if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()