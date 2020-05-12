#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
#
#  name of file: specs.py
#  
#  Copyright 2013 Filipe Marques <eagle.software3@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You received a copy of the GNU General Public License
#  along with this program in License folder; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

#importing the necessary modules
import sys # module of the standard python library
import platform # module of the standard python library
#import textwrap # module of the standard python library
from src_specs.system import System # from package.module import class
from src_specs.development import Development # from package.module import class

documentation = """******************************************************************************************
***  Copyright 2013 Filipe Marques <eagle.software3@gmail.com>                         ***
***  This program show the specifications of systems like: Linux;                      ***
***  Instead of typing every time a command in the console, this program puts together *** 
***    the most important commands to give important information from a system.        ***
***                                                                                    ***
***  With this program you can know the most important informations about your system, ***
***    for this uses:                                                                  ***
***        1 - You need to know the specifications of your pc, laptop,... systems for  ***
***                installing others operating systems;                                ***
***        2 - To check if you buy the expected hardware that you wanted;              ***
***        3 - Just for curiosity and learning.                                        ***
***                                                                                    ***
***  For checking the hardware in your Windows and Mac OS X machine, I advice you to   ***
***    to run a copy of a live linux distribution in a pen USB with python3 installed  ***
***    and from there you can run the specs program without any problems.              ***
***                                                                                    ***
***                                                                                    ***
***       Spread the word, fork, star and please contribute to this project!           ***
***              Git Repo at: https://github.com/filipe-marques/specs.git              ***
***                                                                                    ***
***                                                                                    ***
***   Execute this program with the console window fully maximized!                    ***
***                                                                                    ***
***                                                                                    ***
***  For development purposes (this is the default) execute this program in console    ***
***   doing this:  command-line: python3 specs.py                                      ***
***                                                                                    ***
***  For execution purposes execute this program in console doing this:                ***
***     command-line: chmod +x specs.py (do this just one time. what this does is that ***
***                                      give a executable mode to the file)           ***
***                                                                                    ***
***  Every time that you want execute the program do this:                             ***
***     command-line: ./specs.py                                                       ***
***                                                                                    ***
***------------------------------------------------------------------------------------***
***                                                                                    ***
***  This program is free software; you can redistribute it and/or modify              ***
***  it under the terms of the GNU General Public License as published by              ***
***  the Free Software Foundation; either version 3 of the License, or                 ***
***  any later version.                                                                ***
***                                                                                    ***
***  This program is distributed in the hope that it will be useful,                   ***
***  but WITHOUT ANY WARRANTY; without even the implied warranty of                    ***
***  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                     ***
***  GNU General Public License for more details.                                      ***
***                                                                                    ***
***  You should have received a copy of the GNU General Public License                 ***
***  along with this program; if not, write to the Free Software                       ***
***  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.    ***
***  or go to www.fsf.org                                                              ***
***                                                                                    ***
******************************************************************************************
"""

print(documentation)

print("THE OPTIONS ARE: ")
print(" 1 - SHOW THE SPECIFICATIONS OF THE SYSTEM")
print(" 2 - LIST VERSION NUMBERS OF CRITICAL DEVELOPMENT TOOLS - ONLY FOR LINUX MACHINES")
print(" 3 - EXIT FROM THE PROGRAM ")
try:
    option = int(input("YOUR OPTION IS:  ")) # converts a string to a integer and read the value with input
except ValueError as e:
    print(e, " - The value is not valid, please enter a valid value!")



# instantiation of the two classes
syst = System()
develop = Development()

if option == 1:
    print("YOU HAVE CHOSEN THE OPTION (1 - SHOW THE SPECIFICATIONS OF THE SYSTEM)\n") # \n - puts another line
    if platform.system() == "Linux":
        syst.linux_machine() # object.method_name()
    elif platform.system() == "MacOSX":
        syst.macos_machine() # object.method_name()
    elif platform.system() == "Windows":
        syst.windows_machine() # object.method_name()
                
elif option == 2:
    print("YOU HAVE CHOSEN THE OPTION (2 - LIST VERSION NUMBERS OF CRITICAL DEVELOPMENT TOOLS - ONLY FOR LINUX MACHINES)\n") # - puts another line
    if platform.system() == "Linux":
        develop.linux() # object.method_name()

elif option == 3:
    print("YOU HAVE CHOSEN THE OPTION (3 - EXIT FROM THE PROGRAM)")
    sys.exit()

if __name__ == '__main__':
    pass
