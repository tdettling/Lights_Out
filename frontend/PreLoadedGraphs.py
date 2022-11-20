import main_AND_test.Graph as Graph

def createOptionOne():
    pass

def createOptionTwo():
    pass

def createOptionThree():
    pass

def createOptionFour():
    pass

def createOptionFive():
    pass

def createOptionSix():
    pass

def createOptionSeven():
    pass

def createOptionEight():
    pass

def createOptionNine():
    pass

def createOptionTen():
    pass

def chooseOption(option_selected):
    match option_selected:
        case "option_one":
            print("something")
            selectedGraph = createOptionOne()
            return selectedGraph
        case "option_two":
            print("something")
            selectedGraph = createOptionTwo()
            return selectedGraph

        case "option_three":
            selectedGraph = createOptionThree()
            return selectedGraph
            print("something")

        case "option_four":
            print("something")
            selectedGraph = createOptionFour()
            return selectedGraph

        case "option_five":
            print("something")
            selectedGraph = createOptionFive()
            return selectedGraph

        case "option_six":
            print("something")
            selectedGraph = createOptionSix()
            return selectedGraph

        case "option_seven":
            print("something")
            selectedGraph = createOptionSeven()
            return selectedGraph

        case "option_eight":
            print("something")
            selectedGraph = createOptionEight()
            return selectedGraph

        case "option_nine":
            print("something")
            selectedGraph = createOptionNine()
            return selectedGraph

        case "option_ten":
            print("something")
            selectedGraph = createOptionTen()
            return selectedGraph

        case _:
            print("not an option")
            return
