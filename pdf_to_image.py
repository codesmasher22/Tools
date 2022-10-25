import fitz
pdf = 'mypdf.pdf'
doc = fitz.open(pdf)
 
for page in doc:
    pix = page.getPixmap(alpha=False)
    pix.writePNG('page-%i.png' % page.number)