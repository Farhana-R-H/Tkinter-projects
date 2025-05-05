import tkinter as tk
root=tk.Tk()
root.geometry("300x200")
tk.Label(root,text="USERNAME").grid(row=0, column=0)
tk.Entry(root).grid(row=0 ,column=1)
tk.Label(root,text="PASSWORD").grid(row=1, column=0)
tk.Entry(root, show="*").grid(row=1,column=1)
tk.Button(root, text="LOGIN").grid(row=2 ,column=0 ,columnspan=2)
root.mainloop()