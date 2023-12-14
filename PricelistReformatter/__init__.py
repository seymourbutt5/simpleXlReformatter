from openpyxl import *
from paths import *
from xl_sheet import *
from xl_sheet_reader import *
from xl_sheet_writer import *
import os

print(os.environ["XL_SOURCE_PATH"])

worksheet = xl_sheet()

print(xl_sheet.product_name_column)
print(xl_sheet.price_column)
print(xl_sheet.category_column)

# Testing
write_new_workbook(xl_sheet)
