import pandas as pd
from fpdf import FPDF
# install openpyxl

file = pd.read_excel('generatnExtractnPdf/002 data.xlsx')
# print(file)

for index, row in file.iterrows():
  pdf = FPDF(orientation='P', unit='pt', format='A4')
  pdf.add_page()
  
  pdf.set_font(family='Times', style='B', size=24)
  pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1)
  
  for column in file.columns[1:]:
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100, h=25, txt=f"{column.title()}:")
    
    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100, h=25, txt=row[column], ln=1)
    # print(column)
    
  pdf.output(f"generatnExtractnPdf/{row['name']}.pdf")