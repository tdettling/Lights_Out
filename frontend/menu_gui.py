from functools import partial
import tkinter as tk
from tkinter import E, messagebox
from tkinter import ttk
from tracemalloc import start
from turtle import bgcolor, onclick
 
import PreLoadedGraphs
from Graph import Graph

 
root = tk.Tk()
root.title("Lights Out! A Game on Directed Graphs")
root.geometry("1000x600")
root.resizable(False, False)
app = tk.Canvas(root, width=600, height=600, bg="#c7e7c9")
#app = tk.Frame(root, background="#c7e7c9")
app.place(relx=0, rely=0, relheight=1, relwidth=1)
 
#   enter widgets here
global vertex_button_dict
vertex_button_dict = {}
 
global game_graph
game_graph = Graph(2)
 
global list_of_game_btns
list_of_game_btns = []
 
global moves_counter
moves_counter = 0
 
 
def resetScreen(frame_name):
    for child in frame_name.winfo_children():
        child.destroy()
    frame_name.delete("all")
 
def destoryWidget(widget):
    for child in app.winfo_children():
        if child == widget:
            child.destroy()
 
def toggleBTN(btn, preset_value):
    global vertex_button_dict
    global game_graph
    global list_of_game_btns
    global moves_counter
 
    vertex_to_toggle = vertex_button_dict[btn]
 
    edge_list = game_graph.edge_dict[vertex_to_toggle]
 
    game_graph.toggleVertex(vertex_to_toggle)
 
    #for child in app.winfo_children():
        #if child ==
   
    newColor_currentVertex = toggleButtonColor(btn['bg'])
    btn["bg"] = newColor_currentVertex
    for wgd in app.winfo_children(): # all widgets
        if wgd['text'] in edge_list:
            print("changing button color")
            newColor = toggleButtonColor(wgd['bg']) # change the background colour
            wgd["bg"] = newColor
 
    moves_counter = moves_counter + 1
    game_graph.printGraph()
    if game_graph.checkWinner():
        #display a message saying the game has been won!
        play_again = messagebox.askyesnocancel('WINNER', 'You won! Would you like to play again?')
        print(play_again)
        if play_again == True:
            beginGame(preset_value)
        elif play_again == False:
            main_menu()
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
    preset_display_label = tk.Label(app,
        text="Please select form the following preset graph options: ",
        bg = "#c7e7c9",
        font=("Arial", 15),
        activeforeground = "gray",  # Set the background color to black
    )
    preset_display_label.place(relx=.10, rely=.05, relheight=.2, relwidth=.82)
 
    back_btn = tk.Button(app,
    text="Back",
    font=("Arial", 10),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command = main_menu
    )
    back_btn.place(relx=.45, rely=.030, relheight=.070, relwidth=.070)
 
    #create 10 buttons, for the 10 options
     #preset buttons are created here, seperation used for simplicity
    PresetONE_btn = tk.Button(app,
    text="Preset One",
    font=("Arial", 12),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(beginGame, "option_one"))
    PresetONE_btn.place(relx=.32, rely=.20, relheight=.125, relwidth=.125)
 
    PresetTWO_btn = tk.Button(
    app,
    text="Preset Two",
    font=("Arial", 12),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(beginGame, "option_two")
    #command=partial(startGame_gui.beginGame, PreLoadedGraphs.chooseOption("option_two"))
    )
    PresetTWO_btn.place(relx=.32, rely=.35, relheight=.125, relwidth=.125)
 
    PresetTHREE_btn = tk.Button(
    app,
    text="Preset Three",
    font=("Arial", 12),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(beginGame, "option_three")
    )
    PresetTHREE_btn.place(relx=.32, rely=.50, relheight=.125, relwidth=.125)
 
    PresetFOUR_btn = tk.Button(
    app,
    text="Preset Four",
    font=("Arial", 12),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(beginGame, "option_four")
    )
    PresetFOUR_btn.place(relx=.32, rely=.65, relheight=.125, relwidth=.125)
 
    PresetFIVE_btn = tk.Button(
    app,
    text="Preset Five",
    font=("Arial", 12),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(beginGame, "option_five")
    )
    PresetFIVE_btn.place(relx=.32, rely=.80, relheight=.125, relwidth=.125)
 
    PresetSIX_btn = tk.Button(
    app,
    text="Preset Six",
    font=("Arial", 12),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(beginGame, "option_six")
    )
    PresetSIX_btn.place(relx=.55, rely=.20, relheight=.125, relwidth=.125)
 
    PresetSEVEN_btn = tk.Button(
    app,
    text="Preset Seven",
    font=("Arial", 12),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(beginGame, "option_seven")
    )
    PresetSEVEN_btn.place(relx=.55, rely=.35, relheight=.125, relwidth=.125)
 
    PresetEIGHT_btn = tk.Button(
    app,
    text="Preset Eight",
    font=("Arial", 12),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(beginGame, "option_eight")
    )
    PresetEIGHT_btn.place(relx=.55, rely=.50, relheight=.125, relwidth=.125)
 
    PresetNINE_btn = tk.Button(
    app,
    text="Preset Nine",
    font=("Arial", 12),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(beginGame, "option_nine")
    )
    PresetNINE_btn.place(relx=.55, rely=.65, relheight=.125, relwidth=.125)
 
    PresetTEN_btn = tk.Button(
    app,
    text="Preset Ten",
    font=("Arial", 12),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command=partial(beginGame, "option_ten")
    )
    PresetTEN_btn.place(relx=.55, rely=.80, relheight=.125, relwidth=.125)
 
    #when any of the buttons are pressed, call the appropriate display functions per option
 
 
def Create_show_msg():
   messagebox.showinfo("Message","This function is under construction!.")

def drawBtn_selected():
    resetScreen(app)
    stop_editing_btn = tk.Button(app,
        text="Done Creating Verticies",
        font=("Arial", 10),
        width=25,
        height=5,
        activebackground = "black",
        activeforeground = "gray",
        command = takeEdgeInputs
        )
    stop_editing_btn.place(relx=.25, rely=.030, relheight=.070, relwidth=.15)

    back_btn = tk.Button(app,
    text="Back",
    font=("Arial", 10),
    width=25,
    height=5,
    activebackground = "black",
    activeforeground = "gray",
    command = main_menu
    )
    back_btn.place(relx=.65, rely=.030, relheight=.070, relwidth=.070)

    app.old_coords = None

    app.bind('<Button-1>', draw_vertex)
    app.bind('<Button-3>', draw_edge)
    
# Method to draw line between two consecutive points
def draw_edge(event):
   x, y = event.x, event.y
   if app.old_coords:
      x1, y1 = app.old_coords
      app.create_line(x, y, x1, y1, width=5)
   app.old_coords = x, y

def takeEdgeInputs():
    app.unbind('<Button 1>')
    app.unbind('<Button-3>')
    T = tk.Entry(app)
    T.place(relx=.35, rely=.80, relheight=.080, relwidth=.25)
    #T.insert(tk.END, "tester")

def contructGraph(list_of_verticies, list_of_edges, button_list):
    pass

def draw_vertex(event):
    x1=event.x
    y1=event.y
    x2=event.x
    y2=event.y

    placement_x = float(((x1+x2)/2)/1000)
    placement_y = float(((y1+y2)/2)/600)

    print("clicky click")

    btn = tk.Button(
                    app,
                    text="A",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    highlightcolor='red',
                    foreground = 'black',
                    #command=lambda: [toggleBTN("A_btn"), Create_show_msg()]
                    )
    btn['command'] = lambda: [toggleBTN(btn)]
    btn.place(relx=placement_x, rely=placement_y, relheight=.1, relwidth=.1)

    # Draw an oval in the given co-ordinates
    print(str(placement_x))
    print(str(placement_y))
    app.create_oval(x1,y1,x2,y2,fill="black", width=20)

 
def preset_show_msg(event):
   messagebox.showinfo("Message","you pressed preload graph!")
   presetBTN_selected()
 
def beginGame(preset_value):
    global vertex_button_dict
    global game_graph
    global list_of_game_btns
 
    resetScreen(app)
    game_graph = "null"
    #destoryWidget(widget)
 
    if len(preset_value) > 2:
        titleGame = tk.Label(
        app,
        text="Lights Out!",
        font=("Arial", 40),
        bg = "#c7e7c9",
        activeforeground = "#c7e7c9",  # Set the background color to black
        width = 40,
        height = 20
        )
        titleGame.place(relx=.3, rely=.05, relheight=.16, relwidth=.4)
 
        subtitle_Game = tk.Label(
        app,
        text="Directions: To toggle a vertex, simply click on it!",
        font=("Arial", 10),
        bg = "#c7e7c9",
        activeforeground = "#c7e7c9",  # Set the background color to black
        width = 40,
        height = 20
            )
        subtitle_Game.place(relx=.25, rely=.18, relheight=.1, relwidth=.5)
 
        bottom_info = tk.Label(
        app,
        text="CIS 611 Project, L Dettling. Motivated by Dr. Darren Parker",
        font=("Arial", 10),
        bg = "#c7e7c9",
        activeforeground = "#c7e7c9",  # Set the background color to black
        width = 40,
        height = 20
        )
        bottom_info.place(relx=.15, rely=.80, relheight=.16, relwidth=.7)
 
 
        #generate by case nodes + edges
        match preset_value:
            case "option_one":
                game_graph = PreLoadedGraphs.chooseOption(preset_value)
                A_btn = tk.Button(
                    app,
                    text="A",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    highlightcolor='red',
                    foreground = 'black',
                    #command=lambda: [toggleBTN("A_btn"), Create_show_msg()]
                    )
                A_btn['command'] = lambda: [toggleBTN(A_btn, preset_value)]
                A_btn.place(relx=.10, rely=.50, relheight=.1, relwidth=.1)
                # The line goes through the series of points
                # (x0, y0), (x1, y1), … (xn, yn)
                app.create_line(200, 335, 250, 335, width=8, arrow=tk.LAST)
 
                B_btn = tk.Button(
                    app,
                    text="B",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                B_btn['command'] = lambda: [toggleBTN(B_btn, preset_value)]
                B_btn.place(relx=.25, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(350, 335, 400, 335, width=8, arrow=tk.LAST)
 
                C_btn = tk.Button(
                    app,
                    text="C",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                C_btn['command'] = lambda: [toggleBTN(C_btn, preset_value)]
                C_btn.place(relx=.40, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(500, 335, 550, 335, width=9, arrow=tk.LAST)
 
 
                D_btn = tk.Button(
                    app,
                    text="D",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                D_btn['command'] = lambda: [toggleBTN(D_btn, preset_value)]
                D_btn.place(relx=.55, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(650, 335, 700, 335, width=9, arrow=tk.LAST)
 
                E_btn = tk.Button(
                    app,
                    text="E",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                E_btn['command'] = lambda: [toggleBTN(E_btn, preset_value)]
                E_btn.place(relx=.70, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(800, 335, 850, 335, width=9, arrow=tk.LAST)
 
                F_btn = tk.Button(
                    app,
                    text="F",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                F_btn['command'] = lambda: [toggleBTN(F_btn, preset_value)]
                F_btn.place(relx=.85, rely=.50, relheight=.1, relwidth=.1)
 
 
                vertex_button_dict = {A_btn: "A",
                                      B_btn: "B",
                                      C_btn: "C",
                                      D_btn: "D",
                                      E_btn: "E",
                                      F_btn: "F"}
                list_of_game_btns = [A_btn, B_btn, C_btn, D_btn, E_btn, F_btn]
                                     
                #app.create_line(100,200,200,35, fill="green", width=5)
            case "option_two":
                game_graph = PreLoadedGraphs.chooseOption(preset_value)
                A_btn = tk.Button(
                    app,
                    text="A",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    highlightcolor='red',
                    foreground = 'black',
                    #command=lambda: [toggleBTN("A_btn"), Create_show_msg()]
                    )
                A_btn['command'] = lambda: [toggleBTN(A_btn, preset_value)]
                A_btn.place(relx=.10, rely=.50, relheight=.1, relwidth=.1)
                # The line goes through the series of points
                # (x0, y0), (x1, y1), … (xn, yn)
                app.create_line(200, 335, 250, 335, width=8, arrow=tk.LAST)
 
                B_btn = tk.Button(
                    app,
                    text="B",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                B_btn['command'] = lambda: [toggleBTN(B_btn, preset_value)]
                B_btn.place(relx=.25, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(350, 335, 400, 335, width=8, arrow=tk.LAST)
 
                C_btn = tk.Button(
                    app,
                    text="C",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                C_btn['command'] = lambda: [toggleBTN(C_btn, preset_value)]
                C_btn.place(relx=.40, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(500, 335, 550, 335, width=9, arrow=tk.LAST)
                #coord = 10, 50, 240, 210
                #arc = app.create_arc(coord, start=0, extent=150, fill="blue")
                app.create_line(430,365, 300,430, 150,365, smooth=1, width=7, arrow=tk.LAST)
 
 
                D_btn = tk.Button(
                    app,
                    text="D",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                D_btn['command'] = lambda: [toggleBTN(D_btn, preset_value)]
                D_btn.place(relx=.55, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(650, 335, 700, 335, width=9, arrow=tk.LAST)
 
                E_btn = tk.Button(
                    app,
                    text="E",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                E_btn['command'] = lambda: [toggleBTN(E_btn, preset_value)]
                E_btn.place(relx=.70, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(800, 335, 850, 335, width=9, arrow=tk.LAST)
 
                F_btn = tk.Button(
                    app,
                    text="F",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                F_btn['command'] = lambda: [toggleBTN(F_btn, preset_value)]
                F_btn.place(relx=.85, rely=.50, relheight=.1, relwidth=.1)
 
 
                vertex_button_dict = {A_btn: "A",
                                      B_btn: "B",
                                      C_btn: "C",
                                      D_btn: "D",
                                      E_btn: "E",
                                      F_btn: "F"}
                list_of_game_btns = [A_btn, B_btn, C_btn, D_btn, E_btn, F_btn]
 
            case "option_three":
                #display
                game_graph = PreLoadedGraphs.chooseOption(preset_value)
                A_btn = tk.Button(
                    app,
                    text="A",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'blue',
                    highlightcolor='red',
                    foreground = 'black',
                    #command=lambda: [toggleBTN("A_btn"), Create_show_msg()]
                    )
                A_btn['command'] = lambda: [toggleBTN(A_btn, preset_value)]
                A_btn.place(relx=.35, rely=.32, relheight=.1, relwidth=.1)
                # The line goes through the series of points
                # (x0, y0), (x1, y1), … (xn, yn)
                app.create_line(450, 220, 550, 220, width=8, arrow=tk.LAST)
 
                B_btn = tk.Button(
                    app,
                    text="B",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                B_btn['command'] = lambda: [toggleBTN(B_btn, preset_value)]
                B_btn.place(relx=.55, rely=.32, relheight=.1, relwidth=.1)
                app.create_line(600, 250, 600, 300, width=8, arrow=tk.LAST)
 
                C_btn = tk.Button(
                    app,
                    text="C",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                C_btn['command'] = lambda: [toggleBTN(C_btn, preset_value)]
                C_btn.place(relx=.55, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(550, 330, 450, 330, width=8, arrow=tk.LAST)
 
                D_btn = tk.Button(
                    app,
                    text="D",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                D_btn['command'] = lambda: [toggleBTN(D_btn, preset_value)]
                D_btn.place(relx=.35, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(400, 300, 400, 250, width=8, arrow=tk.LAST)
                
                vertex_button_dict = {A_btn: "A",
                                      B_btn: "B",
                                      C_btn: "C",
                                      D_btn: "D"}
                list_of_game_btns = [A_btn, B_btn, C_btn, D_btn]
 
 
            case "option_four":
                #display
                game_graph = PreLoadedGraphs.chooseOption(preset_value)
                A_btn = tk.Button(
                    app,
                    text="A",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    highlightcolor='red',
                    foreground = 'black',
                    #command=lambda: [toggleBTN("A_btn"), Create_show_msg()]
                    )
                A_btn['command'] = lambda: [toggleBTN(A_btn, preset_value)]
                A_btn.place(relx=.35, rely=.32, relheight=.1, relwidth=.1)
                # The line goes through the series of points
                # (x0, y0), (x1, y1), … (xn, yn)
                app.create_line(450, 220, 550, 220, width=8, arrow=tk.LAST)
 
                B_btn = tk.Button(
                    app,
                    text="B",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                B_btn['command'] = lambda: [toggleBTN(B_btn, preset_value)]
                B_btn.place(relx=.55, rely=.32, relheight=.1, relwidth=.1)
                #app.create_line(450, 220, 550, 220, width=8, arrow=tk.LAST)
 
                C_btn = tk.Button(
                    app,
                    text="C",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'blue',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                C_btn['command'] = lambda: [toggleBTN(C_btn, preset_value)]
                C_btn.place(relx=.35, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(450, 330,550, 330, width=8, arrow=tk.LAST)
 
                D_btn = tk.Button(
                    app,
                    text="D",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                D_btn['command'] = lambda: [toggleBTN(D_btn, preset_value)]
                D_btn.place(relx=.55, rely=.50, relheight=.1, relwidth=.1)
                app.create_line(400, 250, 400, 300, width=8, arrow=tk.LAST)
                
                vertex_button_dict = {A_btn: "A",
                                      B_btn: "B",
                                      C_btn: "C",
                                      D_btn: "D"}
                list_of_game_btns = [A_btn, B_btn, C_btn, D_btn]
 
 
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
                game_graph = PreLoadedGraphs.chooseOption(preset_value)
                A_btn = tk.Button(
                    app,
                    text="A",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    highlightcolor='red',
                    foreground = 'black',
                    #command=lambda: [toggleBTN("A_btn"), Create_show_msg()]
                    )
                A_btn['command'] = lambda: [toggleBTN(A_btn, preset_value)]
                A_btn.place(relx=.20, rely=.42, relheight=.1, relwidth=.1)
                # The line goes through the series of points
                # (x0, y0), (x1, y1), … (xn, yn)
                app.create_line(300, 280, 448, 280, width=8, arrow=tk.LAST)
                app.create_line(300, 270, 448, 190, width=8, arrow=tk.LAST)
                app.create_line(300, 290, 448, 380, width=8, arrow=tk.LAST)
 
 
                B_btn = tk.Button(
                    app,
                    text="B",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'blue',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                B_btn['command'] = lambda: [toggleBTN(B_btn, preset_value)]
                B_btn.place(relx=.45, rely=.27, relheight=.1, relwidth=.1)
                #app.create_line(350, 335, 400, 335, width=8, arrow=tk.LAST)
 
                C_btn = tk.Button(
                    app,
                    text="C",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'blue',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                C_btn['command'] = lambda: [toggleBTN(C_btn, preset_value)]
                C_btn.place(relx=.45, rely=.42, relheight=.1, relwidth=.1)
                #app.create_line(500, 335, 550, 335, width=9, arrow=tk.LAST)
 
 
                D_btn = tk.Button(
                    app,
                    text="D",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                D_btn['command'] = lambda: [toggleBTN(D_btn, preset_value)]
                D_btn.place(relx=.45, rely=.57, relheight=.1, relwidth=.1)
                app.create_line(550, 370, 700, 370, width=8, arrow=tk.LAST)
 
                E_btn = tk.Button(
                    app,
                    text="E",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'blue',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                E_btn['command'] = lambda: [toggleBTN(E_btn, preset_value)]
                E_btn.place(relx=.70, rely=.57, relheight=.1, relwidth=.1)
                #app.create_line(800, 335, 850, 335, width=9, arrow=tk.LAST)
 
                F_btn = tk.Button(
                    app,
                    text="F",
                    font=("Arial", 35),
                    width=25,
                    height=5,
                    bg = 'red',
                    foreground = 'black',
                    #command=partial(generatePresetGraph, "option_one")
                    )
                F_btn['command'] = lambda: [toggleBTN(F_btn, preset_value)]
                F_btn.place(relx=.70, rely=.27, relheight=.1, relwidth=.1)
                app.create_line(700, 190, 550, 190, width=8, arrow=tk.LAST)
                app.create_line(750, 190, 750, 338, width=8, arrow=tk.LAST)
 
 
                vertex_button_dict = {A_btn: "A",
                                      B_btn: "B",
                                      C_btn: "C",
                                      D_btn: "D",
                                      E_btn: "E",
                                      F_btn: "F"}
                list_of_game_btns = [A_btn, B_btn, C_btn, D_btn, E_btn, F_btn]
 
            case _:
                print("not an option")
                return

        reset_btn = tk.Button(app,
                text="Reset Graph",
                font=("Arial", 10),
                width=25,
                height=5,
                activebackground = "black",
                activeforeground = "gray",
                )
        reset_btn['command'] = lambda: [beginGame(preset_value), displayResetMessage()]
        reset_btn.place(relx=.25, rely=.70, relheight=.070, relwidth=.160)

        chooseDiff_btn = tk.Button(app,
                text="Choose Different Graph",
                font=("Arial", 10),
                width=25,
                height=5,
                activebackground = "black",
                activeforeground = "gray",
                )
        chooseDiff_btn['command'] = lambda: [presetBTN_selected()]
        chooseDiff_btn.place(relx=.60, rely=.70, relheight=.070, relwidth=.160)

    else:
        messagebox.showinfo("Message","This function is under constuction!")
        return
 
 
def displayResetMessage():
    messagebox.showinfo("Graph Reset","Graph has been reset!")
 
#visual stuff
def main_menu():
    resetScreen(app)
    app.unbind('<Button 1>')
    app.unbind('<Button-3>')
    title = tk.Label(
        app,
        text="Lights Out!",
        font=("Arial", 40),
        bg = "#c7e7c9",
        activeforeground = "#c7e7c9",  # Set the background color to black
        width = 40,
        height = 20
    )
    title.place(relx=.3, rely=.05, relheight=.16, relwidth=.4)
 
    subtitle = tk.Label(
        app,
        text="A Game on Directed Graphs",
        font=("Arial", 10),
        bg = "#c7e7c9",
        activeforeground = "#c7e7c9",  # Set the background color to black
        width = 40,
        height = 20
    )
    subtitle.place(relx=.3, rely=.18, relheight=.2, relwidth=.4)
 
    createNewGraph_btn = tk.Button(
        app,
        text="Create New Graph",
        font=("Arial", 25),
        width=25,
        height=15,
        activebackground = "#c7e7c9",
        activeforeground = "#c7e7c9",
        command=drawBtn_selected
    )
    createNewGraph_btn.place(relx=.18, rely=.5, relheight=.15, relwidth=.29)
 
    loadPresetGraph_btn = tk.Button(
        app,
        text="Preloaded Graphs",
        font=("Arial", 25),
        activebackground = "black",
        activeforeground = "gray",
        command = presetBTN_selected
    )
    loadPresetGraph_btn.place(relx=.53, rely=.5, relheight=.15, relwidth=.29)
 
    bottom_info = tk.Label(
        app,
        text="CIS 611 Project, L Dettling. Motivated by Dr. Darren Parker",
        font=("Arial", 10),
        bg = "#c7e7c9",
        activeforeground = "#c7e7c9",  # Set the background color to black
        width = 40,
        height = 20
    )
    bottom_info.place(relx=.15, rely=.80, relheight=.16, relwidth=.7)
 
main_menu()
app.mainloop()
