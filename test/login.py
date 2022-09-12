import tkinter as tk

root = tk.Tk()
root.title("Login System")
root.geometry("300x125")

tk.Label(root, text="IP:").pack()
tk.Entry(root, width=20).pack()
tk.Label(root, text="Port:").pack()
tk.Entry(root, width=20).pack()
tk.Button(root, text="login").pack()

root.mainloop()