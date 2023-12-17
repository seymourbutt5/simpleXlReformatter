import PySimpleGUI as sg
from openpyxl import *
from xl_sheet_writer import *
from xl_sheet import *

def upload_xl_sheet():
    sg.theme("DarkTeal2")
    layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("Submit")]]    
    window = sg.Window('My File Browser', layout, size=(600,150))

    # Render window loop
    while(True):
        event, values = window.read()

        # End App if window is closed
        if event == sg.WIN_CLOSED or event=="Exit":
            break

        elif event == "Submit":
            file_path = values["-IN-"]
            if file_path:
                worksheet = xl_sheet(file_path)
                write_new_workbook(worksheet)
            if not is_xlsx_file(file_path):
                sg.popup("Not a valid file format.")
            if not file_path:
                sg.popup("Please select a file.")

def is_xlsx_file(file_path):
    return file_path.lower().endswith(".xlsx")