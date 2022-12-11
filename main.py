import tkinter as tk
from copy import deepcopy
from random import randint


class Board(tk.Frame):
    height = 4
    width = 4

    def __init__(self):
        self.matrix: list[list[int]] = [
            [0, 0, 0, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 0, 0]
        ] # 0 is empty

        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        
        self.main_grid = tk.Frame(
            self, bg="#ffffff", bd=3, width=4, height=4
        )
        self.main_grid.grid(pady=100, padx=100)

    # Simula il movimento in una direzione e ritorna una matrice con il risultato
    def simula(self, matrix: list[list[int]], direction: str) -> None | list[list[int]]:
        match (direction):
            case "RIGHT":
                for row in matrix:
                    while (True):
                        if (row[3] == 0 and row[2] == 0 and row[1] == 0 and row[0] == 0): # Se tutti gli elementi sono vuoti...
                            break
                        elif (row[3] == 0 and row[2] == 0 and row[1] == 0): # Se gli ultimi tre elementi sono vuoti...
                            row[3] = row[0]
                            row[0] = 0
                        elif (row[3] == 0 and row[2] == 0): # Se gli ultimi due elementi sono vuoti...
                            row[3] = row[1]
                            row[2] = row[0]
                            row[1] = 0
                            row[0] = 0
                        elif (row[3] == 0): # Se l'ultimo elemento è vuoto...
                            # ... sposta tutto a destra
                            row[3] = row[2]
                            row[2] = row[1]
                            row[1] = row[0]
                            row[0] = 0
                        
                        if (row[3] == row[2] or row[2] == row[1] or row[1] == row[0]): # Se ci sono due elementi uguali...
                            for i in range(3, 0, -1):
                                if (row[i] == row[i-1]):
                                    row[i] *= 2
                                    row[i-1] = 0
                                    break
                        else:
                            break
            case "UP":
                ...
            case "DOWN":
                ...
            case "LEFT":
                ...
            case _:
                raise ValueError("Invalid direction")

    # Controlla se la partita è finita:
    def controlla(self) -> bool | list[list[int]]:
        # Prova a spostare tutto a destra, poi controlla se è cambiato qualcosa
        right = self.simula(deepcopy(self.matrix), "RIGHT");
        # Prova a spostare tutto in alto, poi controlla se è cambiato qualcosa
        up = self.simula(deepcopy(self.matrix), "UP");
        if (up != None): # 
            return up
        # Prova a spostare tutto in basso, poi controlla se è cambiato qualcosa
        down = self.simula(deepcopy(self.matrix), "DOWN");
        # Prova a spostare tutto a sinistra, poi controlla se è cambiato qualcosa
        left = self.simula(deepcopy(self.matrix), "LEFT");


if __name__ == "__main__":
    Board().mainloop()