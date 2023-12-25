from tkinter import Tk, ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme="arc")
root.geometry("720x720")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()