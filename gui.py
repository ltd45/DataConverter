import sys


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import gui_support
import Function
import tkinter.messagebox as messagebox

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('PDF Converter')
    geom = "610x244+650+150"
    root.geometry(geom)
    w = PDF_Converter (root)
    gui_support.init(root, w)
    root.mainloop()

w = None
def create_PDF_Converter(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('PDF_Converter')
    geom = "610x244+650+150"
    w.geometry(geom)
    w_win = PDF_Converter (w)
    gui_support.init(w, w_win, param)
    return w_win

def destroy_PDF_Converter():
    global w
    w.destroy()
    w = None


class PDF_Converter:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        master.configure(background="#d9d9d9")


        self.txtInput = Text(master)
        self.txtInput.place(relx=0.05, rely=0.2, relheight=0.14, relwidth=0.72)
        self.txtInput.configure(background="white")
        self.txtInput.configure(font="TkTextFont")
        self.txtInput.configure(foreground="black")
        self.txtInput.configure(highlightbackground="#d9d9d9")
        self.txtInput.configure(highlightcolor="black")
        self.txtInput.configure(insertbackground="black")
        self.txtInput.configure(selectbackground="#c4c4c4")
        self.txtInput.configure(selectforeground="black")
        self.txtInput.configure(width=294)
        self.txtInput.configure(wrap=WORD)

        self.txtOutput = Text(master)
        self.txtOutput.place(relx=0.05, rely=0.45, relheight=0.14, relwidth=0.72)
        self.txtOutput.configure(background="white")
        self.txtOutput.configure(font="TkTextFont")
        self.txtOutput.configure(foreground="black")
        self.txtOutput.configure(highlightbackground="#d9d9d9")
        self.txtOutput.configure(highlightcolor="black")
        self.txtOutput.configure(insertbackground="black")
        self.txtOutput.configure(selectbackground="#c4c4c4")
        self.txtOutput.configure(selectforeground="black")
        self.txtOutput.configure(width=294)
        self.txtOutput.configure(wrap=WORD)

        def inputbrowser_click():
            string = Function.browse()
            self.txtInput.insert(1.0, string)

        self.btnInput = Button(master, command=inputbrowser_click)
        self.btnInput.place(relx=0.83, rely=0.2, height=28, width=68)
        self.btnInput.configure(activebackground="#d9d9d9")
        self.btnInput.configure(activeforeground="#000000")
        self.btnInput.configure(background=_bgcolor)
        self.btnInput.configure(disabledforeground="#a3a3a3")
        self.btnInput.configure(foreground="#000000")
        self.btnInput.configure(highlightbackground="#d9d9d9")
        self.btnInput.configure(highlightcolor="black")
        self.btnInput.configure(pady="0")
        self.btnInput.configure(text='''Browse''')
        self.btnInput.configure(width=68)

        def output_click():
            string = Function.browse()
            self.txtOutput.insert(1.0, string)

        self.btnOutput = Button(master, command=output_click)
        self.btnOutput.place(relx=0.83, rely=0.45, height=28, width=68)
        self.btnOutput.configure(activebackground="#d9d9d9")
        self.btnOutput.configure(activeforeground="#000000")
        self.btnOutput.configure(background=_bgcolor)
        self.btnOutput.configure(disabledforeground="#a3a3a3")
        self.btnOutput.configure(foreground="#000000")
        self.btnOutput.configure(highlightbackground="#d9d9d9")
        self.btnOutput.configure(highlightcolor="black")
        self.btnOutput.configure(pady="0")
        self.btnOutput.configure(text='''Browse''')
        self.btnOutput.configure(width=68)

        def start():
            input=self.txtInput.get(1.0, END)
            output=self.txtOutput.get(1.0, END)
            i=Function.mainfunction(input.strip(), output.strip())
            messagebox.showinfo("Results", "The Result was: " + i)

        self.btnStart = Button(master, command=start)
        self.btnStart.place(relx=0.05, rely=0.74, height=28, width=98)
        self.btnStart.configure(activebackground="#d9d9d9")
        self.btnStart.configure(activeforeground="#000000")
        self.btnStart.configure(background=_bgcolor)
        self.btnStart.configure(disabledforeground="#a3a3a3")
        self.btnStart.configure(foreground="#000000")
        self.btnStart.configure(highlightbackground="#d9d9d9")
        self.btnStart.configure(highlightcolor="black")
        self.btnStart.configure(pady="0")
        self.btnStart.configure(text='''Start''')
        self.btnStart.configure(width=98)

        def exitcommand():
            sys.exit(0)

        self.btnExit = Button(master, command=exitcommand)
        self.btnExit.place(relx=0.66, rely=0.74, height=28, width=78)
        self.btnExit.configure(activebackground="#d9d9d9")
        self.btnExit.configure(activeforeground="#000000")
        self.btnExit.configure(background=_bgcolor)
        self.btnExit.configure(disabledforeground="#a3a3a3")
        self.btnExit.configure(foreground="#000000")
        self.btnExit.configure(highlightbackground="#d9d9d9")
        self.btnExit.configure(highlightcolor="black")
        self.btnExit.configure(pady="0")
        self.btnExit.configure(text='''Exit''')
        self.btnExit.configure(width=78)

        def clearcommand():
            self.txtInput.delete('1.0', END)
            self.txtOutput.delete('1.0', END)

        self.btnClear = Button(master, command=clearcommand)
        self.btnClear.place(relx=0.39, rely=0.74, height=28, width=71)
        self.btnClear.configure(activebackground="#d9d9d9")
        self.btnClear.configure(activeforeground="#000000")
        self.btnClear.configure(background=_bgcolor)
        self.btnClear.configure(disabledforeground="#a3a3a3")
        self.btnClear.configure(foreground="#000000")
        self.btnClear.configure(highlightbackground="#d9d9d9")
        self.btnClear.configure(highlightcolor="black")
        self.btnClear.configure(pady="0")
        self.btnClear.configure(text='''Clear''')
        self.btnClear.configure(width=71)



if __name__ == '__main__':
    vp_start_gui()



