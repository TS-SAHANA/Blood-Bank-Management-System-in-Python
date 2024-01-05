 #------------------------------->WANTED
'''import tkinter as tk

window = tk.Tk()
window.title("BLOOD BANK MANAGEMENT")
window.geometry("1350x700")

window.config(bg="blue")

title_label = tk.Label(window,text="BLOOD BANK MANAGEMENT",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="red",fg="white")
title_label.pack(side=tk.TOP,fill=tk.X)

window.mainloop()'''

'''with open("Guidelines.txt") as G:
        guidelines=G.read()

import tkinter as tk
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = guidelines)

# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()

# Buttons Creation
printButton = tk.Button(frame,
                        text = "Donor", 
                        command = printInput)
printButton.pack()
  
# Quotes Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
'''
#Image---------------------------------------->WANTED
'''
from tkinter import *

window = Tk()
window.title("BLOOD BANK MANAGEMENT")
window = Canvas(window, width=450,height=450)
window.pack()
image= PhotoImage(file = "Blood Donation Logo.png")
window.create_image(100, 120, anchor=NW, image=image)

window.mainloop()
'''
# Near to Final...........
'''from tkinter import *

window = Tk()
window.title("BLOOD BANK MANAGEMENT")
window.geometry("1350x700")

window.config(bg="blue")

title_label = Label(window,text="BLOOD BANK MANAGEMENT",font=("Arial",30,"bold"),border=12,relief=GROOVE,bg="red",fg="white")
title_label.pack(side=TOP,fill=X)

#printButton = Button(window,text = "Donor",justify=LEFT)
#printButton.pack()

donorbtn=Button(window,text="DONOR",fg="Red")
donorbtn.pack(side=LEFT)

window = Canvas(window, width=200,height=200)
window.pack(side=TOP,anchor=E)
img= PhotoImage(file = "Blood Donation Logo.png")
window.create_image(-10, -10, anchor=NW, image=img)

#recepient

window.mainloop()'''
#Main reference for the source code
'''from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import pickle

root=Tk( ) #main window for GUI Application
root.title("Employee Management System") #Give title to the main window
root.geometry('1300x1000')

def Exit1( ):
    res=tkinter.messagebox.askquestion(message="Do You Want To EXIT")
    if res=="yes":
        root.destroy( )

def ClearFrame( ):
    for widget in F2.winfo_children( ):
        widget.destroy( )

def Clear( ):
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
    ClearFrame( )

def ViewAll( ):
    for widget in F2.winfo_children( ):
        widget.destroy( )
    try:
        with open("Employee",'rb') as fil:
            Label(F2,text="%s %s %s %s %s %s %s" % ("      ID |","      NAME |","      MOBILE |","      EMAIL |","      DESIG  |","      DEPT  |","      SAL  |")).pack( )
            Label(F2,text="%s" % "*"*60).pack( )
            Rec=pickle.load(fil)
            c=len(Rec)
            for i in Rec:
                Label(F2,text="%s %s %s %s %s %s %s" % (str(i["ID"])+"  |  ",i["NAME"]+"  |  ",str(i["Mob"])+"  |  ",i["Email"]+"  |  ",i["Desig"]+"  |  ",i["DeptID"]+"  |  ",str(i["Sal"])+"  |  ")).pack( )

    except FileNotFoundError:
        Label(F2,text="%s" % "File doesn't exist").pack( )
    except EOFError:
        Label(F2,text="%s" % "File doesn't exist").pack( )

def AddRec( ):
    try:
        fil=open("Employee",'ab+')
        if fil.tell( )>0:
            fil.seek(0)
            Rec1=pickle.load(fil)
        else:
            Rec1=[ ]

        Rec={ }

        if any(dict.get('ID') == E1.get( ) for dict in Rec1):
            tkinter.messagebox.showerror(message="Employee Id already exist")
            E1.delete(0,END)
        else:
            Rec["ID"]=E1.get( )
        if len(E2.get( ))<=0:
            tkinter.messagebox.showerror(message="Name not entered")
        else:
            Rec["NAME"]=E2.get( )

        if len(E3.get( ))!=10 or E3.get( ).isdigit( )==False:
           tkinter.messagebox.showerror(message="Please enter valid Mobile No")
        else:
            Rec["Mob"]=E3.get( )

        if '@' not in E4.get( ) or '.' not in E4.get( ):
            tkinter.messagebox.showerror(message="Enter Valid mail address")
        else:
            Rec["Email"]=E4.get( )

        if len(E5.get( ))==0 or int(E5.get( ))<=0:
            tkinter.messagebox.showerror(message="Enter Valid Salary amount")
        else:
            Rec["Sal"]=int(E5.get( ))

        Rec["Desig"]=Des.get( )
        Rec["DeptID"]=Dept.get( )
        Rec1.append(Rec)
        fil.close( )

        if len(E1.get( ))>0 and len(E2.get( ))>0 and len(E3.get( ))==10 and E3.get( ).isdigit( )==True and '@' in E4.get( ) and '.' in E4.get( ) and len(E5.get( ))!=0 and int(E5.get( ))>0:
            res=tkinter.messagebox.askyesno(message="Please Confirm to add the file")
            if res==True:
                with open("Employee",'wb') as fil: #will open the file for overwriting
                    pickle.dump(Rec1,fil)
                    #Label(F2,text="Record added").pack( )
                    Clear( )
    except ValueError:
        tkinter.messagebox.showerror(message="Invalid Value entered for Salary")

def RemRecord( ):
     if len(E1.get( ))==0:
        tkinter.messagebox.showinfo(message="Enter the Employee Id in the field to remove the record")
     ClearFrame( )
     try:
        with open("Employee",'rb+') as fil:
            Rec=pickle.load(fil)
            for i in range(0,len(Rec)):
                if Rec[i]["ID"]==E1.get( ):
                    Label(F2,text="%s" % "Record Found").pack( )
                    N=Rec[i]
                    E2.insert(0,N["NAME"])
                    E3.insert(0,N["Mob"])
                    E4.insert(0,N["Email"])
                    E5.insert(0,N["Sal"])
                    if N["DeptID"]=="MGR":
                        Dept.current(0)
                    elif N["DeptID"]=="CLK":
                       Dept.current(1)
                    elif N["DeptID"]=="VP":
                        Dept.current(2)
                    else:
                        Dept.current(3)
                    if N["Desig"]=="HR":
                        Des.current(0)
                    elif N["Desig"]=="IT":
                       Des.current(1)
                    elif N["Desig"]=="SALES":
                        Des.current(2)
                    else:
                        Des.current(3)

                    ch=tkinter.messagebox.askyesno(message="Delete the account")
                    if ch==True:
                        Rec.pop(i)
                        Label(F2,text="%s" % "Record Deleted").pack( )
                    break
            else:
                Label(F2,text="%s" % "Record Not Found").pack( )

            fil.seek(0)
            pickle.dump(Rec,fil)
      
     except FileNotFoundError:
            print(F,"File Doesn't exist")
     except KeyError:
            print("Record Not found")
     except IndexError:
            print("Record Not found")

def Search( ):
    if len(E1.get( ))==0:
        tkinter.messagebox.showinfo(message="Enter the Employee Id in the field to search for the record")
    ClearFrame( )
    try:
        with open("Employee",'rb') as fil:
            Rec=pickle.load(fil)
            for i in range(0,len(Rec)):
                if Rec[i]["ID"]==E1.get( ):
                    Label(F2,text="%s" % "Record Found").pack( )
                    N=Rec[i]
                    E2.delete(0,END)
                    E2.insert(0,N["NAME"])
                    E3.delete(0,END)
                    E3.insert(0,N["Mob"])
                    E4.delete(0,END)
                    E4.insert(0,N["Email"])
                    E5.delete(0,END)
                    E5.insert(0,N["Sal"])
                    if N["DeptID"]=="MGR":
                        Dept.current(0)
                    elif N["DeptID"]=="CLK":
                       Dept.current(1)
                    elif N["DeptID"]=="VP":
                        Dept.current(2)
                    else:
                        Dept.current(3)
                    if N["Desig"]=="HR":
                        Des.current(0)
                    elif N["Desig"]=="IT":
                       Des.current(1)
                    elif N["Desig"]=="SALES":
                        Des.current(2)
                    else:
                        Des.current(3)
                    Label(F2,text="%s" % "Record Found",font=('Trebuchet',20)).pack( )
                    break
            else:
                Label(F2,text="%s" % "Record Not Found").pack( )
    except FileNotFoundError:
            print(F,"File Doesn't exist")
    except KeyError:
            print("Record Not found")
    except IndexError:
            print("Record Not found")

def UpdateRec( ):
    if len(E1.get( ))==0:
        tkinter.messagebox.showinfo(message="Click on Search to search and then update")
        Clear( )
    #ClearFrame( )
        
    try:
        with open("Employee",'rb+') as fil:
            found=-1
            Rec1=pickle.load(fil)
            Rec={ }
            for p in Rec1:
                if E1.get( )==p["ID"]:
                    found=0
                    if len(E2.get( ))<=0:
                        tkinter.messagebox.showerror(message="Name not entered")
                    else:
                        p["NAME"]=E2.get( )

                    if len(E3.get( ))!=10 or E3.get( ).isdigit( )==False:
                       tkinter.messagebox.showerror(message="Please enter valid Mobile No")
                    else:
                        p["Mob"]=E3.get( )

                    if '@' not in E4.get( ) or '.' not in E4.get( ):
                        tkinter.messagebox.showerror(message="Enter Valid mail address")
                    else:
                        p["Email"]=E4.get( )

                    if len(E5.get( ))==0 or int(E5.get( ))<=0:
                        tkinter.messagebox.showerror(message="Enter Valid Salary amount")
                    else:
                        p["Sal"]=int(E5.get( ))

                    p["Desig"]=Des.get( )
                    p["DeptID"]=Dept.get( )
                    break
            else:
                Label(F2,text="%s" % "Record Not Found").pack( )
                
            if found==0 and len(E1.get( ))>0 and len(E2.get( ))>0 and len(E3.get( ))==10 and E3.get( ).isdigit( )==True and '@' in E4.get( ) and '.' in E4.get( ) and len(E5.get( ))!=0 and int(E5.get( ))>0:
                res=tkinter.messagebox.askyesno(message="Please Confirm to update the file")
                if res==True:
                    fil.seek(0)
                    pickle.dump(Rec1,fil)
                    Label(F2,text="%s" % "Record Updated").pack( )
    except EOFError:
        print("File doesn't exist")
    except FileNotFoundError:
        print(F,"File doesn't exist")

def Report( ):
    Clear( )
    try:
        with open("Employee",'rb') as fil:
            Rec = pickle.load(fil)
            Label(F2,text="%s %s %s %s %s %s %s" % ("      ID |","      NAME |","      BASIC SALARY |","      HRA |","      DA |","      TAX  |","      GROSS SALARY  |"))
            Label(F2,text="%s" % "*"*100).pack( )

            for i in Rec:
                HRA=round(30*i["Sal"]/100,0)
                DA=round(15*i["Sal"]/100,0)
                TAX=round(((i["Sal"]+HRA+DA)*15/100),0)
                GROSS=HRA+DA+i["Sal"]-TAX
                Label(F2,text="%s %s %s %s %s %s %s" % (str(i["ID"])+"  |  ",i["NAME"]+"  |  ",str(i["Sal"])+"  |  ",str(i["HRA"])+"  |  ",str(i["DA"])+"  |  ",str(i["TAX"])+"  |  ",str(i["GROSS"])+"  |  "))
    except FileNotFoundError:
        print("File Doesn't exist")

Label(root,text="EMPLOYEE MANAGEMENT SYSTEM", font=("Arial bold",30),fg='blue').pack( )
F1=Frame(root,borderwidth=3,relief="solid")
F1.pack(side="left",expand=True,fill="both")
F2=Frame(root,borderwidth=3,relief="solid")
F2.pack(side="right",expand=True,fill="both")
Label(F2,text="WELCOME TO THE EMPLOYEE MANAGEMENT SYSTEM", font=("Trebuchet",20)).grid( row=0,column=0)

Label(F1,text="EMPLOYEE ID").grid( row=0,column=0)
E1=Entry(F1,bd=4)
E1.grid(row=0,column=1,padx=13,pady=10)

Label(F1,text="EMPLOYEE NAME").grid( row=1,column=0)
E2=Entry(F1,bd=4)
E2.grid(row=1,column=1,padx=13,pady=10)

Label(F1,text="MOBILE").grid( row=2,column=0)
E3=Entry(F1,bd=4)
E3.grid(row=2,column=1,padx=13,pady=10)

Label(F1,text="EMAIL").grid( row=3,column=0)
E4=Entry(F1,bd=4)
E4.grid(row=3,column=1,padx=13,pady=10)

Label(F1,text="DEPARTMENT").grid( row=4,column=0)
Dept=ttk.Combobox(F1)
Dept['values']=('MGR','CLK','VP','PRES')
Dept.current(0)
Dept.grid(row=4,column=1,padx=13,pady=10)

Label(F1,text="DESIGNATION").grid( row=5,column=0)
Des=ttk.Combobox(F1)
Des['values']=('HR','IT','SALES','FIN')
Des.current(0)
Des.grid(row=5,column=1,padx=13,pady=10)

Label(F1,text="SALARY").grid( row=6,column=0)
E5=Entry(F1,bd=4)
E5.grid(row=6,column=1,padx=13,pady=10)
Add=Button(F1,text="ADD RECORD",command=AddRec,padx=13,pady=10)
Add.grid(row=20,column=0,sticky=NSEW,padx=13,pady=10)
Del=Button(F1,text="DELETE RECORD",command=RemRecord)
Del.config(relief=RAISED)
Del.grid(row=20,column=1,sticky=NSEW,padx=13,pady=10)
Upd=Button(F1,text="UPDATE RECORD",command=UpdateRec)
Upd.grid(row=20,column=2,sticky=NSEW,padx=13,pady=10)
Ser=Button(F1,text="SEARCH RECORD",command=Search,padx=13,pady=10)
Ser.grid(row=21,column=0,sticky=NSEW,padx=13,pady=10)
View=Button(F1,text="VIEW ALL",command=ViewAll)
View.grid(row=21,column=1,sticky=NSEW,padx=13,pady=10)
Clr=Button(F1,text="CLEAR",command=Clear)
Clr.grid(row=21,column=2,sticky=NSEW,padx=13,pady=10)
Exit=Button(F1,text="EXIT",command=Exit1,padx=13,pady=10)
Exit.grid(row=22,column=0,sticky=NSEW,padx=13,pady=10)
Sal=Button(F1,text="SALARY GENERATION",command=Report)
Sal.grid(row=22,column=1,sticky=NSEW,padx=13,pady=10)
'''
#Main Coding (For our Program)....

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import pickle
from PIL import ImageTk,Image

root=Tk( ) # main window for GUI Application
root.title("Blood Bank Management") # Give title to the main window
root.geometry('1350x700') # Set the size of the window

def Exit1( ):
    res=tkinter.messagebox.askquestion(message="Do You Want To EXIT")
    if res=="yes":
        root.destroy( )

def ClearFrame( ):
    for widget in F2.winfo_children( ):
        widget.destroy( )
    Label(F2,text="     \"Tears Of A Mother Cannot Save Her Child \nBut YOUR BLOOD CAN\"", font=("Trebuchet",20,"bold"),bg="gold",fg="blue").pack()

def Clear( ):
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
    ClearFrame( )

def ViewAll( ):
    for widget in F2.winfo_children( ):
        widget.destroy( )
    Label(F2,text="     \"Tears Of A Mother Cannot Save Her Child \nBut YOUR BLOOD CAN\"", font=("Trebuchet",20,"bold"),bg="gold",fg="blue").pack()
    try:
        with open("Blood Donor",'rb') as fil:
            Label(F2,text="%s" % "-"*125,bg="gold",fg="blue", font=("Arial bold",10)).pack( )
            Label(F2,text="%s %s %s %s %s %s" % ("         ID |","      NAME |","      AGE |","      MOBILE |","      EMAIL  |","      BLOOD GRP  |"),bg="gold",fg="blue", font=("Arial bold",10)).pack( )
            Label(F2,text="%s" % "-"*125,bg="gold",fg="blue", font=("Arial bold",10)).pack( )
            Rec=pickle.load(fil)
            c=len(Rec)
            for i in Rec:
                Label(F2,text="%s %s %s %s %s %s" % (str(i["Id"])+"  |  ",i["Name"]+"  |  ",str(i["Age"])+"  |  ",str(i["Mob"])+"  |  ",i["Email"]+"  |  ",i["BG"]+"  |  "),bg="gold",fg="blue", font=("Arial bold",10)).pack( )

    except FileNotFoundError:
        Label(F2,text="%s" % "File doesn't exist",bg="gold",fg="blue", font=("Arial bold",10)).pack( )
    except EOFError:
        Label(F2,text="%s" % "File doesn't exist",bg="gold",fg="blue", font=("Arial bold",10)).pack( )

def AddRec( ):
    try:
        with open("Blood Donor",'ab+') as fil:
            if fil.tell( )>0:
                fil.seek(0)
                Rec1=pickle.load(fil)
            else:
                Rec1=[ ]
                
            Rec={ }
                        
            if any(dict.get('Id') == E1.get( ) for dict in Rec1):
                tkinter.messagebox.showerror(message="Donor Id already exist")
                E1.delete(0,END)
            else:
                Rec["Id"]=E1.get( )
            
            if len(E2.get( ))<=0:
                tkinter.messagebox.showerror(message="Name not entered")
            else:
                Rec["Name"]=E2.get( )

            if int(E3.get( ))<18 or int(E3.get( ))>65:
                tkinter.messagebox.showerror(message="Valid Age from 18 to 65 only")
            else:
                Rec["Age"]=E3.get( )
            
            if len(E4.get( ))!=10 or E4.get( ).isdigit( )==False:
               tkinter.messagebox.showerror(message="Please enter valid Mobile No")
            else:
                Rec["Mob"]=E4.get( )

            if '@' not in E5.get( ) or '.' not in E5.get( ):
                tkinter.messagebox.showerror(message="Enter Valid mail address")
            else:
                Rec["Email"]=E5.get( )

            Rec["BG"]=BG.get( )
            Rec1.append(Rec)

            if len(E1.get( ))>0 and len(E2.get( ))>0 and int(E3.get( ))>=18 and int(E3.get( ))<=65 and len(E4.get( ))==10 and E4.get( ).isdigit( )==True and '@' in E5.get( ) and '.' in E5.get( ):
              res=tkinter.messagebox.askyesno(message="Please Confirm to add the file")
              if res==True:
                   with open("Blood Donor",'wb') as fil: #will open the file for writing
                           pickle.dump(Rec1,fil)
                           tkinter.messagebox.showinfo(message="Record added")
                           Clear( )

    except ValueError:
        tkinter.messagebox.showerror(message="Invalid Value entered for Age")
         
def RemRecord( ):
     if len(E1.get( ))==0:
        tkinter.messagebox.showinfo(message="Enter the Donor Id in the field to remove the record")
     ClearFrame( )
     try:
        with open("Blood Donor",'rb+') as fil:
            Rec=pickle.load(fil)
            for i in range(0,len(Rec)):
                if Rec[i]["Id"]==E1.get( ):
                    Label(F2,text="%s" % "Record Found",bg="gold",fg="blue", font=("Arial bold",10)).pack( )
                    ch=tkinter.messagebox.askyesno(message="Delete the account")
                    if ch==True:
                        Rec.pop(i)
                        Label(F2,text="%s" % "Record Deleted",bg="gold",fg="blue", font=("Arial bold",10)).pack( )
                    break
            else:
                Label(F2,text="%s" % "Record Not Found",bg="gold",fg="blue", font=("Arial bold",10)).pack( )

            fil.seek(0)
            pickle.dump(Rec,fil)
      
     except FileNotFoundError:
            print(F,"File Doesn't exist",bg="gold",fg="blue", font=("Arial bold",10))
     except KeyError:
            print("Record Not found",bg="gold",fg="blue", font=("Arial bold",10))
     except IndexError:
            print("Record Not found",bg="gold",fg="blue", font=("Arial bold",10))

def Search( ):
    if len(E1.get( ))==0:
        tkinter.messagebox.showinfo(message="Enter the Donor Id in the field to search for the record")
    ClearFrame( )
    try:
        with open("Blood Donor",'rb') as fil:
            Rec=pickle.load(fil)
            for i in range(0,len(Rec)):
                if Rec[i]["Id"]==E1.get( ):
                    Label(F2,text="%s" % "Record Found",bg="gold",fg="blue", font=("Arial bold",20)).pack( )
                    N=Rec[i]
                    E2.delete(0,END)
                    E2.insert(0,N["Name"])
                    E3.delete(0,END)
                    E3.insert(0,N["Age"])
                    E4.delete(0,END)
                    E4.insert(0,N["Mob"])
                    E5.delete(0,END)
                    E5.insert(0,N["Email"])
                    if N["BG"]=="A+":
                        BG.current(0)
                    elif N["BG"]=="O+":
                       BG.current(1)
                    elif N["BG"]=="B+":
                        BG.current(2)
                    elif N["BG"]=="AB+":
                        BG.current(3)
                    elif N["BG"]=="A-":
                        BG.current(4)
                    elif N["BG"]=="O-":
                        BG.current(5)
                    elif N["BG"]=="B-":
                        BG.current(6)
                    elif N["BG"]=="AB-":
                        BG.current(7)
                    break
            else:
                Label(F2,text="%s" % "Record Not Found",bg="gold",fg="blue", font=("Arial bold",10)).pack( )
    except FileNotFoundError:
            print(F,"File Doesn't exist",bg="gold",fg="blue", font=("Arial bold",10))
    except KeyError:
            print("Record Not found",bg="gold",fg="blue", font=("Arial bold",10))
    except IndexError:
            print("Record Not found",bg="gold",fg="blue", font=("Arial bold",10))

def UpdateRec( ):
    if len(E1.get( ))==0:
        tkinter.messagebox.showinfo(message="Click on Search to search and then update")
        Clear( )
        
    try:
        with open("Blood Donor",'rb+') as fil:
            found=-1
            Rec1=pickle.load(fil)
            Rec={ }
            for p in Rec1:
                if E1.get( )==p["Id"]:
                    found=0
                    if len(E2.get( ))<=0:
                        tkinter.messagebox.showerror(message="Name not entered")
                    else:
                        p["Name"]=E2.get( )

                    if int(E3.get( ))<18 or int(E3.get( ))>65:
                        tkinter.messagebox.showerror(message="Valid Age from 18 to 65 only")
                    else:
                        p["Age"]=int(E3.get( ))

                    if len(E4.get( ))!=10 or E4.get( ).isdigit( )==False:
                       tkinter.messagebox.showerror(message="Please enter valid Mobile No")
                    else:
                        p["Mob"]=E4.get( )

                    if '@' not in E5.get( ) or '.' not in E5.get( ):
                        tkinter.messagebox.showerror(message="Enter Valid mail address")
                    else:
                        p["Email"]=E5.get( )

                    p["BG"]=BG.get( )
                    break
            else:
                Label(F2,text="%s" % "Record Not Found",bg="gold",fg="blue", font=("Arial bold",10)).pack( )
                
            if found==0 and len(E1.get( ))>0 and len(E2.get( ))>0 and int(E3.get( ))>=18 and int(E3.get( ))<=65 and len(E4.get( ))==10 and E4.get( ).isdigit( )==True and '@' in E5.get( ) and '.' in E5.get( ):
                res=tkinter.messagebox.askyesno(message="Please Confirm to update the file")
                if res==True:
                    fil.seek(0)
                    pickle.dump(Rec1,fil)
                    Label(F2,text="%s" % "Record Updated",bg="gold",fg="blue", font=("Arial bold",10)).pack( )
                    
    except EOFError:
        print("File doesn't exist",bg="gold",fg="blue", font=("Arial bold",10))
    except FileNotFoundError:
        print(F,"File doesn't exist",bg="gold",fg="blue", font=("Arial bold",10))


def SearchBG( ):
    try:
        with open("Blood Donor",'rb') as fil:
            Rec = pickle.load(fil)
            Clear( )
            Label(F2,text="%s %s %s %s %s %s" % ("         ID |","      NAME |","      AGE |","      MOBILE |","      EMAIL  |","      BLOOD GRP  |"),bg="gold",fg="blue", font=("Arial bold",10)).pack( )
            Label(F2,text="%s" % "-"*125,bg="gold",fg="blue", font=("Arial bold",10)).pack( )
            flag=False
            for i in Rec:
                if i["BG"]==SBG.get( ):
                    Label(F2,text="%s %s %s %s %s %s" % (str(i["Id"])+"  |  ",i["Name"]+"  |  ",str(i["Age"])+"  |  ",str(i["Mob"])+"  |  ",i["Email"]+"  |  ",i["BG"]+"  |  ")).pack( )
                    flag=True
            if flag==False:
                Label(F2,text="%s" % "Currently no donors with required blood group ",bg="gold",fg="blue", font=("Arial bold",10)).pack( )

    except FileNotFoundError:
        Label(F2,text="%s" % "File doesn't exist",bg="gold",fg="blue", font=("Arial bold",10)).pack( )
    except EOFError:
        Label(F2,text="%s" % "File doesn't exist",bg="gold",fg="blue", font=("Arial bold",10)).pack( )

def InfoBlood( ):
    Clear( )
    with open("Blood Type.txt","r") as F:
        info=F.read()
        Label(F2,text=info, font=("Arial bold",10),bg="gold",fg="blue").pack( )

Label(root,text="BLOOD BANK MANAGEMENT",font=("Arial",30,"bold"),border=12,relief=GROOVE,bg="blue",fg="gold").pack( )
root.config(bg="gold")

F1=Frame(root,borderwidth=3,relief="solid",bg="gold")
F1.pack(side="left",expand=True,fill="both")

F2=Frame(root,borderwidth=3,relief="solid",bg="gold")
F2.pack(side="right",expand=True,fill="both")
Label(F2,text="     \"Tears Of A Mother Cannot Save Her Child \nBut YOUR BLOOD CAN\"", font=("Trebuchet",20,"bold"),bg="gold",fg="blue").pack()#grid( row=0,column=0)

img=ImageTk.PhotoImage(Image.open("Background.png"))#,width=675,height=350
label=Label(F2,image=img)
label.pack( )

Label(F1,text="DONOR ID",bg="gold",fg="blue", font=("Arial bold",10)).grid( row=0,column=0)
E1=Entry(F1,bd=4)
E1.grid(row=0,column=1,padx=13,pady=10)

Label(F1,text="DONOR NAME",bg="gold",fg="blue", font=("Arial bold",10)).grid( row=1,column=0)
E2=Entry(F1,bd=4)
E2.grid(row=1,column=1,padx=13,pady=10)

Label(F1,text="AGE",bg="gold",fg="blue", font=("Arial bold",10)).grid( row=2,column=0)
E3=Entry(F1,bd=4)
E3.grid(row=2,column=1,padx=13,pady=10)

Label(F1,text="MOBILE NO",bg="gold",fg="blue", font=("Arial bold",10)).grid( row=3,column=0)
E4=Entry(F1,bd=4)
E4.grid(row=3,column=1,padx=13,pady=10)

Label(F1,text="EMAIL ID",bg="gold",fg="blue", font=("Arial bold",10)).grid( row=4,column=0)
E5=Entry(F1,bd=4)
E5.grid(row=4,column=1,padx=13,pady=10)

Label(F1,text="BLOOD GROUP",bg="gold",fg="blue", font=("Arial bold",10)).grid( row=5,column=0)
BG=ttk.Combobox(F1)
BG['values']=('A+','O+','B+','AB+','A-','O-','B-','AB-')
BG.current(0)
BG.grid(row=5,column=1,padx=13,pady=10)

Label(F1,text="ENTER REQUIRED BLOOD GROUP",bg="gold",fg="blue", font=("Arial bold",10)).grid( row=6,column=1)
SBG=ttk.Combobox(F1)
SBG['values']=('A+','O+','B+','AB+','A-','O-','B-','AB-')
SBG.current(0)
SBG.grid(row=7,column=1,padx=13,pady=10)

Add=Button(F1,text="ADD DONOR",command=AddRec,padx=13,pady=10,fg="gold",bg="blue", font=("Arial bold",10))
Add.grid(row=20,column=0,sticky=NSEW,padx=13,pady=10)

Del=Button(F1,text="DELETE DONOR",command=RemRecord,padx=13,pady=10,fg="gold",bg="blue", font=("Arial bold",10))
Del.config(relief=RAISED)
Del.grid(row=20,column=1,sticky=NSEW,padx=13,pady=10)

Upd=Button(F1,text="UPDATE DONOR",command=UpdateRec,padx=13,pady=10,fg="gold",bg="blue", font=("Arial bold",10))
Upd.grid(row=20,column=2,sticky=NSEW,padx=13,pady=10)

Ser=Button(F1,text="SEARCH DONOR",command=Search,padx=13,pady=10,fg="gold",bg="blue", font=("Arial bold",10))
Ser.grid(row=21,column=0,sticky=NSEW,padx=13,pady=10)

View=Button(F1,text="VIEW ALL",command=ViewAll,padx=13,pady=10,fg="gold",bg="blue", font=("Arial bold",10))
View.grid(row=21,column=1,sticky=NSEW,padx=13,pady=10)

Clr=Button(F1,text="CLEAR",command=Clear,padx=13,pady=10,fg="gold",bg="blue", font=("Arial bold",10))
Clr.grid(row=21,column=2,sticky=NSEW,padx=13,pady=10)

Exit=Button(F1,text="EXIT",command=Exit1,padx=13,pady=10,fg="gold",bg="blue", font=("Arial bold",10))
Exit.grid(row=22,column=0,sticky=NSEW,padx=13,pady=10)

SerBG=Button(F1,text="SEARCH BLOOD GRP",command=SearchBG,padx=13,pady=10,fg="gold",bg="blue", font=("Arial bold",10))
SerBG.grid(row=22,column=1,sticky=NSEW,padx=13,pady=10)

info=Button(F1,text="INFO ON BLOOD",command=InfoBlood,padx=13,pady=10,fg="gold",bg="blue", font=("Arial bold",10))
info.grid(row=22,column=2,sticky=NSEW,padx=13,pady=10)
'''
root=Canvas(width=400,height=400)
root.pack(expand=YES,fill=BOTH)

image=ImageTk.PhotoImage(file="old bg.jpg")
root.create_image(10,10,image=image,anchor=NW)
'''
'''same=True
n=0.25 # Adding a background image
background_image =Image.open("Blood Heart.jpeg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(617,279,image = img)
Canvas1.config(bg="light pink",width = newImageSizeWidth , height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)'''
