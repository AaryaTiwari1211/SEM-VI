from docx2pdf import convert

for i in range(1,6):
    input_file = f"./EXPS/AICA.docx"
    convert(input_file)
    print(f"Converted {input_file} to PDF")

