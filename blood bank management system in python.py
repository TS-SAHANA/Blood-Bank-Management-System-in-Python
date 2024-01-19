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
                    Label(F2,text="%s %s %s %s %s %s" % (str(i["Id"])+"  |  ",i["Name"]+"  |  ",str(i["Age"])+"  |  ",str(i["Mob"])+"  |  ",i["Email"]+"  |  ",i["BG"]+"  |  "),font=("Arial bold",10),bg="gold",fg="blue").pack( )
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
