import sqlite3
import xlrd
import xlwt 
from xlwt import Workbook 



db = 'db.sqlite3'
con = sqlite3.connect(db)
cur = con.cursor()
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1') 

col_head = (u"الوصف" ,
			u"المعيار",
			u"وزن المعيار",
			u"مجموعة الصنف",
			u"الطاقة")
data = cur.execute("""SELECT unit.description, unit.home_standrd, unit.home_standrd_wieght,unit.enerygy, grop.arabic_name 
					FROM  foodconf_unit AS unit INNER JOIN foodconf_itemgroup AS grop
					ON unit.item_group_id =grop.id""")


for  i in range(0,len(col_head)):
	sheet1.write(0,i,col_head[i])

n = 1 
for e in data :
	sheet1.write(n,0,e[0])
	sheet1.write(n,1,e[1])
	sheet1.write(n,2,e[2])
	sheet1.write(n,3,e[4])
	sheet1.write(n,4,e[3])
	n+=1

wb.save('Units.xls') 
# b = cur.execute("SELECT * FROM foodconf_unit")
# print(b)
# for i in b :print(i)
# b.fetchall()
# print(data)
# for i in data:
# 	print(i)
