import tkinter
import PyPDF2
from tkinter import *
from tkinter import filedialog

#Setting Variables
window = Tk()
file_list=[]
file_list_names=[]

output = PyPDF2.PdfFileWriter()


window.columnconfigure(0, minsize=300)
window.columnconfigure(1, minsize=300)


def watermarksourcefunc():
    global watermark
    watermark = filedialog.askopenfilename(filetypes=[("PDF File", "*.pdf")])
    watermarkfilepath.config(text=watermark)


def fileselectfunc():
    global filestobewatermarked
    filestobewatermarked = filedialog.askopenfilenames(filetypes=[("PDF File", "*.pdf")])
    for file in filestobewatermarked:
        file_list.append(file)



def runwatermark():

    for file in file_list:
        merged_file = file.replace('.pdf', '_WM.pdf')
        print(merged_file)

        input_file = open(file, 'rb')
        input_pdf = PyPDF2.PdfFileReader(file)
        # Get number of pages in input document
        page_count = input_pdf.getNumPages()

        watermark_file = open(watermark, 'rb')
        watermark_pdf = PyPDF2.PdfFileReader(watermark_file)

        for page_number in range(page_count):
            print("Watermarking page {} of {}".format(page_number, page_count))
            pdf_page = input_pdf.getPage(page_number)
            watermark_page = watermark_pdf.getPage(0)
            pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)

        merged_file = open(merged_file, 'wb')
        output.write(merged_file)

        merged_file.close()
        watermark_file.close()
        input_file.close()

# ******************************************************************************
# ````````````````````````````FORM LAYOUT```````````````````````````````````````
# ******************************************************************************

window.title('PDF WATERMARKER')

#Row 1
watermarklabel = Label(window, text="Select Watermark file",)
watermarklabel.grid(column=0,row=1, sticky=W)

watermarksourcebutton = Button(window, text="Browse", command=watermarksourcefunc, fg='black', bg='white')
watermarksourcebutton.grid(column=1, row=1)

#Row 2
watermarkfilepath = Label(window, text="", borderwidth=2, relief="groove")
watermarkfilepath.grid(columnspan=2, row=2, stick=NSEW)

#Row 3
sourcefileslabel = Label(window, text='Select Files to be Watermarked', anchor="w")
sourcefileslabel.grid(column=0, row=3, stick=W)

sourcefilesbutton = Button(window, text="Browse", command=fileselectfunc, fg='black', bg='white')
sourcefilesbutton.grid(column=1, row=3)

#Row 4
filestobewatermarkedlist = Label(window, text="", borderwidth=2, relief="groove")
filestobewatermarkedlist.grid(columnspan=2, row=4, stick=NSEW)

#Row 5
runwatermarkbutton = Button(window, text="Watermark", command=runwatermark, fg='black', bg='white')
runwatermarkbutton.grid(columnspan=2, row=5)


#MAIN LOOP
window.mainloop()
