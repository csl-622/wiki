# Use this to convert the 6 to 12th textbooks to text file 
import os

from os import chdir, getcwd, listdir, path

import pyPdf

from time import strftime


def check_path(prompt):

  
    abs_path = raw_input(prompt)

    while path.exists(abs_path) != True:

        print "\nThe specified path does not exist.\n"

        abs_path = raw_input(prompt)

    return abs_path   

   

print "\n"

#Update the path of the folder here
folder = check_path("Provide absolute path for the folder: ")


list=[]

directory=folder

for root,dirs,files in os.walk(directory):

    for filename in files:

        if filename.endswith('.pdf'):

            t=os.path.join(directory,filename)

            list.append(t)


m=len(list)

i=0

while i<=len(list):

    path=list[i]

    head,tail=os.path.split(path)

    var="\\"

   

    tail=tail.replace(".pdf",".txt")

    name=head+var+tail

   

   

    

    content = ""


    pdf = pyPdf.PdfFileReader(file(path, "rb"))


    for i in range(0, pdf.getNumPages()):

        # Extract text from page and add to content

        content += pdf.getPage(i).extractText() + "\n"

    print strftime("%H:%M:%S"), " pdf  -> txt "

    f=open(name,'w')

    f.write(content.encode("UTF-8"))

    f.close
