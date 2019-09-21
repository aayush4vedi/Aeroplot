import openpyxl 

text = open('flights.txt')
text.seek(0)

wb = openpyxl.load_workbook('flights.xlsx')
sheet = wb.active
sheet.cell(row = 1, column = 1).value = "ID"
sheet.cell(row = 1, column = 2).value = "Date"
sheet.cell(row = 1, column = 3).value = "Day"
sheet.cell(row = 1, column = 4).value = "Day Type"
sheet.cell(row = 1, column = 5).value = "Flight Number"
sheet.cell(row = 1, column = 6).value = "From"
sheet.cell(row = 1, column = 7).value = "To"
sheet.cell(row = 1, column = 8).value = "Dep Time"

r = 2
for t in text.readlines()[2:]:
    t = t.split("|")
    sheet.cell(row = r, column = 1).value = t[1].strip()
    sheet.cell(row = r, column = 2).value = t[2].strip()
    sheet.cell(row = r, column = 3).value = t[3].strip()
    sheet.cell(row = r, column = 4).value = t[4].strip()
    sheet.cell(row = r, column = 5).value = t[5].strip()
    sheet.cell(row = r, column = 6).value = t[6].strip()
    sheet.cell(row = r, column = 7).value = t[7].strip()
    sheet.cell(row = r, column = 8).value = t[8].strip()
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