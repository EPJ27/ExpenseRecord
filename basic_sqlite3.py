#basic sqlite3.py
import sqlite3

#database
conn = sqlite3.connect('expense.sqlite3')

# ตัวดำเนินการ
c = conn.cursor()

# create table
#FEILD = ['id(transectionid)','วันเวลา(stamp)','รายการ(title)','ค่าใช้จ่าย(expense)','จำนวน(quantity)','รวม(total)']
c.execute(""" CREATE TABLE IF NOT EXISTS expenselite (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				transectionid TEXT,
				stamp DATETIME,
				title TEXT,
				expense REAL,
				quantity INTEGER,
				total REAL
			)""")

def insert_expense(transctionid,stamp,title,expense,quantity,total):
	ID = None
	with conn:
		c.execute(""" INSERT INTO expenselite VALUES(?,?,?,?,?,?,?)""",
				(ID,transctionid,stamp,title,expense,quantity,total))
	conn.commit()  # การบันทึกข้อมูลลงในฐานข้อมูล 
	print('Insert Success')

def show_expense():
	with conn:
		c.execute("SELECT * FROM expenselite")
		expense = c.fetchall()  # คำสั่งดึงข้อมูล
		print(expense)
	return expense

show_expense()


#insert_expense('2021156454545','2021-09-05','ข้าวสาร',45,2,90)

print('success')