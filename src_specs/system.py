#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
#
#  name of file: system.py
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

#importing modules from the standard python library
import os, platform 

# this class don't have the construct method def __init__(): , because this class only return data
class System:
    # linux_machine function
    def linux_machine(self):
        print("THE RESUME OF THE LINUX SYSTEM:")
        print("") # spacing
        print("----------->THE X SERVER VERSION:")
        os.system('X -version') # executes the command-line X -version
        print("") # spacing
        print("----------->THE JAVA JDK OR JRE VERSION:\n") # \n - puts another line
        os.system('java -version') # executes the command-line java -version
        print("") # spacing
        print("----------->THE HARDWARE IN THE MACHINE:\n") # \n - puts another line
        os.system('lspci -v') # executes the command-line lspci - lists the hardware in the system
        print("") # spacing
        print("----------->THE ACTUAL USAGE OF THE DISK OR PARTITION BY THE OPERATING SYSTEM IN THE MACHINE:\n") # \n - puts another line
        os.system('df --total') # executes the command-line df --total - lists the actual usage of the disk or partition by the operating system
        print("") # spacing
        print("----------->THE RAM MEMORY IN THE MACHINE (IN KILOBYTES):\n") # \n - puts another line
        os.system('free') # executes the command-line free - lists the ram memory in the system
        print("") # spacing
        print("----------->THE NETWORK INFORMATION IN THE MACHINE:\n") # \n - puts another line
        os.system('ifconfig') # executes the command-line ifconfig - lists the related information between the machine and the network
        print("") # spacing
        print("----------->OTHER IMPORTANT INFORMATIONS:\n") # \n - puts another line
        # plat is a variable that is assign to platform.uname() that will return a tuple 
        plat = platform.uname()
        print("The name of the operating system is....:" , plat[0]) # indexing at the position 0 of the tuple
        print("The computer network name is...........:" , plat[1]) # indexing at the position 1 of the tuple
        print("The system release is..................:" , plat[2]) # indexing at the position 2 of the tuple
        print("The system release version is..........:" , plat[3]) # indexing at the position 3 of the tuple
        print("The machine type is....................:" , plat[4]) # indexing at the position 4 of the tuple
        print("The (real) processor name is...........:" , plat[5]) # indexing at the position 5 of the tuple
        print("") # spacing
        return
    
    # macos_machine function
    def macos_machine(self):
        print("THE RESUME OF THE MAC OS X SYSTEM:")
        print("") # spacing
        print("Do you have a macintosh ?")
        print("Please, contribute to this project!\n") # \n - puts another line
        # plat is a variable that is assign to platform.uname() that will return a tuple
        plat1 = platform.uname()
        print("The name of the operating system is....:" , plat1[0]) # indexing at the position 0 of the tuple
        print("The computer network name is...........:" , plat1[1]) # indexing at the position 1 of the tuple
        print("The system release is..................:" , plat1[2]) # indexing at the position 2 of the tuple
        print("The system release version is..........:" , plat1[3]) # indexing at the position 3 of the tuple
        print("The machine type is....................:" , plat1[4]) # indexing at the position 4 of the tuple
        print("The (real) processor name is...........:" , plat1[5]) # indexing at the position 5 of the tuple
        print("") # spacing
        return
    
    # windows_machine function
    def windows_machine(self):
        print("THE RESUME OF THE WINDOWS SYSTEM:")
        print("") # spacing
        print("----------->THE JAVA JDK OR JRE VERSION:\n") # \n - puts another line
        os.system('java -version') # executes the command-line java -version
        print("") # spacing
        print("----------->THE NETWORK INFORMATION IN THE MACHINE:\n") # \n - puts another line
        os.system('ipconfig') # executes the command-line ipconfig - lists the related information between the machine and the network
        print("") # spacing
        print("----------->OTHERS IMPORTANT INFORMATIONS:\n") # \n - puts another line
        # plat is a variable that is assign to platform.uname() that will return a tuple
        plat2 = platform.uname()
        print("The name of the operating system is....:" , plat2[0]) # indexing at the position 0 of the tuple
        print("The computer network name is...........:" , plat2[1]) # indexing at the position 1 of the tuple
        print("The system release is..................:" , plat2[2]) # indexing at the position 2 of the tuple
        print("The system release version is..........:" , plat2[3]) # indexing at the position 3 of the tuple
        print("The machine type is....................:" , plat2[4]) # indexing at the position 4 of the tuple
        print("The (real) processor name is...........:" , plat2[5]) # indexing at the position 5 of the tuple
        print("") # spacing
        return



if __name__ == '__main__':
    pass