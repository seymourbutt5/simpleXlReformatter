from openpyxl import *
from paths import *

# Takes a list of column data, the desired header, and the column number to write the data to
def create_workbook():
    workbook = Workbook()
    return workbook

def set_column(workbook, header, column_data, column_num):
    # Create a new workbook and get the active sheet
    sheet = workbook.active

    # Iterate through the data and write it to the first column of the sheet
    sheet.cell(row=1, column=column_num, value=header)

    for index, value in enumerate(column_data, start=2):
        sheet.cell(row=index, column=column_num, value=value)

def save_workbook(workbook, path):
    workbook.save("C:\\Users\\aquic\\Documents\\GitHub\\simpleXlReformatter\\ReformattedFiles\\testfile.xlsx")

def write_new_workbook(xl_sheet):
    workbook = create_workbook()
    set_column(workbook, "Product Name", xl_sheet.product_name_column, 1)
    set_column(workbook, "Price", xl_sheet.price_column, 2)
    set_column(workbook, "Category", xl_sheet.category_column, 3)
    save_workbook(workbook, destination_xl_file)
