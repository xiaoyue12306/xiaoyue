import xlrd,xlwt
from xlutils.copy import copy
excel=xlrd.open_workbook(r'C:\Users\xyy\Desktop\xy\Python\venv\vlookup\Stock Check.xls')
sheet1=excel.sheets()[0]
sheet2=excel.sheets()[1]
sheet3=excel.sheets()[2]
new_excel=copy(excel)



newex=new_excel.get_sheet(2)
print(newex)
# 获取表一单元格的值
sheet3_h=1
rest_count=[]
for sheet1_h in range (1,151):


    cell_sap_value=int(sheet1.cell(sheet1_h,0).value)
    # 获取表二单元格的值

    for sheet2_h in range(1,16904):
        # 表二sap的值
        cell_wl_value=int(sheet2.cell(sheet2_h,0).value)
        # wl_list.append(cell_wl_value)


        # 表一表二sap对应
        if cell_sap_value==cell_wl_value :


            #获取工厂
            factory = int(sheet2.cell(sheet2_h, 2).value)
            # 获取库存
            rest=int(sheet2.cell(sheet2_h,5).value)
            rest_count.append(rest)
            if  factory==int(5050):
                newex.write(sheet3_h,1,factory)
                newex.write(sheet3_h,0,cell_sap_value)
                newex.write(sheet3_h,2,rest)
                sheet3_h+=1
            elif factory == int(5250):
                newex.write(sheet3_h, 1, factory)
                newex.write(sheet3_h, 0, cell_sap_value)
                newex.write(sheet3_h, 2, rest)
                sheet3_h += 1

            elif factory == int(5251):
                newex.write(sheet3_h, 1, factory)
                newex.write(sheet3_h, 0, cell_sap_value)
                newex.write(sheet3_h, 2, rest)
                sheet3_h += 1

list1=[]
list2=[]
for sheet1_h in range (1,151):


    cell_sap_value2=int(sheet1.cell(sheet1_h,0).value)
    list1.append(cell_sap_value2)
    # 获取表二单元格的值


for sheet2_h in range(1,16904):
    # 表二sap的值
    cell_wl_value=int(sheet2.cell(sheet2_h,0).value)
    list2.append(cell_wl_value)

nul=[x for x in list1 if x not in list2]
for nul in nul:
    newex.write(sheet3_h, 1, 'sheet2无此数据')
    newex.write(sheet3_h, 0, nul)
    newex.write(sheet3_h, 2, 'sheet2无此数据')
    sheet3_h += 1

new_excel.save('xgx_no_factory2.xls')