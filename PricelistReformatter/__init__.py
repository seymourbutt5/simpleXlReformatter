from openpyxl import *
from paths import *
from xl_sheet import *
from xl_sheet_reader import *

worksheet = xl_sheet()

# Testing
print(worksheet.product_name_column)
print(worksheet.price_column)
print(worksheet.category_column)

