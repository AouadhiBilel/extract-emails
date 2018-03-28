import xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Emails")

filepath = 'results.txt'
with open(filepath,"r") as f:
    for cnt,line in enumerate(f):
        print("Now writing site: "+ line)
        sheet.write(cnt,1, line)
        print("done writing site: "+ line)

workbook.save('excel_emails.xls')
