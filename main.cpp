/*
    Copyright 2014 2015 Filipe Marques <eagle.software3@gmail.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You received a copy of the GNU General Public License
    along with this program in License folder; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
    MA 02110-1301, USA.
*/
#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream file(argv[1], ios::in);
    if(!file.is_open())
    {
        cerr << "File not open !" << "\n";
        cerr << "This program expects an argument that is a name of a text file like text.txt !!!" << "\n";
        return 1;
    }
    string output;
    output = argv[1];
    output.append("_downloaded.txt");
    ofstream file_out(output.c_str(), ios::out);
    if(!file.is_open())
    {
        cerr << "File output not open !" << "\n";
        return 1;
    }
    cout << "Welcome to AutoDown (console program) version 1.0.0" << "\n";
    cout << "This program licensed under: GNU GPL v.3" << "\n";
    cout << "You can find the source code at: https://github.com/filipe-marques/utils" << "\n";
    cout << "" << "\n";
    cout << "" << "\n";
    cout << "Output file: " << output.c_str() << "\n";
    cout << "" << "\n";
    cout << "" << "\n";
    int i = 0;
    while (!file.eof())
    {
        string line, command;
        command = "./youtube-dl -t ";
        line.clear();
        file >> line;
        command.append(line);
        cout << "DOWNLOADING: " << command.c_str() << "\n";
        i = i + 1;
        system(command.c_str());
        cout << "DOWNLOADED: " << i << " - " << line.c_str() << "\n";
        cout << "------------------------------------------------------------" << "\n";
        //--------------------------------------------------------------------------
        // write the 'url in a file called argv[1]_downloaded.txt
        file_out << "'" << line << "\n";
        //--------------------------------------------------------------------------
        if(file.eof())
            break;
    }
    file.close();
    cout << "Closing file ... " << argv[1] << " ... Done !!!" << "\n";
    file_out.close();
    cout << "Closing file ... " << output.c_str() << " ... Done !!!" << "\n";
    return 0;
}
