### DEBUGGER MODULE
# Define global debugger variables
version = 0.01
debugMode = False


# define debugger functions
def greetings():
    print("hello, this is web scrapper", version)


# define debugger
class debug_config:
    def __init__(self):
        self.mode = input("Debug Mode On? (y/n)")
        self.print_details()

    def print_details(self):
        if self.mode == 'y':
            print("Debug Mode is On", )
            debugMode = True

        elif self.mode == 'n':
            print("Debug Mode is Off", )

        else:
            print("Input invalid." )
            self.mode = input("Debug Mode On? (y/n)")
            self.print_details()
