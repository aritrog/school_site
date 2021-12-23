from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont



class pdfgen():
	def __init__(self):
		print("hi")
		c=canvas.Canvas("name1.pdf",pagesize=A4)
		width,height=A4
		#c.translate(inch,inch)
		self.put_heading(c)
		c.save()




	def put_heading(self,c):	
		c.setFillColorRGB(1,0,0)
		c.setFont('Helvetica',14)
		c.drawString(3.28*inch,11.2*inch,"Under the aegis of")
		c.setFont('Helvetica',16)
		c.drawString(2.6*inch,10.9*inch,"Indus Renaissance Foundation")
		c.setFont('Helvetica',10)
		c.drawString(2.7*inch,10.7*inch,"An Education Society, Regd. under W.B. Govt.")
		c.setFont('Times-Bold',30)
		c.drawString(1.1*inch, 10.3*inch, "AMBEDKAR PUBLIC SCHOOL")
		c.setFont('Times-Bold',16)
		c.drawString(2.4*inch, 10.07*inch, "C.B.S.E Syllabus (Regular)")
		c.setFont('Helvetica-Bold',11)
		c.drawString(1.1*inch, 9.9*inch, 
			"63, Netaji Subhash Path, Nichubasa, Kanchrapara, 24 pgs. (N) Ph.:9903004488,9230614678")

