from functools import partial
import tkinter as tk
from tkinter import E, messagebox
from tkinter import ttk
from tracemalloc import start
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
global vertex_button_dict
vertex_button_dict = {}

global game_graph
game_graph = Graph(2)

global list_of_game_btns
list_of_game_btns = []



def resetScreen(frame_name):
    for child in frame_name.winfo_children():
        child.destroy()

def destoryWidget(widget):
    for child in app.winfo_children():
        if child == widget:
            child.destroy()

def toggleBTN(btn):
    global vertex_button_dict
    global game_graph
    global list_of_game_btns

    vertex_to_toggle = vertex_button_dict[btn]

    edge_list = game_graph.edge_dict[vertex_to_toggle]

    game_graph.toggleVertex(vertex_to_toggle)

    #for child in app.winfo_children():
        #if child == 
    
    toggleButtonColor(btn)
    for wgd in app.winfo_children(): # all widgets 
        try:
            if wgd['text'] in edge_list:
                toggleButtonColor(wgd['highlightbackground']) # change the background colour
            else:
                pass
        except:
            pass
    #for button in vertex_button_dict:
        #if vertex_button_dict[button] in edge_list:
            #toggleButtonColor(button.cget('bg'))
    game_graph.printGraph()
    if game_graph.checkWinner:
        #display a message saying the game has been won!
        play_again = messagebox.askretrycancel('WINNER', 'You won! Would you like to play again?')
        if play_again == 'yes':
            pass
        elif play_again == 'no':
            pass
        else:
            messagebox.showerror('error', 'something went wrong')

def toggleButtonColor(currentBtnColor):
    if currentBtnColor == "red":
        return "blue"
    return "red"

#def createPresetGraphButtons():
   
#event handler
def generatePresetGraph(preset_option):
    game_graph_temp = Graph(2)
    game_graph_temp = PreLoadedGraphs.chooseOption(preset_option)
    #clear screen
    resetScreen(app)
    #Title on screem


def presetBTN_selected():
    #clear screen
    resetScreen(app)
    #create labels
    preset_display_label = tk.Label(
        text="Please select form the following preset graph options: ",
        activebackground = "black",
        activeforeground = "gray",  # Set the background color to black
    )
    preset_display_label.place(relx=.2, rely=.05, relheight=.2, relwidth=.3)

    #create 10 buttons, for the 10 options
     #preset buttons are created here, seperation used for simplicity
    PresetONE_btn = tk.Button(app, 
    text="Preset One", 
    width=25, 
    height=5,
    activebackground = "black", 
    activeforeground = "gray", 
    command=partial(beginGame, "option_one"))
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

    #when any of the buttons are pressed, call the appropriate display functions per option


def Create_show_msg():
   messagebox.showinfo("Message","You pressed create new graph!.")

def preset_show_msg(event):
   messagebox.showinfo("Message","you pressed preload graph!")
   presetBTN_selected()

def beginGame(preset_value):
    global vertex_button_dict
    global game_graph
    global list_of_game_btns

    resetScreen(app)
    

    if len(preset_value) > 2:
        titleGAME = tk.Label(
        app,
        text="Lights Out!",
        activebackground = "black",
        activeforeground = "gray",  # Set the background color to black
        width = 10, 
        height = 10
        )
        titleGAME.place(relx=.2, rely=.2, relheight=.1, relwidth=.1)
        #generate by case nodes + edges
        match preset_value:
            case "option_one":
                game_graph = PreLoadedGraphs.chooseOption(preset_value)
                A_btn = tk.Button(
                    app,
                    text="A",
                    width=25,
                    height=5,
                    highlightbackground= 'red',
                    highlightcolor='red',
                    foreground = 'black',
                    #command=lambda: [toggleBTN("A_btn"), Create_show_msg()]
                    )
                A_btn['command'] = lambda: [toggleBTN(A_btn), Create_show_msg()]
                A_btn.place(relx=.2, rely=.35, relheight=.06, relwidth=.06)

                B_btn = tk.Button(
                    app,
                    text="B",
                    width=25,
                    height=5,
                    highlightbackground= 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                B_btn.place(relx=.3, rely=.35, relheight=.06, relwidth=.06)

                C_btn = tk.Button(
                    app,
                    text="C",
                    width=25,
                    height=5,
                    highlightbackground= 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                C_btn.place(relx=.4, rely=.35, relheight=.06, relwidth=.06)

                D_btn = tk.Button(
                    app,
                    text="D",
                    width=25,
                    height=5,
                    highlightbackground= 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                D_btn.place(relx=.5, rely=.35, relheight=.06, relwidth=.06)

                E_btn = tk.Button(
                    app,
                    text="E",
                    width=25,
                    height=5,
                    highlightbackground= 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                E_btn.place(relx=.6, rely=.35, relheight=.06, relwidth=.06)

                F_btn = tk.Button(
                    app,
                    text="F",
                    width=25,
                    height=5,
                    highlightbackground= 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                F_btn.place(relx=.7, rely=.35, relheight=.06, relwidth=.06)


                vertex_button_dict = {A_btn: "A",
                                      B_btn: "B",
                                      C_btn: "C",
                                      D_btn: "D",
                                      E_btn: "E",
                                      F_btn: "F"}
                list_of_game_btns = [A_btn, B_btn, C_btn, D_btn, E_btn, F_btn]
                                      
                #app.create_line(100,200,200,35, fill="green", width=5)
            case "option_two":
                #display
                pass
            case "option_three":
                #display
                pass

            case "option_four":
                #display
                pass

            case "option_five":
                #display
                pass

            case "option_six":
                #display
                pass

            case "option_seven":
                #display
                pass

            case "option_eight":
                #display
                pass

            case "option_nine":
                #display
                pass

            case "option_ten":
                #display
                pass

            case _:
                print("not an option")
                return
    else:
        messagebox.showinfo("Message","This function is under constuction!")
        return




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