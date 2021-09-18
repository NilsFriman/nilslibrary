# Takes input in form of a text that will appear to the user when asked for input, and gives back an integer value only.
def intinput(text):
    done = False
    while not done:
        finaltext = input(text)
        try:
            finaltext = int(finaltext)
            done = True
        except Exception:
            print("Sorry, you can only enter an integer. For example, 4 or -11.")
    return finaltext

# Takes input in form of a text that will appear to the user when asked for input, and gives back a float value only.
def floatinput(text):
    done = False
    while not done:
        finaltext = input(text)
        try:
            finalfloat = float(finaltext)
            done = True
        except Exception:
            print("Sorry, you can only enter an float. For example, 4.0 or -11.7.")
    return finalfloat

# Takes input in form of a text that will appear to the user when asked for input, and gives back a valid string without
# trailing newline or spaces
def stringinput(text):
    done = False
    while not done:
        finaltext = input(text)
        if finaltext != "":
            finaltext.rstrip()
            done = True
        else:
            print("Sorry, you have to enter some text.")
    return finaltext

# Takes input in the form of question and the default answer (either True (Yes) or False (No)),
# and returns True if the user inputs something other than the opposite of default, False if anything else
def boolinput(text, default):
    done = False
    while not done:
        if default:
            finaltext = input(text + " (Y/n)\n")
            finaltext.lower()
            if finaltext == "n":
                dabool = False
                done = True
            else:
                dabool = True
                done = True
        elif not default:
            finaltext = input(text + " (y/N)\n")
            finaltext.lower()
            if finaltext == "y":
                dabool = False
                done = True
            else:
                dabool = True
                done = True
        else:
            print("Hey programmer! When you call function boolinput, you must use the format boolinput(text, default),")
            print("where default is either True or False and shows which one of the two is the default one.")
    return dabool