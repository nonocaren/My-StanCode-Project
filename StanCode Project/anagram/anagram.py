"""
File: anagram.py
Name: Caren Yang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dic = []

def main():
    """
    TODO:
    """
    print(f'Welcome to StanCode "Anagram Generator" (or -1 to quit)')
    start = time.time()
    ####################
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break
        read_dictionary()
        find_anagrams(word)
        print(str(len(find_anagrams_helper(word, [], [], []))), 'anagrams', find_anagrams_helper(word, [], [], []))
    #                  #
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            vocab = line.strip()
            dic.append(vocab)



def find_anagrams(s): # look in dictionary
    """
    :param s: the word user input
    :param [] (list): an empty list to save current word
    :param [] (list): an empty list to save index
    :param [] (list): an empty list to save answer
    """
    print(len(find_anagrams_helper(s, [], [], [])))


def lst_to_string(lst):
    empty = ''
    for ch in lst:
        empty += ch
    return empty


def find_anagrams_helper(word, current_lst, index_list, ans_lst):
    if len(current_lst) == len(word): # find word in dictionary (loop through the dictionary)
        a = lst_to_string(current_lst)
        for ch in dic:
            if ch == a:
                if ch not in ans_lst:
                    ans_lst.append(a)
                    print('Found: ' + a)
                    print('Searching...')
    else:  # make current_lst longer
        for i in range(len(word)):
            if i in index_list: # use index_lst to judge if the alphabet already in string
                pass
            else:
                # choose
                current_lst.append(word[i]) # an alphabet
                index_list.append(i) # int
                # explore
                find_anagrams_helper(word, current_lst, index_list, ans_lst)  # 要手動退回上一個 stack frame 的狀態 => Back Tracking
                # un-choose
                current_lst.pop()
                index_list.pop()
    return ans_lst


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for word in dic:
        if word == sub_s:
            return True
    return False


if __name__ == '__main__':
    main()
