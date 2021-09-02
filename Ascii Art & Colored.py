# install Required Packages:
# pip install termcolor2 
# pip install pyfiglet
# import Required packages:
import termcolor2
import pyfiglet
list_of_colors = ['red', 'green', 'yellow','blue', 'magenta', 'cyan', 'white'] # list of qualify colors
Word = input("Please enter your word to ascii art : ") # get a word from user 
user_color = input("Please enter your color ['red', 'green', 'yellow','blue', 'magenta', 'cyan', 'white'] : ") # get color from user
Word_figlet = pyfiglet.figlet_format(Word) # figletting procces
# check qualify of color
if user_color in list_of_colors:
    Word_Colored = termcolor2.colored(Word_figlet,user_color)
    print(Word_Colored)
else:
    print("your color is not defined... ")
# End Script and WaterMark
print("Build by Amirsobhan Hosseinpour ! license: CC by sa... ")
input("Please enter key to end... ")
# Build by Amirsobhan Hosseinpour ! license: CC by sa..