import os
import re
from datetime import datetime

# current date and time, in digits only, to affix to file for 'random' name
date_time = datetime.now()
string = date_time.isoformat()
numeric_string = re.sub(r'\D', '', string)

source_xl_file = os.environ.get('XL_SOURCE_PATH')
destination_xl_file = os.environ.get('XL_DESTINATION_PATH') + "Pricelist_" + numeric_string + ".xlsx"