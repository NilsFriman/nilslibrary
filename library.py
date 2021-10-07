# Takes input in form of a text that will appear to the user when asked for input, and gives back an integer value only.
def intinput(text):
    while True:
        finaltext = input(text)
        try:
            return int(finaltext)
        except Exception:
            print("Sorry, you can only enter an integer. For example, 4 or -11.")

# Takes input in form of a text that will appear to the user when asked for input, and gives back a float value only.
def floatinput(text):
    while True:
        finaltext = input(text)
        try:
            return float(finaltext)
        except Exception:
            print("Sorry, you can only enter an float. For example, 4.0 or -11.7.")

# Takes input in form of a text that will appear to the user when asked for input, and gives back a valid string without
# trailing newline or spaces
def strinput(text):
    while True:
        finaltext = input(text)
        if finaltext != "":
            finaltext.rstrip()
            return finaltext
        else:
            print("Sorry, you have to enter some text.")

# Takes input in the form of question and the default answer (either True (Yes) or False (No)),
# and returns True if the user inputs something other than the opposite of default, False if anything else
def boolinput(text, default):
    while True:
        if default:
            finaltext = input(text + " (Y/n)\n")
            finaltext.lower()
            if finaltext == "n":
                return False
            else:
                return True
        elif not default:
            finaltext = input(text + " (y/N)\n")
            finaltext.lower()
            if finaltext == "y":
                return False
            else:
                return True
        else:
            print("Hey programmer! When you call function boolinput, you must use the format boolinput(text, default),")
            print("where default is either True or False and shows which one of the two is the default one.")

import json

# Overrites what is currently in the filename with the dump variable.
# If there is no file with that name, a file is created.
def writedata(filename, dump):
    a_file = open(filename, "w")
    json.dump(dump, a_file)
    a_file.close()

# Returns whatever is in the filename file.
def readdata(filename):
    a_file = open(filename, "r")
    return a_file.read()

# Presents the user with a number of options, and lets the user choose an option. The chosen option is returned.
def options(*args):
    while True:
        for argument in args:
            print("Option number " + str(args.index(argument) + 1) + ": " + str(argument))
        try:
            choice = int(input("What option number do you choose?\n"))
            if choice > 0:
                return args[choice - 1]
            else:
                raise ValueError
        except ValueError:
            print("You can only choose a whole number between 1 and " + str(len(args)))

def plural(number, singular, plural):
    if str(abs(number)) == "1":
        try:
            return str(number) + " " + singular
        except:
            print("Variable 'singular' must be a string.")
    else:
        try:
            return str(number) + " " + plural
        except:
            print("Variable 'plural' must be a string.")