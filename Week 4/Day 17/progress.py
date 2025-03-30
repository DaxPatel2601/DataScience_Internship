import xlrd
import matplotlib.pyplot as plt
import numpy as np

sheet=xlrd.open_workbook("progress.xlsx").sheet_by_index(0)

date_DXP=[]
date_JMP=[]
hours=[0,1,2,3,4,5,6,7]

dxp_company_work=[]
dxp_course_work=[]
dxp_english_work=[]
dxp_total_work=np.array([])

jmp_company_work=[]
jmp_course_work=[]
jmp_english_work=[]
jmp_total_work=np.array([])



for j in range(1,sheet.nrows):
    if sheet.cell_value(j,4)=="DXP":
        date_DXP.append(int(sheet.cell_value(j,2)))
        dxp_company_work.append(int(sheet.cell_value(j,5)))
        dxp_course_work.append(int(sheet.cell_value(j,6)))
        dxp_english_work.append(int(sheet.cell_value(j,7)))
    if sheet.cell_value(j,4)=="JMP":
        date_JMP.append(int(sheet.cell_value(j, 2)))
        jmp_company_work.append(int(sheet.cell_value(j, 5)))
        jmp_course_work.append(int(sheet.cell_value(j, 6)))
        jmp_english_work.append(int(sheet.cell_value(j, 7)))


dxp_total_work=np.append(dxp_total_work,sum(dxp_english_work))
dxp_total_work=np.append(dxp_total_work,sum(dxp_course_work))
dxp_total_work=np.append(dxp_total_work,sum(dxp_company_work))
jmp_total_work = np.append(jmp_total_work, sum(jmp_english_work))
jmp_total_work = np.append(jmp_total_work,sum(jmp_course_work))
jmp_total_work = np.append(jmp_total_work,sum(jmp_company_work))



fig, ax = plt.subplots(2, 2,figsize=(10,5))

# DXP plo graph
ax[0,0].plot(date_DXP,dxp_course_work,label="Course")
ax[0,0].plot(date_DXP,dxp_company_work,label="Company")
ax[0,0].plot(date_DXP,dxp_english_work,label="English")
ax[0,0].set_xticks(date_DXP)
ax[0,0].set_yticks(hours)
ax[0,0].set_xlabel("Date")
ax[0,0].set_ylabel("Hours")
ax[0,0].set_title("DAX Date Wise Work Analysis")
ax[0,0].grid(alpha=0.2)
ax[0,0].legend()


# JMP plot graph
ax[0,1].plot(date_JMP,jmp_course_work,label="Course")
ax[0,1].plot(date_JMP,jmp_company_work,label="Company")
ax[0,1].plot(date_JMP,jmp_english_work,label="English")
ax[0,1].set_xticks(date_JMP)
ax[0,1].set_yticks(hours)
ax[0,1].set_xlabel("Date")
ax[0,1].set_ylabel("Hours")
ax[0,1].set_title("JIMI Date Wise Work Analysis")
ax[0,1].grid(alpha=0.2)
ax[0,1].legend()

ax[1,0].pie(dxp_total_work,labels=["English","Course","Company"],autopct="%.2f%%")
ax[1,0].set_title("DAX Overall Analysis")

ax[1,1].pie(jmp_total_work,labels=["English","Course","Company"],autopct="%.2f%%")
ax[1,1].set_title("JIMI Overall Analysis")

plt.tight_layout()
plt.show()

