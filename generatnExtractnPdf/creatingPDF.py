# This script creates a pdf file
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('generatnExtractnPdf/img.png', w=80, h=50)
pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt='ALX GRADUATION', align='C', border=1, ln=1)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt='Description:')

pdf.output('generatnExtractnPdf/output.pdf')