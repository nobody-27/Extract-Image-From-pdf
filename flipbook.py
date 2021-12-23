import fitz



file = fitz.open("sample.pdf")
page = len(file)
for  i in range(page):
    for image in file.get_page_images(i):
        j = 0
        customxref=image[0]
        pic = fitz.Pixmap(file, customxref)
        finalpic = fitz.Pixmap(fitz.csRGB,pic)
        finalpic.writePNG(str(i)+"_"+str(j)+".png")
        pic = None
        finalpic = None
