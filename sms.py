#Nguyễn Đình Tuấn Long - 20216941
from tkinter import *
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas as pd
# Kết nối cơ sở dữ liệu
def connect_database():
    def connect():
        global mycursor,log
        try:
            log=pymysql.connect(host='localhost',user='root',password='tuanlong2003')
            mycursor=log.cursor()
        except:
            messagebox.showerror('Lỗi','Thông tin nhập vào không đúng',parent=connectWindow)
            return
        try:
            query='create database quanlysinhvien'
            mycursor.execute(query)
            query='use quanlysinhvien'
            mycursor.execute(query)
            query='create table sinh_vien(MaSV INT PRIMARY KEY,HoTen VARCHAR(255), KhoaHoc INT, KhoaVien VARCHAR(50), Lop VARCHAR(50), DiemTichLuy FLOAT)'
            mycursor.execute(query)
        except:
            query='use quanlysinhvien'
            mycursor.execute(query)
        messagebox.showinfo('Thành công', 'Đã kết nối cơ sở dữ liệu thành công', parent=connectWindow)
        connectWindow.destroy()


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('550x300+730+230')
    connectWindow.title('Kết nối database')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('Helvetica',20))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('Helvetica',20),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('Helvetica',20))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('Helvetica',20), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('Helvetica',20))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('Helvetica',20),show='*', bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='Kết nối database',command=connect)
    connectButton.grid(row=3,columnspan=2)
#Chức năng trong chương trình
#Thêm thông tin sinh viên
def add_student():
    def add_data():
        if idEntry.get() =='' or nameEntry.get() =='' or instiEntry.get() == '' or KEntry.get() =='' or classEntry.get() =='' or gpaEntry.get() =='':
            messagebox.showerror('Lỗi','Vui lòng nhập đủ thông tin', parent = add_window)
        else:
            try:
                int(idEntry.get())
                int(KEntry.get())
                float(gpaEntry.get())
            except ValueError:
                messagebox.showerror('Lỗi', 'Vui lòng nhập đúng định dạng', parent=add_window)
                return
            query = 'insert into sinh_vien values (%s, %s, %s, %s, %s, %s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),KEntry.get(),instiEntry.get(),classEntry.get(),gpaEntry.get()))
            log.commit()
            result = messagebox.askyesno('Thêm dữ liệu thành công', 'Bạn có muốn xóa màn hình',parent = add_window)
            print(result)
            if result:
                idEntry.delete(0, END)
                instiEntry.delete(0, END)
                KEntry.delete(0, END)
                classEntry.delete(0, END)
                nameEntry.delete(0, END)
                gpaEntry.delete(0, END)
            else:
                pass
            
            query = 'select * from sinh_vien'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            print(fetched_data)
            student_table.delete(*student_table.get_children())
            for data in fetched_data:
                datalist = list(data)
                student_table.insert('',END,values = datalist)
            
    add_window=Toplevel()
    add_window.resizable(0,0)
    add_window.grab_set()
    idLabel=Label(add_window,text="Mã số sinh viên", font=('times new roman',20))
    idLabel.grid(row=0,column=0,padx=30,pady=15)
    idEntry=Entry(add_window,font=('roman',15),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)
    
    nameLabel=Label(add_window,text="Họ và tên sinh viên", font=('times new roman',20))
    nameLabel.grid(row=1,column=0,padx=30,pady=15)
    nameEntry=Entry(add_window,font=('roman',15),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)
    
    KLabel=Label(add_window,text="Khóa", font=('times new roman',20))
    KLabel.grid(row=3,column=0,padx=30,pady=15)
    KEntry=Entry(add_window,font=('roman',15),width=24)
    KEntry.grid(row=3,column=1,pady=15,padx=10)
    
    instiLabel=Label(add_window,text="Viện/Trường", font=('times new roman',20))
    instiLabel.grid(row=4,column=0,padx=30,pady=15)
    instiEntry=Entry(add_window,font=('roman',15),width=24)
    instiEntry.grid(row=4,column=1,pady=15,padx=10)
    
    classLabel=Label(add_window,text="Lớp", font=('times new roman',20))
    classLabel.grid(row=5,column=0,padx=30,pady=15)
    classEntry=Entry(add_window,font=('roman',15),width=24)
    classEntry.grid(row=5,column=1,pady=15,padx=10)
    
    gpaLabel=Label(add_window,text="Điểm tích lũy", font=('times new roman',20))
    gpaLabel.grid(row=6,column=0,padx=30,pady=15)
    gpaEntry=Entry(add_window,font=('roman',15),width=24)
    gpaEntry.grid(row=6,column=1,pady=15,padx=10)
    
    add_student_button = ttk.Button(add_window, text="Thêm sinh viên",widt=25,command=add_data)
    add_student_button.grid(row=7,columnspan=2,pady=15)

#Cập nhật thông tin sinh viên
def update_student():
    def update_data():
        query='update sinh_vien set Hoten=%s,Khoahoc=%s,KhoaVien=%s,Lop=%s,DiemTichLuy=%s where MaSV = %s'
        mycursor.execute(query,(nameEntry.get(),KEntry.get(),instiEntry.get(),classEntry.get(),gpaEntry.get(),idEntry.get()))
        log.commit()
        messagebox.showinfo('OK','Cập nhật dữ liệu thành công')
        update_window.destroy()
        print_student()
    update_window=Toplevel()
    update_window.resizable(0,0)
    update_window.title('Cập nhật thông tin sinh viên')
    update_window.grab_set()
    idLabel=Label(update_window,text="Mã số sinh viên", font=('times new roman',20))
    idLabel.grid(row=0,column=0,padx=30,pady=15)
    idEntry=Entry(update_window,font=('roman',15),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)
    
    nameLabel=Label(update_window,text="Họ và tên sinh viên", font=('times new roman',20))
    nameLabel.grid(row=1,column=0,padx=30,pady=15)
    nameEntry=Entry(update_window,font=('roman',15),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)
    
    KLabel=Label(update_window,text="Khóa", font=('times new roman',20))
    KLabel.grid(row=3,column=0,padx=30,pady=15)
    KEntry=Entry(update_window,font=('roman',15),width=24)
    KEntry.grid(row=3,column=1,pady=15,padx=10)
    
    instiLabel=Label(update_window,text="Viện/Trường", font=('times new roman',20))
    instiLabel.grid(row=4,column=0,padx=30,pady=15)
    instiEntry=Entry(update_window,font=('roman',15),width=24)
    instiEntry.grid(row=4,column=1,pady=15,padx=10)
    
    classLabel=Label(update_window,text="Lớp", font=('times new roman',20))
    classLabel.grid(row=5,column=0,padx=30,pady=15)
    classEntry=Entry(update_window,font=('roman',15),width=24)
    classEntry.grid(row=5,column=1,pady=15,padx=10)
    
    gpaLabel=Label(update_window,text="Điểm tích lũy", font=('times new roman',20))
    gpaLabel.grid(row=6,column=0,padx=30,pady=15)
    gpaEntry=Entry(update_window,font=('roman',15),width=24)
    gpaEntry.grid(row=6,column=1,pady=15,padx=10)
    
    update_student_button = ttk.Button(update_window, text="Cập nhật",widt=25,command=update_data)
    update_student_button.grid(row=7,columnspan=2,pady=15)

    indexing = student_table.focus()
    content = student_table.item(indexing)
    listdata = content['values']
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0,listdata[1])
    KEntry.insert(0,listdata[2])
    instiEntry.insert(0,listdata[3])
    classEntry.insert(0,listdata[4])
    gpaEntry.insert(0,listdata[5])
#Xóa sinh viên
def delete_student():
    def xoa_student():
        if deleteEntry.get() == '' or delete1Entry.get() == '':
            messagebox.showerror('Lỗi','Cần nhập đầy đủ thông tin', parent = new_window)
        else:
                name_delete = deleteEntry.get()
                id_delete = delete1Entry.get()
                query = 'select * from sinh_vien where MaSV = %s and HoTen = %s'
                mycursor.execute(query, (id_delete, name_delete))
                fetched_data = mycursor.fetchall()
                student_table.delete(*student_table.get_children())
                if (len(fetched_data) == 0):
                        messagebox.showerror('Lỗi', 'Thông tin sinh viên không có trong db')
                        return
                else:            
                    query = 'delete from sinh_vien where MaSV = %s and HoTen = %s'
                    mycursor.execute(query,(id_delete,name_delete))
                    log.commit()
                    messagebox.showinfo('Xóa thành công',f'Sinh viên {name_delete} đã được xóa')
                    query = 'select * from sinh_vien'
                    mycursor.execute(query)
                    messagebox.showinfo('OK','Thực hiện xóa thông tin sinh viên thành công')
                    fetched_data = mycursor.fetchall()
                    student_table.delete(*student_table.get_children())
                    for data in fetched_data:
                        student_table.insert('',END, values=data)
        new_window.destroy()
    new_window = Toplevel()
    new_window.geometry('600x150+730+230')
    deletelabel = Label(new_window, text = 'Nhập tên sinh viên cần xóa', font=('Helvetica',15))
    deletelabel.grid(column=0,row=0,padx=10,pady=10)
    deletelabel1 = Label(new_window, text = 'Nhập mã số sinh viên cần xóa', font=('Helvetica',15))
    deletelabel1.grid(column=0,row=1,padx=10,pady=10)
    deleteEntry = Entry(new_window, font=('Helvetica',15))
    deleteEntry.grid(column=1,row=0,padx=7)
    delete1Entry = Entry(new_window, font=('Helvetica',15))
    delete1Entry.grid(column=1,row=1,padx=7,pady=10)
    deletebutton = ttk.Button(new_window, text='Xóa sinh viên',width=15,command=xoa_student)
    deletebutton.grid(row=2,column=0,columnspan=2,pady=10)


#In danh sách sinh viên theo lớp
def list_student():
    def student_by_list():
        if askEntry.get()=='':
            messagebox.showerror('Lỗi','Bạn cần phải nhập đúng tên lớp cần truy xuất')
        else:    
            classname = askEntry.get()
            query = 'select * from sinh_vien where Lop = (%s)'
            mycursor.execute(query, classname)
            fetched_data = mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for data in fetched_data:
                student_table.insert('',END, values=data)
            ask.destroy()
        pass
    ask = Toplevel()
    ask.geometry('350x150+730+230')
    ask.grab_set()
    ask.resizable(0,0)
    asklabel = Label(ask, text = 'Nhập tên lớp học bạn muốn truy vấn', 
    font=('Helvetica',15))
    asklabel.grid(column=0,row=0,padx=10,pady=10)
    askEntry = Entry(ask, font=('Helvetica',15))
    classname = askEntry.get()
    askEntry.grid(column=0,row=1)
    askbutton = ttk.Button(ask, text='In danh sách',width=15,command=student_by_list)
    askbutton.grid(row=2,column=0,columnspan=2,pady=10)

#In danh sách tất cả các sinh viên
def print_student():
    query = 'select * from sinh_vien'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('',END, values=data)
            
#Tìm kiếm sinh viên
def search_student():
    def search_by_name_and_id():
        if searchEntry.get() == '' or search1Entry.get() == '':
            messagebox.showerror('Lỗi','Bạn cần phải nhập đầy đủ các thông tin')
        else:    
            name_student = searchEntry.get()
            id_student = search1Entry.get()
            query = 'select * from sinh_vien where Hoten = (%s) and MaSV like (%s)'
            mycursor.execute(query, (name_student, id_student))
            fetched_data = mycursor.fetchall()
            if len(fetched_data) == 0:
                messagebox.showinfo('Thông báo', 'Không tìm thấy sinh viên')
            else:
                student_table.delete(*student_table.get_children())
                for data in fetched_data:
                    student_table.insert('', END, values=data)
                search.destroy()
            pass
    search = Toplevel()
    search.geometry('500x150+730+230')
    search.grab_set()
    search.resizable(0,0)
    searchlabel = Label(search, text = 'Nhập tên sinh viên cần tìm', font=('Helvetica',15))
    searchlabel.grid(column=0,row=0,padx=10,pady=10)
    searchlabel1 = Label(search, text = 'Nhập mã số sinh viên', font=('Helvetica',15))
    searchlabel1.grid(column=0,row=1,padx=10,pady=10)
    searchEntry = Entry(search, font=('Helvetica',15))
    searchEntry.grid(column=1,row=0,padx=7)
    search1Entry = Entry(search, font=('Helvetica',15))
    search1Entry.grid(column=1,row=1,padx=7,pady=10)
    name_student = searchEntry.get()
    id_student = search1Entry.get()
    searchbutton = ttk.Button(search, text='Tìm sinh viên',width=15,command=search_by_name_and_id)
    searchbutton.grid(row=2,column=0,columnspan=2,pady=10)
    
    
# Sắp xếp sinh viên theo điểm
def sort_student():
    query = 'select * from sinh_vien order by DiemTichLuy DESC'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('',END, values=data)
        

#Phân loại sinh viên
def category():
    another_window = Toplevel()
    another_window.geometry('500x500+40+40')
    another_window.resizable(0,0)
    another_window.grab_set()
    cate_table = ttk.Treeview(another_window, columns=('Mã số sinh viên',
    'Họ và tên','Xếp loại'),yscrollcommand=scrollbary.set)
    cate_table.pack(fill=BOTH,expand=1)
    scrollbary.config(command=cate_table.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    cate_table.heading('Mã số sinh viên', text = 'Mã số sinh viên')
    cate_table.heading('Họ và tên', text = 'Họ và tên')
    cate_table.heading('Xếp loại', text = 'Xếp loại')
    cate_table.configure(show='headings')   
    try:
        procedure_sql = '''
        CREATE PROCEDURE Phanloaisinhvien()
        BEGIN
            SELECT 
                HoTen,
                DiemTichLuy,
                CASE 
            WHEN DiemTichLuy > 3.6 THEN 'Xuất Sắc'
            WHEN DiemTichLuy >= 3.2 AND DiemTichLuy <= 3.6 THEN 'Giỏi'
            WHEN DiemTichLuy >= 2.5 AND DiemTichLuy < 3.2 THEN 'Khá'
            ELSE 'Trung Bình'
        END AS XepLoai
        FROM sinh_vien;
        END;
        '''
        query = 'call Phanloaisinhvien()'
        mycursor.execute(procedure_sql)
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        cate_table.delete(*cate_table.get_children())
        for data in fetched_data:
                cate_table.insert('',END, values=data)
    except:
        query = 'call Phanloaisinhvien()'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        cate_table.delete(*cate_table.get_children())
        for data in fetched_data:
                cate_table.insert('',END, values=data)
            

#Xuất file thông tin
def export_student():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = student_table.get_children()
    newlist = []
    for index in indexing:
        content = student_table.item(index)
        datalist = content['values']
        newlist.append(datalist)
    table = pd.DataFrame(newlist, columns=['Mã số sinh viên','Họ và tên',
    'Khóa','Viện Trường','Lớp','Điểm tích lũy'])
    table.to_csv(url, index=False, encoding='utf-8-sig')
    messagebox.showinfo('Đã xuất dữ liệu thành công')

# Thoát khỏi chương trình  
def exit_student():
    result = messagebox.askyesno('Thoát','Bạn có muốn thoát chương trình không')
    if result:
        root.destroy()
    else:
        pass

#GUI Part
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('elegance')
root.geometry('1560x770+20+20')
root.resizable(0,0)
root.title("Quản lý sinh viên")

#Định nghĩ chi tiết đồ họa trong cửa sổ chương trình
Text = ttk.Label(root,text="Phần mềm quản lý sinh viên",font=(('arial'),26))
Text.place(x=450,y=10)
dev_label = Label(root, text ="Nguyễn Đình Tuấn Long",activebackground='white')
dev_label.configure(foreground='gray')
dev_label.place(x=40,y=25)

connectButton=ttk.Button(root,text='Import dữ liệu',width=50,command=connect_database)
connectButton.place(x=1120,y=15)

leftFrame=Frame(root)
leftFrame.place(x=15,y=65,width=400,height=700)

logo_image=PhotoImage(file='icons8-student-48.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

add_student_button=ttk.Button(leftFrame,text='Thêm sinh viên',width=30,command=add_student)
add_student_button.grid(row=1,column=0,pady=20)

delete_student_button=ttk.Button(leftFrame,text='Xóa sinh viên',width=30,command=delete_student)
delete_student_button.grid(row=2,column=0,pady=20)

update_student_button=ttk.Button(leftFrame,text='Cập nhật thông tin sinh viên',width=30,command=update_student)
update_student_button.grid(row=3,column=0,pady=20)

print_student_button=ttk.Button(leftFrame,text='In tất cả sinh viên',width=30,command=print_student)
print_student_button.grid(row=4,column=0,pady=20)

search_student_button=ttk.Button(leftFrame,text='Tìm kiếm sinh viên',width=30,command=search_student)
search_student_button.grid(row=5,column=0,pady=20)

sort_student_button=ttk.Button(leftFrame,text='Sắp xếp sinh viên theo điểm',width=30,command=sort_student)
sort_student_button.grid(row=6,column=0,pady=20)

category_button=ttk.Button(leftFrame,text='Phân loại sinh viên',width=30,command=category)
category_button.grid(row=7,column=0,pady=20)

export_button=ttk.Button(leftFrame,text='Xuất dữ liệu',width=30,command=export_student)
export_button.grid(row=8,column=0,pady=20)

exit_button=ttk.Button(leftFrame,text='Thoát',width=30,command=exit_student)
exit_button.grid(row=9,column=0,pady=20)

rightframe = Frame(root)
rightframe.place(x=250,y=77,width=1300,height=650)

scrollbarx= Scrollbar(rightframe, orient=HORIZONTAL)  
scrollbary= Scrollbar(root,orient=VERTICAL)

student_table = ttk.Treeview(rightframe, columns=('Mã số sinh viên','Họ và tên','Khóa','Viện/trường','Lớp',
'Điểm tích lũy'), yscrollcommand=scrollbary.set)
student_table.pack(fill=BOTH,expand=1)

# scrollbarx.config(command=student_table.xview)
scrollbary.config(command=student_table.yview)

# scrollbarx.pack(side=BOTTOM, fill=X)
scrollbary.pack(side=RIGHT, fill=Y)

student_table.heading('Mã số sinh viên', text='Mã số sinh viên')
student_table.heading('Họ và tên', text='Họ và tên')
student_table.heading('Khóa', text='Khóa')
student_table.heading('Viện/trường', text='Viện/trường')
student_table.heading('Lớp', text='Lớp')
student_table.heading('Điểm tích lũy', text='Điểm tích lũy')
student_table.configure(show='headings')

student_table.config(show='headings')

root.mainloop()

