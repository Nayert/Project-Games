import tkinter as tk

root = tk.Tk()
root.title("My Tk App")
root.geometry("400x300")
root.resizable(False,False)

tk.Label(root, text="Username").grid(row=0, column=0, sticky="e")
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0, sticky="e")
tk.Entry(root, show="*").grid(row=1, column=1)

tk.Button(root, text="Login").grid(row=2, column=0, columnspan=2)
root.mainloop()



