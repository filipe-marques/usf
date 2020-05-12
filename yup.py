#!/usr/bin/python3

#	Copyright 2014 2015 2016 Filipe Marques <eagle.software3@gmail.com>
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

import re, sys, urllib.request

# Uma classe é um novo tipo de dados definido pelo utilizador
# só se utiliza parenteses quando se herda classes
class YoutubeUrlParser:
    
    def find_urls(self, name_file):
        with open(name_file,'r') as file_input:
            file_input1 = file_input.read()
        try:
            links = re.findall(r'<a.*?href="(.*?)"',file_input1)
            with open(name_file+'.txt','w') as file_input2:
            #fi = open(name_file+'.txt','w')
                for link in links:
                    #print(link)
                    file_input2.write(link)
                    file_input2.write('\n')
                #fi.close()
        except IOError as err:
            print("I/O error: {0}".format(err))
    
    def analyze_data(self, file_name):
        with open(file_name+'.txt','r') as fi:
            f = fi.readlines()
        try:
            with open(file_name+'.txt','w') as fi:
                #file_links_input_again = open(file_name+'.txt','w')
                # mostra o tipo de dados da variável
                #print(type(f))
                for lin in f:
                    if 'http://www.youtube.com/watch?v=' in lin or 'https://www.youtube.com/watch?v=' in lin:
                        # se este url é igual ao outro a seguir, removi-o da list
                        if lin == lin:
                            f.remove(lin)
                            #print(lin)
                            fi.write(lin)
                            #print(type(lin))
                            #print(type(file_links_input_again))
                            #file_links_input_again.close()
        except IOError as err:
            print("I/O error: {0}".format(err))
    
    def online_analyze_data(self, file_name):
        with open(file_name+'.txt','r') as fi:
            f = fi.readlines()
        try:
            with open(file_name+'.txt','w') as fi:
                #file_links_input_again = open(file_name+'.txt','w')
                # mostra o tipo de dados da variável
                #print(type(f))
                for lin in f:
                    if '/watch?v=' in lin:
                        # se este url é igual ao outro a seguir, removi-o da list
                        if lin == lin:
                            f.remove(lin)
                            #print(lin)
                            fi.write("https://www.youtube.com"+lin)
                            #print(type(lin))
                            #print(type(file_links_input_again))
                            #fi.close()
        except IOError as err:
            print("I/O error: {0}".format(err))
            
    def online_find_urls(self, url, name_of_file):
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read()
            # prints bytes type
            #print(type(html))
            # pass bytes type to str type
            ht = html.decode(encoding="utf-8", errors="strict")
            # prints str type
            #print(type(ht))
            with open('provisory-html.txt', 'w') as fil:
                ff = fil.write(ht)
            self.find_urls('provisory-html.txt')
            self.online_analyze_data("provisory-html.txt")
        except Exception as err:
            print("Exception error: {0}".format(err)+"\n maybe try to do it in offline mode ...")
            self.find_urls(name_of_file)
            self.analyze_data(name_of_file)
            print("Done !!!")
        
def main():
    # https://www.youtube.com/watch?v=QR_L0gmwg10
    # instanciar a classe
    do_job = YoutubeUrlParser()
    # aceder aos métodos da classe
    #if "http://" or "https://" in str(sys.argv[1]):
    do_job.online_find_urls(sys.argv[1], sys.argv[1])
        
    #if "http://" or "https://" not in sys.argv[1]:
    #    do_job.find_urls(sys.argv[1])
    #    do_job.analyze_data(sys.argv[1])
    #else:
    #    do_job.online_find_urls(sys.argv[1])
    # esta variável do_job é do tipo de dados YoutubeUrlParser
    #print(type(do_job))

if "__main__" == __name__:
    main()
