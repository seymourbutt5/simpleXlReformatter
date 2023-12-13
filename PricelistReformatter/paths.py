from datetime import datetime

# Using a datetime affix to randomise the file name at generation
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

source_xl_file = "C:\\Users\\aquic\\Documents\\PricelistReformatter\\PRICE LIST 01.12.2023.xlsx"
destination_xl_file = "C:\\Users\\aquic\\Documents\\PricelistReformatter\\Pricelist_" + dt_string