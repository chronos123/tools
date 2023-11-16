import PyPDF2

def extract_pages(file_name, start_page, end_page):
    pdf_file = open(file_name, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    pdf_writer = PyPDF2.PdfWriter()
    for page_num in range(start_page - 1, end_page):  # Python uses 0-indexing
        pdf_writer.add_page(pdf_reader.pages[page_num])

    output_file_name = f"{file_name[:-4]}_{start_page}-{end_page}.pdf"
    with open(output_file_name, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    pdf_file.close()

# Call the function with the name of your PDF file
extract_pages(r"E:\北航\研一\研一上\数字图像处理\数字图像处理中文第三版(冈萨雷斯).pdf", 258, 342)
# "E:\北航\研一\研一上\数字图像处理\数字图像处理第三版课后习题答案.pdf"

