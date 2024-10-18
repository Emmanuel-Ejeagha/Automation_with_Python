# This script creates a pdf file
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('generatnExtractnPdf/img.png', w=80, h=50)

pdf.output('generatnExtractnPdf/output.pdf')