#!/usr/bin/env python3

import os, sys

def updateForFirstTime():
    print("1.0 ------------ Updating for the first time the system !")
    print("1.1 ------------ Removing the db.lck file: sudo rm /var/lib/pacman/db.lck")
    os.system("sudo rm /var/lib/pacman/db.lck")
    print("1.2 ------------ Success!!!")
    print("1.3 ------------ Moving gnupg files to a old folder: sudo mv /etc/pacman.d/gnupg/ /etc/pacman.d/gnupgold")
    os.system("sudo mv /etc/pacman.d/gnupg/ /etc/pacman.d/gnupgold")
    print("1.4 ------------ Init keys with sudo pacman-key --init")
    os.system("sudo pacman-key --init")
    print("1.5 ------------ Populating keys with: sudo pacman-key --populate archlinux manjaro")
    os.system("sudo pacman-key --populate archlinux manjaro")
    print("1.6 ------------ Updating the system !")
    os.system("sudo pacman -Syyu")

def updateSystem():
    print("2 ------------ Updating the system !")
    os.system("sudo pacman -Syyu")

def updateSystem_IgnoreSomePackage(package_name):
    print("3 ------------ Update the system but ignore some package ?")
    print("Ignoring this package name: "+package_name)
    os.system("sudo pacman -Syyu --ignore="+package_name)

def updateSystem_IgnoreSomePackageGroup(package_group):
    print("4 ----------- Update the system but ignore some package group ?")
    print("Ignoring this package group: "+package_group)
    os.system("sudo pacman -Syyu --ignoregroup="+package_group)

def download_withWget(text_file_name1):
    print("5 ----------- Download with wget a .iso file ?")
    try:
        with open(text_file_name1) as file1:
            read_data1 = file1.readline()
        print("Downloading, please wait ... ")
        os.system("wget "+read_data1)
    except FileNotFoundError:
         print("Oops! There is no file with that name!")

def continue_download_withWget(text_file_name2):
    print("6 ----------- Continuing download with wget a .iso file ?")
    try:
        with open(text_file_name2) as file2:
            read_data2 = file2.readline()
        print("Downloading, please wait ... ")
        os.system("wget -c "+read_data2)
    except FileNotFoundError:
         print("Oops! There is no file with that name!")

def main():
    print("1 - Update for first time the system ?")
    print("2 - Update the system ?")
    print("3 - Update the system but ignore some package ?")
    print("4 - Update the system but ignore some package group ?")
    print("5 - Download with wget a .iso file ?")
    print("6 - Continuing download with wget a .iso file ?")
    print("7 - Exit ?")
    choice = input("What do you want to do ?  -->  ")
    if choice == "1":
        updateForFirstTime()
    elif choice == "2":
        updateSystem()
    elif choice == "3":
        package_to_ignore = input("Write the name of package to ignore ?  -->  ")
        updateSystem_IgnoreSomePackage(package_to_ignore)
    elif choice == "4":
        package_group_to_ignore = input("Write the name of package group to ignore ?  -->  ")
        updateSystem_IgnoreSomePackageGroup(package_group_to_ignore)
    elif choice == "5":
        text_file1 = input("Write the name of the text file with the url ?  -->  ")
        download_withWget(text_file1)
    elif choice == "6":
        text_file2 = input("Write the name of the text file with the url to continue download ?  -->  ")
        continue_download_withWget(text_file2)
    elif choice == "7":
        print("Exiting... !")
        sys.exit()

if __name__ == "__main__":
	main()
	sys.exit()

