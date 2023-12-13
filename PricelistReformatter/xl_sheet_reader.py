from openpyxl import *
from paths import *

def get_column(column_head):   
    # Open the spreadsheet 
    workbook = load_workbook(source_xl_file)     
    # Get the first sheet 
    sheet = workbook.worksheets[0]  
       
    # Create a list to store the values 
    column = []    
    # Iterate over the rows in the sheet 
    for row in sheet: 
        # Get the value of the first cell 
        # in the row (the "Name" cell) 
        cell = row[column_head].value 
        # Add the value to the list        
        column.append(cell)    
    
    # Removing the header information from the column
    column.pop(0)
    column.pop(0)
    return column