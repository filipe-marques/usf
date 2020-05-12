#!/usr/bin/python3

#	Copyright 2014 Filipe Marques <eagle.software3@gmail.com>
#  
#	This program is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; either version 3 of the License, or
#	any later version.
#  
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#  
#	You received a copy of the GNU General Public License
#	along with this program in License folder; if not, write to the Free Software
#	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#	MA 02110-1301, USA.

import os, sys

def downloader_in_linux(file_name):
	with open(file_name, 'r') as fi:
		url = fi.readlines()
	
	f = open(file_name+'_downloaded.txt', 'w')
	for d in url:
		#print(type(d))
		print(os.system("./youtube-dl -t "+d))
		print("URL: "+d)
		df = d.replace(d, "'"+d)
		f.write(df)
		#f.write("\n")
	f.close()

def downloader_in_windows(fil_name):
	with open(fil_name, 'r') as fi:
		url = fi.readlines()
	
	f = open(fil_name+'_downloaded.txt', 'w')
	for d in url:
		#print(type(d))
		print(os.system("youtube-dl -t "+d))
		print("URL: "+d)
		df = d.replace(d, "'"+d)
		f.write(df)
		#f.write("\n")
	f.close()

def main():
	print("WELCOME TO DOWNLOADER! version 1.0.0")
	print("TO EXIT PRESS: p")
	stop = input("Exit ?: ")
	if 'p' in stop:
		sys.exit()
	else:
		if sys.platform == 'win32':
			downloader_in_windows(sys.argv[1])
		elif sys.platform == 'linux':
			downloader_in_linux(sys.argv[1])

if __name__ == "__main__":
	main()
	sys.exit()
