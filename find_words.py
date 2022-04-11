
from word_hunt import *

max_word_length = word_hunt.max_word_length
board_width = word_hunt.board_width
board_height = word_hunt.board_height
three_letter_starts = word_hunt.three_letter_starts
four_letter_starts = word_hunt.four_letter_starts


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
