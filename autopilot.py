import openpyxl 

text = open('flights.txt')
text.seek(0)

wb = openpyxl.load_workbook('flights.xlsx')
sheet = wb.active
headers = ["ID","Date","Day","Day Type","Flight Number","From","To","Dep Time"]
for i in range(1,9):
    sheet.cell(row = 1, column = i).value = headers[i-1]

r = 2
for t in text.readlines()[2:]:
    t = t.split("|")
    for j in range(1,9):
        sheet.cell(row = r, column = j).value = t[j].strip()
    r += 1

wb.save('flights.xlsx')

#clense the old db
db = openpyxl.load_workbook('db.xlsx')
sheet = db.active

for i in range(1,sheet.max_row+1):
    for j in range(1,sheet.max_column+1):
        sheet.cell(row = i, column = j).value =""

#resetting the headers
sheet.cell(row = 1, column = 1).value = "TimeStamp"
for i in range(2,66):
        sheet.cell(row = 1, column = i).value = "f" + str(i-1)
db.save('db.xlsx')