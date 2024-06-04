from tkinter import *
import random

def restart():
    global player

    player = random.choice(characters)
    label.config(text=player + " 's turn ")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player

        if check_winner():
            label.config(text=(player + " won"))
        elif check_winner() == "Tie":
            label.config(text="Tie")
        else:
            player = characters[(characters.index(player) + 1) % 2]
            label.config(text=(player + " 's turn"))

def check_winner():
    # Check rows and columns for a winner
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True

    # Check diagonals for a winner
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        return True

    # Check for tie
    if not empty_spaces():
        return "Tie"
    return False

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

# Create the board for the game
board = Tk()
board.title("Tic-Tac-Toe")

# Create the list of characters
characters = ["x", "o"]

# Create the buttons in a two-dimensional array or list
buttons = [['', '', ''],
           ['', '', ''],
           ['', '', '']]

player = random.choice(characters)

# The status bar letting the players know whose turn it is
label = Label(text=player + " 's turn", font=('futura', 40))
label.pack(side="top")

new_game_button = Button(text="New game", font=('futura', 20), command=restart)
new_game_button.pack(side="top")

# Create the frame
frame = Frame(board)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

board.mainloop()
