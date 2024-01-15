import tkinter as tk
from tkinter import filedialog
import hashlib

class MD5Gui:
    def __init__(self, app):
        self.root = app
        self.app_layout()
        
    def app_layout(self):

        self.EnterLabel = tk.Label(app, text="File 1: ")
        self.EnterLabel.grid(column = 0, row = 0, ipadx=5, pady=5, sticky=tk.W+tk.N)
        self.ResultLabel = tk.Label(app, text="md5 hash: ")
        self.ResultLabel.grid(column = 0, row = 1, ipadx=5, pady=5, sticky=tk.W+tk.N)

        self.EnterLabel = tk.Label(app, text="File 2: ")
        self.EnterLabel.grid(column = 0, row = 2, ipadx=5, pady=5, sticky=tk.W+tk.N)
        self.ResultLabel = tk.Label(app, text="md5 hash: ")
        self.ResultLabel.grid(column = 0, row = 3, ipadx=5, pady=5, sticky=tk.W+tk.N)

        self.EnterBox = tk.Entry(app, width=50)
        self.EnterBox.grid(column=1,row=0,padx=10,pady=5, sticky=tk.N)
        self.ResultBox = tk.Entry(app, width=50)
        self.ResultBox.grid(column=1,row=1,padx=10,pady=5, sticky=tk.N)

        self.EnterBox2 = tk.Entry(app, width=50)
        self.EnterBox2.grid(column=1,row=2,padx=10,pady=5, sticky=tk.N)
        self.ResultBox2 = tk.Entry(app, width=50)
        self.ResultBox2.grid(column=1,row=3,padx=10,pady=5, sticky=tk.N)

        self.OpenFile = tk.Button(app, text='Open File 1', command=self.openFile)
        self.OpenFile.grid(column=3, row=0)

        self.OpenFile = tk.Button(app, text='Open File 2', command=self.openFile2)
        self.OpenFile.grid(column=3, row=2)

        self.CompareHash = tk.Button(app, text='Compare Hash', command=self.compareHash)
        self.CompareHash.grid(column=0,row=4,padx=10,pady=5, sticky=tk.N)

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

    def openFile2(self):
        self.filename = filedialog.askopenfilename(initialdir="/",title="Dialog Box",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files","*.*")))
        self.EnterBox2.delete(0, "end")
        self.EnterBox2.insert(tk.END, self.filename)

        self.md5_hash = hashlib.md5()
        with open(self.filename, "rb") as f:
                  for byte_block in iter(lambda: f.read(4096),b''):
                      self.md5_hash.update(byte_block)
                  self.ResultBox2.delete(0, "end") 
                  self.ResultBox2.insert(tk.END, self.md5_hash.hexdigest())

    def compareHash(self):

        hash_a = self.ResultBox.get()
        hash_b = self.ResultBox2.get()

        if hash_a == hash_b:
             self.labelMessage = tk.Label(app, text="Hashes Match")
             self.labelMessage.grid(column=1,row=4,padx=10,pady=5, sticky=tk.N)

        else:
             self.labelMessage = tk.Label(app, text="Hashes Don't Match")
             self.labelMessage.grid(column=1,row=4,padx=10,pady=5, sticky=tk.N)

if __name__ == "__main__":
    app = tk.Tk()
    app.title("MD5 File Hash")
    app2 = MD5Gui(app)
    app.mainloop()
