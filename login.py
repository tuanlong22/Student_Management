#Nguyễn Đình Tuấn Long - 20216941
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Phần mềm quản lý sinh viên','Vui lòng nhập đầy đủ thông tin')
    elif usernameEntry.get()=='Tuanlong' and passwordEntry.get()=='1234567':
        messagebox.showinfo('Phần mềm quản lý sinh viên','Đăng nhập thành công')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Phần mềm quản lý sinh viên','Tài khoản không hợp lệ')

window=Tk()
window.geometry('470x440+0+0')
window.resizable(False,False)
window.configure(bg='#b3afaf')
window.title('Phần mềm quản lý sinh viên')
icon_photo = PhotoImage(file = 'user.png')
window.iconphoto(False,icon_photo)

loginFrame=Frame(window,bg='white')
loginFrame.place(x=30,y=95,width=400,height=460)

logoImage=PhotoImage(file='title1.png')

logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

author_frame=Frame(window,bg='#f2f2f2')
author_frame.place(x=15,y=20,width=445,height=70)

Text = Label(author_frame,text="Phát triển bởi Nguyễn Đình Tuấn Long - 20216941",font=('Helvetica',15))
Text.grid(row=0,column=0)

Text1 = Label(author_frame,text="Phần mềm quản lý sinh viên",font=('Helvetica',15))
Text1.grid(row=1,column=0)


# logoLabel=Label(loginFrame)
# logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
# # usernameImage=PhotoImage(file='Education_(193).png')
usernameLabel=Label(loginFrame,text='Tên đăng nhập',font=('Arial',17),bg='#f2f2f2')
usernameLabel.grid(row=1,column=0,pady=10)

usernameEntry=Entry(loginFrame,font=('Arial',15),bd=3)
usernameEntry.grid(row=1,column=1,pady=10)

passwordLabel=Label(loginFrame,text='Mật khẩu',font=('Arial',17),bg='#f2f2f2')
passwordLabel.grid(row=2,column=0,pady=10)

passwordEntry=Entry(loginFrame,font=('Helvetica',15),bd=3,show="*")
passwordEntry.grid(row=2,column=1,pady=10)

loginButton=Button(loginFrame,text='Đăng nhập',font=('Helvetica',15),width=10,command=login, bg='blue')
loginButton.grid(row=3,column=0,pady=10,columnspan=2)
window.mainloop()