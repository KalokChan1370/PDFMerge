from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from tkinter import *
from tkinter.ttk import *
import sys
import time

def merge (folder):
    output = PdfFileWriter()
    merges = []
    counter = 0

    # gets list of pdf files excluding the merged.pdf(the output file)
    for filename in os.listdir(folder):
        if filename[-4:]=='.pdf' and filename!= 'merged.pdf':
            merges.append(filename)
    if len(merges)!=0:
        while(counter< len(merges)):
            time.sleep(0.05)
            read = PdfFileReader(merges[counter])
            output.appendPagesFromReader(read)
            counter+=1
            bar['value']+=counter/len(merges)*100
            percent.set(str(int(counter/len(merges)*100))+"%")
            window.update_idletasks()
        
        with open("merged.pdf", 'wb') as out:
            output.write(out)
        text.set("Merge complete!!")
    else:
        text.set("No PDF files to merge.")

window = Tk()
window.title("PDFMerge")
bar = Progressbar(window, orient=HORIZONTAL, length = 500)
bar.pack(pady=10)

percent = StringVar()
percentLabel = Label(window,textvariable=percent).pack()
text= StringVar()
taskLabel = Label(window,textvariable=text).pack()

# uncomment the path variable with __file__ and comment the other
# if using as a .py
# path=os.path.dirname(os.path.realpath(__file__))
path=os.path.dirname(os.path.realpath(sys.executable))
merge(path)

button = Button(window, text="close", command=window.destroy).pack()
window.mainloop()