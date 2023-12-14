"""
File: anagram.py
Name:
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
dict_lst = []
ans_lst = []


def main():
    global dict_lst, ans_lst
    dict_lst = read_dictionary()
    """
    此為用字串處理的方式的測試檔案
    """
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit) ')
    while True:
        ans_lst = []
        user_string = input('Find anagrams for: ').lower()
        if user_string == EXIT:
            break
        start = time.time()
        find_anagrams(user_string, len(user_string))
        print(len(ans_lst), 'anagrams:', ans_lst)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    TODO: 讀取檔案，且把每個換行字元去掉
    :return: 讀取後的字典
    """
    lst = []
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip().lower()
            lst.append(line)
    return lst


def find_anagrams(user_string, r, result=[]):
    """
    :user_string: 使用者輸入的字串
    :r: user_string的長度，進入遞迴後會縮減
    :result: list
    """
    # 使用全域變數
    global dict_lst, ans_lst
    # 每次遞迴前都先將current_str串上result裡的字母
    current_str = ''.join(result)
    # 開始遞迴前先判斷current_str是否為空，若非空則丟入has_prefix()檢查是否為True
    if len(current_str) and not has_prefix(current_str):
        return
    # 若user_string的長度已經為0，則代表已經完成一次字串的排列組合，即可檢查是否在字典裡面
    if r == 0:
        # print(''.join(result))
        if current_str in dict_lst and current_str not in ans_lst:
            ans_lst.append(current_str)
        return
    # loop整個user_string，並切成current_element以及remaining_elements，在recursive中，current_element會在result(lst)內做排列組合
    # 而剩餘的字串remaining_elements成為新的user_string，重複同樣的動作
    for i in range(len(user_string)):
        current_element = user_string[i]
        remaining_elements = user_string[:i] + user_string[i + 1:]
        find_anagrams(remaining_elements, r - 1, result + [current_element])


def has_prefix(sub_s):
    """
    :param sub_s: 從current_str中組成的字串，可能為多種排列組合
    :return: boolean值，用來判斷sub_s是否在字典裡
    """
    # 使用binary search，從字典中的左右不斷逼近
    # 將字典按字母順序排序
    global dict_lst
    # left為字典最左側的index值，right為最後一個index值
    left, right = 0, len(dict_lst) - 1
    while left <= right:
        # 從中間切分取得mid
        mid = (left + right) // 2
        word = dict_lst[mid]
        if word.startswith(sub_s):
            return True
        # 因為字典已經有被排序過，所以大於或小於的寫法是可以用的
        elif word < sub_s:
            # 若sub_s的位置在word右側，將left更新為中間值+1，繼續跑while loop
            left = mid + 1
        else:
            # 若sub_s的位置在word左側，將right更新為中間值-1，繼續跑while loop
            right = mid - 1
    return False


# def has_prefix_helper(sub_s, dict_lst):
#     for word in dict_lst:
#         if word.startswith(sub_s):
#             return True
#     return False


if __name__ == '__main__':
    main()
