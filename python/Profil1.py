import PySimpleGUI as sg
sg.theme("DarkGreen4")
window = sg.Window(title="profile",
                   layout=[[sg.Text("NPM    : 2210010092")],
                           [sg.Text("Nama   : Diva Damayanti")],
                           [sg.Text("Kelas  : 5P Reguler Banjarmasin")],
                           ],
                           size=(400,200),
                           font=("Times", 18))
window()
window.close()