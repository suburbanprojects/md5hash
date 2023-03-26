import tkinter as tk
import hashlib

app = tk.Tk()
app.title("MD5 hash")

def GenHash():
    global EnterBox
    text=EnterBox.get()
    text2 = text.encode('ascii')

    md5_hash = hashlib.md5()
    md5_hash.update(text2)
    result = md5_hash.hexdigest()
    
    ResultBox.delete(0, "end")
    ResultBox.insert(tk.INSERT, result)

EnterLabel = tk.Label(app, text="Enter text here: ")
EnterLabel.grid(column = 0, row = 0, ipadx=5, pady=5, sticky=tk.W+tk.N)
ResultLabel = tk.Label(app, text="md5 hash: ")
ResultLabel.grid(column = 0, row = 1, ipadx=5, pady=5, sticky=tk.W+tk.N)

EnterBox = tk.Entry(app, width=35)
EnterBox.grid(column=1,row=0,padx=10,pady=5, sticky=tk.N)
ResultBox = tk.Entry(app, width=35)
ResultBox.grid(column=1,row=1,padx=10,pady=5, sticky=tk.N)

resultButton = tk.Button(app, text='Get Hash', command=GenHash)
resultButton.grid(column=0, row=4, pady=10, sticky=tk.W)

app.mainloop()
