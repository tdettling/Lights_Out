from functools import partial
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from turtle import bgcolor, onclick

import PreLoadedGraphs
from Graph import Graph
import startGame_gui

root = tk.Tk()
root.title("Lights Out! A Game on Directed Graphs")
root.geometry("1500x1000")
app = tk.Frame(root, background="#c7e7c9")
app.place(relx=0, rely=0, relheight=1, relwidth=1)
#	enter widgets here
vertex_button_dict = {}


def resetScreen():
    for child in app.winfo_children():
        child.destroy()


def determineButtonColor(buttonColor):
    if buttonColor == "red":
        return "blue"
    return "red"

def toggleVertex(graph, vertex):
    #toggle vertex
    graph.toggleVertex(vertex)
    #toggle button colors
    listOfAdjVerticies = graph.getListOfAdjacentVerticies(vertex)
    #for vertex in listOfAdjVerticies:
        #button_to_change = 
        #button_to_change.configure(bg = "red")

    #check for win!

def createPresetGraphButtons():
    #preset buttons are created here, seperation used for simplicity
    PresetONE_btn = tk.Button(app, text="Preset One", width=25, height=5,\
    activebackground = "black", activeforeground = "gray", command=partial(generatePresetGraph, "option_one"))
    PresetONE_btn.place(relx=.2, rely=.25, relheight=.125, relwidth=.125)

    PresetTWO_btn = tk.Button(
    app,
    text="Preset Two",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(generatePresetGraph, "option_two")
    #command=partial(startGame_gui.beginGame, PreLoadedGraphs.chooseOption("option_two"))
    )
    PresetTWO_btn.place(relx=.2, rely=.4, relheight=.125, relwidth=.125)

    PresetTHREE_btn = tk.Button(
    app,
    text="Preset Three",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(generatePresetGraph, "option_three")
    )
    PresetTHREE_btn.place(relx=.2, rely=.55, relheight=.125, relwidth=.125)

    PresetFOUR_btn = tk.Button(
    app,
    text="Preset Four",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(generatePresetGraph, "option_four")
    )
    PresetFOUR_btn.place(relx=.2, rely=.70, relheight=.125, relwidth=.125)

    PresetFIVE_btn = tk.Button(
    app,
    text="Preset Five",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(generatePresetGraph, "option_five")
    )
    PresetFIVE_btn.place(relx=.2, rely=.85, relheight=.125, relwidth=.125)

    PresetSIX_btn = tk.Button(
    app,
    text="Preset Six",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(generatePresetGraph, "option_six")
    )
    PresetSIX_btn.place(relx=.4, rely=.25, relheight=.125, relwidth=.125)

    PresetSEVEN_btn = tk.Button(
    app,
    text="Preset Seven",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(generatePresetGraph, "option_seven")
    )
    PresetSEVEN_btn.place(relx=.4, rely=.4, relheight=.125, relwidth=.125)

    PresetEIGHT_btn = tk.Button(
    app,
    text="Preset Eight",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(generatePresetGraph, "option_eight")
    )
    PresetEIGHT_btn.place(relx=.4, rely=.55, relheight=.125, relwidth=.125)

    PresetNINE_btn = tk.Button(
    app,
    text="Preset Nine",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(generatePresetGraph, "option_nine")
    )
    PresetNINE_btn.place(relx=.4, rely=.70, relheight=.125, relwidth=.125)

    PresetTEN_btn = tk.Button(
    app,
    text="Preset Ten",
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(generatePresetGraph, "option_ten")
    )
    PresetTEN_btn.place(relx=.4, rely=.85, relheight=.125, relwidth=.125)

#event handler
def generatePresetGraph(preset_option):
    game_graph_temp = Graph(2)
    game_graph_temp = PreLoadedGraphs.chooseOption(preset_option)
    #clear screen
    resetScreen()
    #Title on screem


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
    font=("Arial", 40),
    activebackground = "#c7e7c9",
    activeforeground = "#c7e7c9",  # Set the background color to black
    width = 20, 
    height = 20
)
title.place(relx=.4, rely=.05, relheight=.2, relwidth=.2)

createNewGraph_btn = tk.Button(
    app,
    text="Create New Graph",
    font=("Arial", 30),
    width=25,
    height=15,
    activebackground = "#c7e7c9",
    activeforeground = "#c7e7c9",
    command=Create_show_msg
)
createNewGraph_btn.place(relx=.27, rely=.5, relheight=.15, relwidth=.18)

loadPresetGraph_btn = tk.Button(
    app, 
    text="Preloaded Graphs",
    font=("Arial", 30),
    activebackground = "black",
    activeforeground = "gray",
    command = presetBTN_selected
)
loadPresetGraph_btn.place(relx=.5, rely=.5, relheight=.15, relwidth=.18)


app.mainloop()