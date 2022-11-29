from functools import partial
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


import PreLoadedGraphs
from Graph import Graph

'''
root = tk.Tk()
    root.title("Lights Out! A Game on Directed Graphs")
    root.geometry("1500x1000")
    app = tk.Frame(root, background="#c7e7c9")
    app.place(relx=0, rely=0, relheight=1, relwidth=1)
'''

def beginGame(root, gameGraph = Graph(2), preset_value = "null"):
    vertex_button_dict = {}

    if preset_value != "null":
        titleGAME = tk.Label(
        root,
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
                gameGraph = PreLoadedGraphs.chooseOption(preset_value)

                A_btn = tk.Button(
                    root,
                    text="A",
                    width=25,
                    height=5,
                    activebackground = "black",
                    activeforeground = "gray",
                    #command=partial(generatePresetGraph, ("option_one")
                    )
                A_btn.place(relx=.2, rely=.35, relheight=.06, relwidth=.06)

                B_btn = tk.Button(
                    root,
                    text="B",
                    width=25,
                    height=5,
                    activebackground = "black",
                    activeforeground = "gray",
                    #command=partial(generatePresetGraph, "option_one")
                    )
                B_btn.place(relx=.3, rely=.35, relheight=.06, relwidth=.06)

                C_btn = tk.Button(
                    root,
                    text="C",
                    width=25,
                    height=5,
                    activebackground = "black",
                    activeforeground = "gray",
                    #command=partial(generatePresetGraph, "option_one")
                    )
                C_btn.place(relx=.4, rely=.35, relheight=.06, relwidth=.06)

                D_btn = tk.Button(
                    root,
                    text="D",
                    width=25,
                    height=5,
                    activebackground = "black",
                    activeforeground = "gray",
                    #command=partial(generatePresetGraph, "option_one")
                    )
                D_btn.place(relx=.5, rely=.35, relheight=.06, relwidth=.06)

                E_btn = tk.Button(
                    root,
                    text="E",
                    width=25,
                    height=5,
                    activebackground = "black",
                    activeforeground = "gray",
                    #command=partial(generatePresetGraph, "option_one")
                    )
                E_btn.place(relx=.6, rely=.35, relheight=.06, relwidth=.06)

                F_btn = tk.Button(
                    root,
                    text="F",
                    width=25,
                    height=5,
                    activebackground = "black",
                    activeforeground = "gray",
                    #command=partial(generatePresetGraph, "option_one")
                    )
                F_btn.place(relx=.7, rely=.35, relheight=.06, relwidth=.06)


                #vertex_button_dict = {"A": ,
                            #"B": PresetTWO_btn,
                            #"C": Prese}

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




#root.mainloop()