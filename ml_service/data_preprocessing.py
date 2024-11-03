import os

from parser import take_all_files, get_links_to_files
from pdf_processing import pdf_reader, write_to_txt

# parsing files
url = 'https://www.disclosure.ru/issuer/7740000076/'
folder = "pdfci/"

take_all_files(get_links_to_files(url), folder)

# convert files from pdf to txt with taking text from images
folder = "images/"
folder1 = "processed_files/"

for filename in os.listdir("pdfci"):
    try:
        text = pdf_reader("pdfci/" + filename, folder)
        write_to_txt(text, folder1)
    except Exception as e:
        print(f"Error processing file {filename}")

# chanking and embedding files,
