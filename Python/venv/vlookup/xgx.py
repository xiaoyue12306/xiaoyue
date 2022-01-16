import xlrd,xlwt
from xlutils.copy import copy
excel=xlrd.open_workbook(r'C:\Users\xyy\Desktop\xy\Python\venv\vlookup\Stock Check.xls')
sheet1=excel.sheets()[0]
sheet2=excel.sheets()[1]
new_excel=copy(excel)
newex=new_excel.get_sheet(0)
# 获取表一单元格的值
for sheet1_h in range (1,151):
    cell_sap_value=int(sheet1.cell(sheet1_h,0).value)
    # 获取表二单元格的值
    for sheet2_h in range(1,16904):
        cell_wl_value=int(sheet2.cell(sheet2_h,0).value)
        # 在表二寻找对应值
        if cell_sap_value==cell_wl_value:
            # 获取库存
            rest=int(sheet2.cell(sheet2_h,5).value)
            rest_count.append(rest)
            # 获取工厂
            factory=sheet2.cell(sheet2_h,2).value
            if factory==str(5050):
                newex.write(sheet1_h,1,sum(rest_count))
            elif factory==str(5250):
                newex.write(sheet1_h,2,sum(rest_count))
            elif factory == str(5251):
                newex.write(sheet1_h, 3,sum(rest_count))
new_excel.save('write2.xls')