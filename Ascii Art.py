# install Required Packages:
# pip install pyfiglet 
# import Required packages:
import pyfiglet
Word = input("Please enter your word to ascii art : ") # get a word from user 
Word_figlet = pyfiglet.figlet_format(Word) # figletting procces
print(Word_figlet) # show figlted word or text (default: wrod) to user

# End Script and WaterMark
print("Build by Amirsobhan Hosseinpour ! license: CC by sa... ")
input("Please enter key to end... ")
# Build by Amirsobhan Hosseinpour ! license: CC by sa.