import tkinter as tk

def on_close():
    print("Application closed")
    root.destroy()

root = tk.Tk()
root.title("Desktop App")
label = tk.Label(root, text="Hello, this is your Python desktop app!")
label.pack(pady=20)

close_button = tk.Button(root, text="Close", command=on_close)
close_button.pack(pady=10)

root.mainloop()
