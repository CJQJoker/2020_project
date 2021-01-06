import xlrd
#打开xls文件
ad_wb = xlrd.open_workbook("data_2.xls")
#获取第一个目标表单
sheet_0 = ad_wb.sheet_by_index(0)
#生成存有所有通知正文的txt
for i in range(sheet_0.nrows):
    with open("all-notice.txt","a", encoding="utf-8") as f:
        f.write(sheet_0.cell_value(i,3))
        f.write('\n')
