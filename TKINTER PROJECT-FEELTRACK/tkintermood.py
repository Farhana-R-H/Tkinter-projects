import tkinter as tk
from datetime import datetime

# Save Mood Function
def save_mood():
    mood = mood_var.get()
    note = entry_note.get()
    
    if mood == "":
        label_result.config(text="❗ Please select a mood.")
        return
    
    if note.strip() == "":
        label_result.config(text="❗ Please enter a note.")
        return
    
    with open("mood_journal.txt", "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {mood} - {note}\n")
    
    label_result.config(text="✅ Mood Saved!")
    entry_note.delete(0, tk.END)

# View Entries Function
def view_entries():
    try:
        with open("mood_journal.txt", "r") as file:
            entries = file.read()
    except FileNotFoundError:
        entries = "No entries found."

    view_window = tk.Toplevel(root)
    view_window.title("Mood Entries")
    view_window.geometry("500x400")
    view_window.configure(bg="#fff")

    text_area = tk.Text(view_window, wrap="word", font=("Segoe UI", 10))
    text_area.insert(tk.END, entries)
    text_area.config(state="disabled")
    text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Root Window
root = tk.Tk()
root.title("🌈 Mood Journal")
root.geometry("500x380")
root.configure(bg="#f0f8ff")

emoji_font = ("Segoe UI Emoji", 11)
label_font = ("Segoe UI", 11, "bold")

# Title Label
label_title = tk.Label(root, text="🌤️ Select Your Mood:", font=label_font, bg="#f0f8ff", fg="#333")
label_title.pack(pady=(10, 0))

# Mood Options Frame
mood_frame = tk.Frame(root, bg="#f0f8ff")
mood_frame.pack()

mood_var = tk.StringVar()

tk.Radiobutton(mood_frame, text="😊 Happy", variable=mood_var, value="Happy", font=emoji_font, bg="#f0f8ff", anchor="w", width=20).pack(anchor="w")
tk.Radiobutton(mood_frame, text="😢 Sad", variable=mood_var, value="Sad", font=emoji_font, bg="#f0f8ff", anchor="w", width=20).pack(anchor="w")
tk.Radiobutton(mood_frame, text="😡 Angry", variable=mood_var, value="Angry", font=emoji_font, bg="#f0f8ff", anchor="w", width=20).pack(anchor="w")
tk.Radiobutton(mood_frame, text="😴 Tired", variable=mood_var, value="Tired", font=emoji_font, bg="#f0f8ff", anchor="w", width=20).pack(anchor="w")
tk.Radiobutton(mood_frame, text="🤩 Excited", variable=mood_var, value="Excited", font=emoji_font, bg="#f0f8ff", anchor="w", width=20).pack(anchor="w")

# Note Label and Entry
label_note = tk.Label(root, text="📝 Write a short note:", font=label_font, bg="#f0f8ff", fg="#333")
label_note.pack(pady=(10, 0))

entry_note = tk.Entry(root, width=40, font=("Segoe UI", 10))
entry_note.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

button_save = tk.Button(button_frame, text="💾 Save Mood", command=save_mood,
                        bg="#4CAF50", fg="white", activebackground="#45a049",
                        font=("Segoe UI", 10, "bold"), padx=10, pady=5)
button_save.pack(side="left", padx=10)

button_view = tk.Button(button_frame, text="📖 View Entries", command=view_entries,
                        bg="#2196F3", fg="white", activebackground="#1976D2",
                        font=("Segoe UI", 10, "bold"), padx=10, pady=5)
button_view.pack(side="left", padx=10)

# Result Label
label_result = tk.Label(root, text="", bg="#f0f8ff", fg="green", font=("Segoe UI", 10))
label_result.pack()

root.mainloop()
