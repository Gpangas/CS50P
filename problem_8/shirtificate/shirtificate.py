from fpdf import FPDF

#Input name for the shirt
name = input('Name: ')

#Set and add pdf page
pdf = FPDF(orientation='portrait', unit='mm', format='A4')
pdf.add_page()

#Add title
pdf.set_text_color(r=150, g=0, b=0)
pdf.set_font('helvetica', style='B', size=50)
pdf.set_y(45)
pdf.cell(w=0, h=0, text = "CS50 Shirtificate", new_x='LMARGIN', new_y='LAST', align = 'C')

#Add shirt image
pdf.image('shirtificate.png', x= 15, y= 80, w=180)

#Add name in shirt
pdf.set_text_color(r=0, g=0, b=0)
pdf.set_font('helvetica', style='B', size=30)
pdf.set_y(140)
pdf.cell(w=0, h=0, text = f"{name}", align = 'C')
pdf.ln()
pdf.cell(w=0, h=0, text = f"took CS50", align = 'C')

pdf.output('shirtificate.pdf')
