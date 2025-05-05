import tkinter as tk
def calculator():
    try:
        result=eval(entry.get())
        label_result.config(text="Result: " + str(result))
    except:
        label_result.config(text="Error in Expression")

root=tk.Tk()
root.title("CALCULATOR")
root.geometry("600x200")

label=tk.Label(root, text="ENTER VALUE")
label.pack()

entry=tk.Entry(root ,width=30)
entry.pack(pady=20)

button=tk.Button(root,text="CALCULATE",command=calculator)
button.pack()

label_result=tk.Label(root)
label_result.pack()
root.mainloop()