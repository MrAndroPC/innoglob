from pypdf import PdfReader
from text_from_image import text_recognition
import os

counter = 1

def pdf_reader(pdf_file: str, folder: str):
    reader = PdfReader(pdf_file)

    text = ''

    for page in reader.pages:

        page_text = page.extract_text().splitlines()

        text += "\n".join([x for x in page_text if x.strip()])

        for count, image_file_object in enumerate(page.images):
            try:
                with open(folder + str(count) + image_file_object.name, "wb") as fp:
                    fp.write(image_file_object.data)
                    text += text_recognition(folder + str(count) + image_file_object.name)
                os.remove(folder + str(count) + image_file_object.name)
            except Exception as e:
                print(f"Error processing image on file {pdf_file}")

    # os.remove(pdf_file)
    return text

def write_to_txt(text: str, folder: str):
    global counter
    counter += 1

    file_name = folder+str(counter)+"_file.txt"
    with open(file_name, "w", encoding='utf-8') as f:
        f.write(text)


# pdf_file = "pdfci/otchet.pdf"

# print(pdf_reader(pdf_file, folder))
#
# write_to_txt(pdf_reader(pdf_file, folder), folder1)

# print(full_path)

# print(pdf_reader("pdfci/10.pdf", "images/"))