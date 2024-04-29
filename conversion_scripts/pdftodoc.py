from pdf2docx import Converter


def convert_pdf_to_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file)  # all pages by default
    cv.close()
    print(f"Converted {pdf_file} to DOCX")


# for i in range(7, 9):
#     pdf_file = f"./EXPS/AICA_expt_2{i}.pdf"
#     docx_file = f"./EXPS/16010421119_A3_VAPT_EXP{i}.docx"
#     convert_pdf_to_docx(pdf_file, docx_file)

convert_pdf_to_docx("./EXPS/AICA_expt_2.pdf", "./EXPS/AICA_exp_2.docx")
