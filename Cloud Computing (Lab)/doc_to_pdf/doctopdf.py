from docx2pdf import convert

# Replace 'input_file.docx' with the path to your Word file

for i in range(1,9):
    input_file = f"./all/16010421119_A3_CC_EXP{i}_INLAB.docx"
    convert(input_file)
    print(f"Converted {input_file} to PDF")
