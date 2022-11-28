import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from turtle import onclick

root = tk.Tk()
root.title("Lights Out! A Game on Directed Graphs")
#root.geometry()
app = tk.Frame(root)
app.place(relx=0, rely=0, relheight=1, relwidth=1)
#	enter widgets here


def resetScreen():
    for child in app.winfo_children():
        child.destroy()

def createPresetGraphButtons():
    #preset buttons are created here, seperation used for simplicity
    PresetONE_btn = tk.Button(
    app,
    text="Preset One",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=Create_show_msg
    )
    PresetONE_btn.place(relx=.2, rely=.25, relheight=.125, relwidth=.125)

    PresetTWO_btn = tk.Button(
    app,
    text="Preset Two",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=Create_show_msg
    )
    PresetTWO_btn.place(relx=.2, rely=.4, relheight=.125, relwidth=.125)

    PresetTHREE_btn = tk.Button(
    app,
    text="Preset Three",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=Create_show_msg
    )
    PresetTHREE_btn.place(relx=.2, rely=.55, relheight=.125, relwidth=.125)

    PresetFOUR_btn = tk.Button(
    app,
    text="Preset Four",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=Create_show_msg
    )
    PresetFOUR_btn.place(relx=.2, rely=.70, relheight=.125, relwidth=.125)

    PresetFIVE_btn = tk.Button(
    app,
    text="Preset Five",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=Create_show_msg
    )
    PresetFIVE_btn.place(relx=.2, rely=.85, relheight=.125, relwidth=.125)

    PresetSIX_btn = tk.Button(
    app,
    text="Preset Six",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=Create_show_msg
    )
    PresetSIX_btn.place(relx=.4, rely=.25, relheight=.125, relwidth=.125)

    PresetSEVEN_btn = tk.Button(
    app,
    text="Preset Seven",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=Create_show_msg
    )
    PresetSEVEN_btn.place(relx=.4, rely=.4, relheight=.125, relwidth=.125)

    PresetEIGHT_btn = tk.Button(
    app,
    text="Preset Eight",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=Create_show_msg
    )
    PresetEIGHT_btn.place(relx=.4, rely=.55, relheight=.125, relwidth=.125)

    PresetNINE_btn = tk.Button(
    app,
    text="Preset Nine",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=Create_show_msg
    )
    PresetNINE_btn.place(relx=.4, rely=.70, relheight=.125, relwidth=.125)

    PresetTEN_btn = tk.Button(
    app,
    text="Preset Ten",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=Create_show_msg
    )
    PresetTEN_btn.place(relx=.4, rely=.85, relheight=.125, relwidth=.125)
#event handler
def selectPreloadedONE():
    pass

def presetBTN_selected():
    #clear screen
    resetScreen()
    #create labels
    preset_display_label = tk.Label(
        text="Please select form the following preset graph options: ",
        activebackground = "black",
        activeforeground = "gray",  # Set the background color to black
    )
    preset_display_label.place(relx=.2, rely=.05, relheight=.2, relwidth=.3)


    #create 10 buttons, for the 10 options
    createPresetGraphButtons()
    #when any of the buttons are pressed, call the appropriate display functions per option


def Create_show_msg(event):
   messagebox.showinfo("Message","You pressed create new graph!.")

def preset_show_msg(event):
   messagebox.showinfo("Message","you pressed preload graph!")
   presetBTN_selected()


#visual stuff
title = tk.Label(
    app,
    text="Lights Out!",
    activebackground = "black",
    activeforeground = "gray",  # Set the background color to black
    width = 10, 
    height = 10
)
title.place(relx=.2, rely=.2, relheight=.1, relwidth=.1)

createNewGraph_btn = tk.Button(
    app,
    text="Create new",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=Create_show_msg
)
createNewGraph_btn.place(relx=.4, rely=.4, relheight=.1, relwidth=.1)

loadPresetGraph_btn = tk.Button(
    app, 
    text="load graph",
    activebackground = "black",
    activeforeground = "gray",
    command = presetBTN_selected
)
loadPresetGraph_btn.place(relx=.5, rely=.5, relheight=.1, relwidth=.1)


app.mainloop()