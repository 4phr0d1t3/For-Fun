# Seccion 1: Obtención del texto

from pathlib import Path
from warnings import filterwarnings
from PyPDF2 import PdfFileReader

print("Extrayendo...")

# Abriendo y leyendo el PDF deseado
name = 'PDFs/Living in the Light'
filePath = name + '.pdf'
openedFile = open(filePath, 'rb')
pdfFR = PdfFileReader(openedFile, strict=False)

# Extraemos el texto contenido del PDF
txt = ''
for actualPage in range(pdfFR.getNumPages()):
	page = pdfFR.getPage(actualPage)
	txt += ' ' + page.extractText()
openedFile.close()

# Teniendo el texto recuperado del PDF, guardamos en un archivo txt
with Path('extracted.txt').open(mode ='w') as txtFile: txtFile.write(txt)
txtFile.close()

# Seccion 2: Creación del PDF

from fpdf import FPDF

print("Convirtiendo a PDF...")

# Definición de las partes del PDF
class PDF(FPDF):
	def header(self):
		# Posicionamiento de la imagen del color deseado para el fondo
		self.image('bg-color.png', x = 0, y = 0, w = 216, h = 280, type = '', link = '')

	def body(self):
		# Obtencion del texto recuperado anteriormente
		with open("extracted.txt", 'rb') as fh:
			txt = fh.read().decode('utf-8')

		txtAux = " "
		cont = 0
		self.set_font("Montserrat", 'L', size = 16)
		# Definición de donde y como se mostrará nuestro texto en el PDF
		for i in range(0, len(txt)):
			if txt[i] == " " or txt[i] == ".":
				pdfBR.write(8, txt = " ")
				# print(txtAux)

				leftH = txtAux[0:round(len(txtAux)*(5/12))]
				rightH = txtAux[len(leftH): len(txtAux)]

				self.set_font(family = "Montserrat", style = 'B', size = 16)
				self.write(8, txt = leftH)

				self.set_font(family = "Montserrat", style = 'L', size = 16)
				self.write(8, txt = rightH)

				txtAux = ""
				cont = 0
			else:
				txtAux = txtAux + txt[i]
				cont += 1

pdfBR = PDF('P', 'mm', 'Letter')

# Habilitamos el modo automatico de salto de pagina
pdfBR.set_auto_page_break(auto= True, margin=15)
# Añadimos una nueva pagina al documento
pdfBR.add_page()

# Añadimos la fuente que queremos usar para nuestro documento ademas del color
pdfBR.add_font("Montserrat", 'L', "./fonts/Montserrat-Light.ttf", uni=True)
pdfBR.add_font("Montserrat", 'B', "./fonts/Montserrat-SemiBold.ttf", uni=True)
pdfBR.set_text_color(56, 36, 12)

pdfBR.body()
# Envía el documento a algún destino: salida estándar, un archivo o una cadena de bytes;
# en nuestro caso, archivo PDF
filterwarnings('ignore')
pdfBR.output(name + '-BR.pdf')
print("Listo para leer: " + name + '-BR.pdf')
