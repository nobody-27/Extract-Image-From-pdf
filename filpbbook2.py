import fitz as ft

file = ft.open("sample.pdf")
for i in range(len(file)):
    for image in file.getPageImageList(i):
          xref = image[0]