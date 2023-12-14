import os
from datetime import datetime

# Using a datetime affix to randomise the file name at generation
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

source_xl_file = os.environ.get('XL_SOURCE_PATH')
destination_xl_file = os.environ.get('XL_DESTINATION_PATH') + "Pricelist" + dt_string + ".xlsx"