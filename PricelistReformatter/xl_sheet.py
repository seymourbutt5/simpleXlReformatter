from openpyxl import *
from xl_sheet_reader import *

class xl_sheet:
    columns = ["Product Name", "Price", "Category", "Image"]
    product_name_column = []
    price_column = []
    category_column = []

    def __init__(self):
        self.product_name_column = get_column(3)
        self.price_column = get_column(17)
        self.category_column = get_column(7)


