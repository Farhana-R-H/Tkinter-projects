
import tkinter as tk
def show_message():
    name=entry.get()
    label_result.config(text=f'HELLO, {name}!....')
root=tk.Tk()
root.title("GREETING APP")
root.geometry("600x200")

label=tk.Label(root, text="ENTER YOUR NAME")
label.pack()

entry=tk.Entry(root)
entry.pack()

button=tk.Button(root,text="GREET",command=show_message)
button.pack()

label_result=tk.Label(root)
label_result.pack()
root.mainloop()