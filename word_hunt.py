import sys
import tkinter as tk
from tkinter import *


max_word_length = 9
board_width = 0
board_height = 0
three_letter_starts = set()
four_letter_starts = set()


def find_words(board, i, j, word, found_words, visited, word_set):#i and j are coordinates
    word += board[i][j]
    visited.add((i, j))
   # print(word)
    if len(word) == 3:
        if word not in three_letter_starts:
            return -1
    elif len(word) == 4:
        if word not in four_letter_starts:
            return -1
    if word in word_set:
        found_words.add(word.upper())
    if len(word) > max_word_length:
        return -1
    if i - 1 > -1 and j - 1 > -1 and board[i - 1][j - 1] != "#" and (i-1, j-1) not in visited:#Top Left
        find_words(board, i-1, j-1, word, found_words, visited.copy(), word_set)
    if j - 1 > -1 and board[i][j - 1] != "#" and (i, j-1) not in visited:#Up
        find_words(board, i, j-1, word, found_words, visited.copy(), word_set)
    if i + 1 < board_width and j - 1 > -1 and board[i+1][j-1] != "#" and (i+1, j-1) not in visited:#Top Right
        find_words(board, i+1, j-1, word, found_words, visited.copy(), word_set)
    if i - 1 > -1 and board[i-1][j] != "#" and (i-1, j) not in visited:#Left
        find_words(board, i-1, j, word, found_words, visited.copy(), word_set)
    if i + 1 < board_width and board[i+1][j] != "#" and (i+1, j) not in visited:#Right
        find_words(board, i+1, j, word, found_words, visited.copy(), word_set)
    if i - 1 > -1 and j + 1 < board_height and board[i-1][j+1] != "#" and (i-1, j+1) not in visited:#Bottom Left
        find_words(board, i-1, j+1, word, found_words, visited.copy(), word_set)
    if j + 1 < board_height and board[i][j+1] != "#" and (i, j+1) not in visited:#Down
        find_words(board, i, j+1, word, found_words, visited.copy(), word_set)
    if i+1 < board_width and j+1 < board_height and board[i+1][j+1] != "#" and (i+1, j+1) not in visited:#Bottom Right
        find_words(board, i+1, j+1, word, found_words, visited.copy(), word_set)
    return found_words




def get_board():
    global board_width
    global board_height
    global three_letter_starts
    global four_letter_starts
    filename = "scrabble.txt"
    string = ""
    option = var.get()
    if option == 1:
        for i in range(len(entry1_lis)):
            string += str(entry1_lis[i].get())
        input = string.upper()
        board = []
        for i in range(4):
            lis = []
            for j in range(4):
                lis.append(input[4*i + j])
                if j == 3:
                    board.append(lis)
    if option == 2: #GWW#AHUIDLS#POKEKOL#FLL#
        for i in range(len(entry2_lis)):
            string += str(entry2_lis[i].get())
        input = string.upper()
        input = "#" + input
        input = input[:3] + "#" + input[3:]
        input = input[:12] + "#" + input[12:]
        input = input[:20] + "#" + input[20:]
        input = input + "#"
        board = []
        for i in range(5):
            lis = []
            for j in range(5):
                lis.append(input[5*i + j])
                if j == 4:
                    board.append(lis)
    if option == 3:# UI#QWIWRCE#UOP#OHPEOPI#NL
        for i in range(len(entry3_lis)):
            string += str(entry3_lis[i].get())
        input = string.upper()
        input = input[:2] + "#" + input[2:]
        input = input[:10] + "#" + input[10:]
        input = input[:14] + "#" + input[14:]
        input = input[:22] + "#" + input[22:]
        board = []
        for i in range(5):
            lis = []
            for j in range(5):
                lis.append(input[5*i + j])
                if j == 4:
                    board.append(lis)
    if option == 4:
        for i in range(len(entry4_lis)):
            string += str(entry4_lis[i].get())
        input = string.upper()
        board = []
        for i in range(5):
            lis = []
            for j in range(5):
                lis.append(input[5*i + j])
                if j == 4:
                    board.append(lis)







    characters = set(input)
    if "#" in characters:
        characters.remove("#")
    three_letter_starts = set()
    four_letter_starts = set()
    word_set = set()
    board_width = len(board)
    board_height = len(board[0])
    #Dictionary, where key is start of word and value is the word itself
    with open(filename) as f:
            for line in f:
                word = line.strip().upper()
                #Check is set of characters in word is in set of the input
                if set(word).issubset(characters) and len(word) > 2:
                    three_letter_starts.add(word[:3])
                    if len(word) > 3:
                        four_letter_starts.add(word[:4])
                    word_set.add(word)

    word_length_to_score = {3: 100, 4: 400, 5:800, 6:1400, 7: 1800, 8: 2200, 9:2600, 10:3000}


    the_words = set()
    for i in range(board_height):
        for j in range(board_width):
            visited = set()
            the_words.union(find_words(board, i, j, "", the_words, visited, word_set), the_words)

    final_dictionary = {}
    for the_word in the_words:
        if len(the_word) not in final_dictionary:
            final_dictionary[len(the_word)] = [the_word]
        else:
            final_dictionary[len(the_word)].append(the_word)

    score_window = Tk()
    score_window.geometry("1000x1000+10+20")
    label_lis = []
    total_score = 0
    number_of_words_count = 0
    for i in range(11, 2, -1):
        if i in final_dictionary:
            for item in final_dictionary[i]:
                l = Label(score_window, text = str(item) + "      " + str(word_length_to_score[i]))
                label_lis.append(l)
                print(item, word_length_to_score[i])
                total_score += word_length_to_score[i]
                number_of_words_count += 1
    print(total_score)
    score.config(text="Total Score: " + str(total_score))
    number_of_words.config(text="Number of Words: " + str(number_of_words_count))
    for i in range(len(label_lis)):
        label_lis[i].grid(row = int(i%20), column = int(i/20), sticky = W, pady = 2)

    score_window.mainloop()






def select_map():
    option = var.get()
    if option == 1:
        frame1.place(relx = .27, rely = .25)
        frame2.pack_forget()
        frame3.pack_forget()
        frame4.pack_forget()
    if option == 2:
        frame2.place(relx = .27, rely = .25)
        frame1.pack_forget()
        frame3.pack_forget()
        frame4.pack_forget()
    if option == 3:
        frame3.place(relx = .27, rely = .25)
        frame1.pack_forget()
        frame2.pack_forget()
        frame4.pack_forget()
    if option == 4:
        frame4.place(relx = .27, rely = .25)
        frame1.pack_forget()
        frame2.pack_forget()
        frame3.pack_forget()


window = Tk()

window.title("Word Hunt")
window.geometry("1000x1000+10+20")


def validate(P, integer, max, map):
    if len(P) == 0:
        return True
    elif len(P) == 1 and P.isalpha():
        if int(integer) + 1 < int(max):
            if int(map) == 1:
                entry1_lis[int(integer) + 1].focus()
            if int(map) == 2:
                entry2_lis[int(integer) + 1].focus()
            if int(map) == 3:
                entry3_lis[int(integer) + 1].focus()
            if int(map) == 4:
                entry4_lis[int(integer) + 1].focus()
        return True
    else:
        return False

vcmd = (window.register(validate))


frame1 = Frame(window, bg="black",width=400,height=400)
entry1_lis = []#.1, .36666, .6333333, .9
coordinates_list1 = [.1, .3666666, .633333, .9]
for i in range(4):
    for j in range(4):
        entry1 = tk.Entry(frame1, justify="center", validate="key", validatecommand=(vcmd, '%P', 4*i + j, 16, 1))
        entry1.place(width=40, height=40, relx = coordinates_list1[j], rely = coordinates_list1[i])#.1, .3, .5, .7, .9
        entry1_lis.append(entry1)



map2_blocks = [(1, 1), (5, 5), (1, 9), (9, 1), (9, 9)]
frame2 = Frame(window, bg="black",width=400,height=400)
entry2_lis = []
count = 0
for i in range(1, 11, 2):
    for j in range(1, 11, 2):
        if (i, j) in map2_blocks:
            blegh = 1
        else:
            entry2 = tk.Entry(frame2, justify="center", validate="key", validatecommand=(vcmd, '%P', count, 20, 2))
            entry2.place(width=30, height=30, relx = float(j/10), rely = float(i/10))#.1, .3, .5, .7, .9
            entry2_lis.append(entry2)
            count+=1


map3_blocks = [(1, 5), (5, 1), (5, 9), (9, 5)]
frame3 = Frame(window, bg="black",width=400,height=400)
entry3_lis = []
count = 0
for i in range(1, 11, 2):
    for j in range(1, 11, 2):
        if (i, j) in map3_blocks:
            blegh = 1
        else:
            entry3 = tk.Entry(frame3, justify="center", validate="key", validatecommand=(vcmd, '%P', count, 21, 3))
            entry3.place(width=30, height=30, relx = float(j/10), rely = float(i/10))#.1, .3, .5, .7, .9
            entry3_lis.append(entry3)
            count += 1

frame4 = Frame(window, bg="black",width=400,height=400)
entry4_lis = []
count = 0
for i in range(1, 11, 2):
    for j in range(1, 11, 2):
        entry4 = tk.Entry(frame4, justify="center", validate="key", validatecommand=(vcmd, '%P', count, 25, 4))
        entry4.place(width=30, height=30, relx = float(j/10), rely = float(i/10))#.1, .3, .5, .7, .9
        entry4_lis.append(entry4)
        count += 1





score = tk.Label(window, text = 'Score:')
score.place(relx = .5, rely = .1, anchor = "center")

number_of_words = tk.Label(window, text = 'Number of Words:')
number_of_words.place(relx = .5, rely = .2, anchor = "center")

enter = Button(window, text = "Enter", command=get_board)
enter.place(relx = .5, rely = .8)

exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.place(relx = .55, rely = .8)


var = IntVar()
map1 = Radiobutton(window, text = "Map 1", variable=var, value=1, command=select_map)
map1.place(relx = .8, rely = .3)

map2 = Radiobutton(window, text = "Map 2",variable=var, value=2, command=select_map)
map2.place(relx = .8, rely = .35)

map3 = Radiobutton(window, text = "Map 3",variable=var, value=3, command=select_map)
map3.place(relx = .8, rely = .4)

map4 = Radiobutton(window, text = "Map 4",variable=var, value=4, command=select_map)
map4.place(relx = .8, rely = .45)

map1.select()

window.mainloop()





'''
Map 1:
a r e s
f h t e
o p z w
y u r s
# #GWW#AHUIDLS#POKEKOL#FLL#
Map 2:
# a l k #
g h s e f
w u # k l
w i p o l
# d o l #

# UI#QWIWRCE#UOP#OHPEOPI#NL
Map 3:
u i # o p
l w u h i
# r o p #
q c p e n
w e # o l

Map 4:

i w p o l
e r k a e
f o w q w
e v l e r
q b n a s
'''
