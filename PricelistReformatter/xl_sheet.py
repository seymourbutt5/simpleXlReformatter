from openpyxl import *
from paths import *
from xl_sheet_reader import *
from xl_sheet_writer import *

class xl_sheet():
    product_name_column = []
    price_column = []
    category_column = []

    def __init__(self, file_path):
        self.product_name_column = get_column(3, file_path)
        self.price_column = get_column(17, file_path)
        self.category_column = get_column(7, file_path)

    def print_self(self):
        print(self.product_name_column)
        print(self.price_column)
        print(self.category_column)


