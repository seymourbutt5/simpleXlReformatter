from openpyxl import *
from paths import *
from xl_sheet import *
from xl_sheet_reader import *
from xl_sheet_writer import *

worksheet = xl_sheet()

# Testing
write_new_workbook(worksheet)
