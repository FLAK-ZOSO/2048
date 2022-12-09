import tkinter as tk


class Board(tk.Frame):
    height = 4
    width = 4

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        
        self.main_grid = tk.Frame(
            self, bg="#ffffff", bd=3, width=4, height=4
        )
        self.main_grid.grid(pady=(100, 0))

if __name__ == "__main__":
    Board().mainloop()