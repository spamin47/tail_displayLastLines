import sys
import os


if len(sys.argv) == 3:
    if(str(sys.argv[2]).isdigit()):
        try:
            with open(sys.argv[1],"r+") as file:
                try:
                    last_lines = file.readlines()
                    for x in range(-int(sys.argv[2]),0):
                        print(last_lines[x])  
                except Exception:
                    print("Invalid second argument. File contains lines less than " + str(sys.argv[2]))
            
        except IOError:
            print("Invalid first argument. Could not find file " + str(sys.argv[1]))
    else:
        print("Invalid second argument. Argument is not a number.")

else:
    print("Wrong number of commands inputted.")
    print("Please input First argument: file, Second argument: last N lines")
    