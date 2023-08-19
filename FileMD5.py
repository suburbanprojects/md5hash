import tkinter as tk
from tkinter import filedialog
import hashlib

class MD5Gui:
    def __init__(self, app):
        self.root = app
        self.app_layout()
        
    def app_layout(self):
        self.EnterLabel = tk.Label(app, text="File: ")
        self.EnterLabel.grid(column = 0, row = 0, ipadx=5, pady=5, sticky=tk.W+tk.N)
        self.ResultLabel = tk.Label(app, text="md5 hash: ")
        self.ResultLabel.grid(column = 0, row = 1, ipadx=5, pady=5, sticky=tk.W+tk.N)

        self.EnterBox = tk.Entry(app, width=50)
        self.EnterBox.grid(column=1,row=0,padx=10,pady=5, sticky=tk.N)
        self.ResultBox = tk.Entry(app, width=50)
        self.ResultBox.grid(column=1,row=1,padx=10,pady=5, sticky=tk.N)

        self.OpenFile = tk.Button(app, text='Open File', command=self.openFile)
        self.OpenFile.grid(column=3, row=0)

    def openFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/",title="Dialog Box",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files","*.*")))
        self.EnterBox.delete(0, "end")
        self.EnterBox.insert(tk.END, self.filename)

        self.md5_hash = hashlib.md5()
        with open(self.filename, "rb") as f:
                  for byte_block in iter(lambda: f.read(4096),b''):
                      self.md5_hash.update(byte_block)
                  self.ResultBox.delete(0, "end") 
                  self.ResultBox.insert(tk.END, self.md5_hash.hexdigest())
                
               
if __name__ == "__main__":
    app = tk.Tk()
    app.title("MD5 File Hash")
    app2 = MD5Gui(app)
    app.mainloop()
