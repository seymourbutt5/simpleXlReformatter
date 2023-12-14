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
            worksheet = xl_sheet()
            write_new_workbook(worksheet)
