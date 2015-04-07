import tkinter
import tkinter.filedialog
import myConverter
import urllib.request as urllib


def browse():
    in_path = tkinter.filedialog.askopenfilename()
    return in_path

def mainfunction(input, output):
    #response = urllib.urlopen(input)
    #html = response.read()
    #myConverter.htmlToCsv(html, output)
    return "You did not do anything moron."
