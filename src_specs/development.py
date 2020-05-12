#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
#
#  name of file: development.py
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
import os

# this class don't have the construct method def __init__(): , because this class only return data
class Development:
    def linux(self):
        print("LIST VERSION NUMBERS OF CRITICAL DEVELOPMENT TOOLS")
        print("") # spacing
        print("----------->THE BASH VERSION:")
        os.system('bash --version | head -n1 | cut -d" " -f2-4') # executes the command-line
        print("") # spacing
        print("----------->THE BINUTILS VERSION:")
        os.system('ld --version | head -n1 | cut -d" " -f3-') # executes the command-line
        print("") # spacing
        print("----------->THE BISON VERSION:")
        os.system('bison --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE BZIP2 VERSION:")
        os.system('bzip2 --version 2>&1 < /dev/null | head -n1 | cut -d" " -f1,6-') # executes the command-line
        print("") # spacing
        print("----------->THE GNU COREUTILS VERSION:")
        os.system('chown --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE GNU DIFFUTILS VERSION:")
        os.system('diff --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE GNU FINDUTILS VERSION:")
        os.system('find --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE GNU AWK VERSION:")
        os.system('gawk --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE GNU GCC VERSION:")
        os.system('gcc --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE EGLIBC VERSION:")
        os.system('ldd --version | head -n1 | cut -d" " -f2-') # executes the command-line
        print("") # spacing
        print("----------->THE GNU GREP VERSION:")
        os.system('grep --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE GZIP VERSION:")
        os.system('gzip --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE GNU M4 VERSION:")
        os.system('m4 --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE GNU MAKE VERSION:")
        os.system('make --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE PATCH VERSION:")
        os.system('patch --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE PERL VERSION:")
        os.system('perl -V:version') # executes the command-line
        print("") # spacing
        print("----------->THE GNU SED VERSION:")
        os.system('sed --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE GNU TAR VERSION:")
        os.system('tar --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE MAKEINFO VERSION:")
        os.system('makeinfo --version | head -n1') # executes the command-line
        print("") # spacing
        print("----------->THE XZ UTILS VERSION:")
        os.system('xz --version | head -n1') # executes the command-line

if __name__ == '__main__':
    pass