import img2pdf
from PIL import Image 
from fpdf import FPDF
from docx2pdf import convert
from moviepy.editor import *

def jpg_to_pdf():#jpg_to_pdf_single
    img_path='test/blr.jpg'
    pdf_path='test/blr.pdf'
    image = Image.open(img_path) 
    pdf_bytes = img2pdf.convert(image.filename) 
    file = open(pdf_path, "wb")
    file.write(pdf_bytes)
    image.close() 
    file.close()

def jpg_to_png(): #jpg_to_png
   Image.open("test/blr.jpg").save("test/sample1.png")


def jpg_to_pdf_multiple(): #jpg_to_pdf_multiple
    x=y=0
    pdf = FPDF()
    imagelist=['test/test1.jpg','test/test2.jpg','test/test3.jpg']
    for i in range(len(imagelist)):
        img=Image.open(imagelist[i])
        w,h=img.size
        w,h=float(w * 0.264583), float(h * 0.264583)
        pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
        orientation = 'P' if w < h else 'L'
        w = w if w < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
        h = h if h < pdf_size[orientation]['h'] else pdf_size[orientation]['h']
        pdf.add_page(orientation=orientation)
        pdf.image(imagelist[i],x,y,w,h)
    pdf.output("test/yourfile.pdf", "F")

def docx_to_pdf():  #docx_to_pdf  
    convert("test/input.docx", "test/output.pdf")