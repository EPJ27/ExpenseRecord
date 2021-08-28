from tkinter import *
from tkinter import ttk,messagebox
import csv
from datetime import datetime

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย v1.0 by EakTo8')
GUI.geometry('600x700+800+60')

# B1 = Button(GUI, text='Hello')
# B1.pack(ipadx=50,ipady=10)  # .pack ติดปุ่มกับ GUI

##################################
menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label="import csv")
filemenu.add_command(label="export csv")

# Help
def About():
    print('About Menu')
    messagebox.showinfo('About','สวัสดีครับ โปรแกรมนี้คือโปรแกรมบันทึกรายการซื้อสินค้า\nสนใจติดต่อที่ คุณเอก Tel. 0932359294')

helpmenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label="About",command=About)

##################################

# (3)----------  Tab -----------------#
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

icon_t1 = PhotoImage(file='asset/img/T1_expanse.png')
icon_t2 = PhotoImage(file='asset/img/T2_price.png')

Tab.add(T1,text=f'{"Add Expense":^{30}}',image=icon_t1,compound='top') #f string เพื่อ balance tab
Tab.add(T2,text=f'{"List view":^{30}}',image=icon_t2,compound='top') # .subsample(2) = ย่อรูป

F1 = Frame(T1)
F1.pack()

days = {'Mon':'วันจันทร์',
        'Tue':'วันอังคาร',
        'Wen':'วันพุธ',
        'Thu':'วันพฤหัสบดี',
        'Fri':'วันศุกร์',
        'Sat':'วันเสาร์',
        'Sun':'วันอาทิตย์'}

#----------  Function save -----------------#
def Save(event=None):  #line 85
    expense = v_expense.get()
    price = v_price.get()
    qty = v_qty.get()

    if expense == '':
        print('No data')
        messagebox.showinfo('Error','กรุณากรอกข้อมูลสินค้า')
        return
    elif price == '':
        messagebox.showinfo('Error','กรุณากรอกราคาสินค้า')
        return
    elif qty == '':
        qty = 1

    try:
        total =  float(price) * float(qty)
        # .get() ดึงค่ามาจาก v_expence = StringVar()
        print('รายการ: {} ราคา: {} บาท'.format(expense,price))
        print('จำนวน: {} ราคารวม: {} บาท'.format(qty,total))
        print('------')
        text = 'รายการ: {} ราคา: {} บาท\n'.format(expense,price)
        text = text + 'จำนวน: {} ชิ้น   ราคารวม: {} บาท'.format(qty,total)
        v_result.set(text)
        v_expense.set('')  # Reset entry ให้เป็นค่าว่าง
        v_price.set('')
        v_qty.set('')

        # บันทึกข้อมูลลง CSV อย่าลืม import csv
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('savedata.csv','a',encoding='utf-8',newline='') as f:
            # with สั่งเปิดไฟล์ แล้วปิดอัตโนมัติ
            # 'a'  การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
            # newline=''   --> ทำให้ไม่มีบรรทัดว่าง
            fw = csv.writer(f) # สร้างฟังก์ชันบันทึกข้อมูล
            data = [expense,price,qty,total,dt]
            fw.writerow(data)
        # ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
        E1.focus()
        update_table()
    except:
        print('ERROR')
        messagebox.showwarning('Error','กรุณากรอข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        # v_expense.set('')  # Reset entry ให้เป็นค่าว่าง
        v_price.set('')
        v_qty.set('')
    

# ทำให้สามารถกดenterได้
GUI.bind('<Return>',Save) # ต้องเพิ่ม def Save(event=None) ด้วย


FONT1 = (None,20)  # None เปลี่ยนเป็น 'Augsana '

#---------Img---------
img_icon = PhotoImage(file='asset/img/Icon_F1.png')
main_icon = ttk.Label(F1,image=img_icon)
main_icon.pack()

# (1) ----------  Tab -----------------#
#---------text---------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()
# StringVar() ตัวแปลพิเศษสำหรับเก็บข้อมมูฃใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()

#---------text/---------
L2 = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
# StringVar() ตัวแปลพิเศษสำหรับเก็บข้อมมูฃใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()

#---------text/---------
L3 = ttk.Label(F1,text='จำนวน',font=FONT1).pack()
v_qty = StringVar()
# StringVar() ตัวแปลพิเศษสำหรับเก็บข้อมมูฃใน GUI
E3 = ttk.Entry(F1,textvariable=v_qty,font=FONT1)
E3.pack()
# ---------------

# (2)----------  Btn Save -----------------#
icon_b1 = PhotoImage(file='asset/img/b1_save.png')

B2 = ttk.Button(F1, text=f'{"save":>{10}}',image=icon_b1,compound='left',command=Save)
B2.pack(ipadx=50,ipady=10,pady=20)

v_result = StringVar()
v_result.set('------ผลลัพธ์------')
result = ttk.Label(F1,textvariable=v_result,font=FONT1,foreground='green')
result.pack(pady=20)

######################## Tab2 #####################

def read_csv():
    with open('savedata.csv',newline='',encoding='utf-8') as f: # with เพื่อเปิดแล้วปิด
        fr = csv.reader(f)
        data = list(fr)
    return data
        # print(data)
        # # print(data[0][1])
        # for d in data:
        #     print(d)

## table
L = ttk.Label(T2,text='ตารางผลลัพท์ทั้งหมด',font=FONT1).pack(pady=20)

header = ['รายการ','ค่าใช้จ่าย','จำนวน','รวม','วันเวลา']
tv_csv = ttk.Treeview(T2,column=header,show='headings',height=10)
tv_csv.pack()

#-----------------------
#medthod 3
for h in header:
    tv_csv.heading(h,text=h)

# #medthod 2
# for i in range(len(header)):
#     tv_csv.heading(header[i],text=header[i])

#medthod 1
# tv_csv.heading(header[0],text=header[0])
# tv_csv.heading(header[1],text=header[1])
# tv_csv.heading(header[2],text=header[2])
# tv_csv.heading(header[3],text=header[4])
#-----------------------

headerwidth = [170,80,80,80,120]
for h,w in zip(header,headerwidth):
    tv_csv.column(h,width  = w)
# tv_csv.column('วันเวลา',width=10)

def update_table():
    tv_csv.delete(*tv_csv.get_children())
    data = read_csv()
    for d in data:
        tv_csv.insert('',0,value=d)

update_table()


GUI.mainloop()
