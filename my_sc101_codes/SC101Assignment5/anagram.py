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


def main():
    global dict_lst
    dict_lst = read_dictionary()
    """
    TODO:
        1. 做出使用者輸入的介面後，使用while True讓使用者重複輸入，直到輸入EXIT為止
        2. 編輯find_anagrams()，使ans_lst存著所有的答案後印出
    """
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit) ')
    while True:
        user_string = input('Find anagrams for: ').lower()
        if user_string == EXIT:
            break
        start = time.time()
        ans_lst = find_anagrams(user_string)
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


def find_anagrams(s):
    """
    :param s: 使用者輸入的字串
    :return: 1.印出Searching...
             2.印出所有符合在字典中的strings（Found: ）
             3.印出將所有符合的string組成的list
    """
    global dict_lst
    ans_lst = []
    # 用來檢查該字母有無被使用過，若無為False，有則為True
    used_ch = [False] * len(s)
    print('Searching...')
    find_anagrams_helper(s, [], dict_lst, ans_lst, used_ch)
    return ans_lst


def find_anagrams_helper(s, current_lst, lst, ans_lst, used_ch):
    """
    :s: 使用者輸入的字串
    :current_lst: 在遍歷整個字串時，用來接住每一個字母的list
    :lst: 存放所有字典詞彙的list
    :ans_lst: 裝著所有最後呈現的答案的list
    :used_ch: a boolean list，用來對照current_lst，若current_lst的相同index有相同的字母，代表要把其boolean值改為True.
    TODO:
    Loop使用者輸入的字串
    每個字母依序丟進字典裡面
    如果有一樣的字母，將current_lst新增該字母
    base case:如果lst長度剛好跟原本的字串一樣長->代表找到答案->印出
    """
    if len(current_lst) == len(s):
        check_words = ''
        for character in current_lst:
            check_words = check_words + character
        if check_words in lst and check_words not in ans_lst:
            ans_words = check_words
            print('Found: ', ans_words)
            print('Searching...')
            ans_lst.append(ans_words)
    else:
        for i in range(len(s)):
            if not used_ch[i]:
                # choose
                # 使用過，則改為True
                used_ch[i] = True
                current_lst.append(s[i])
                # explore
                # 用has_prefix()先做檢查，若為True則進入recursive
                if has_prefix(''.join(current_lst)):
                    find_anagrams_helper(s, current_lst, lst, ans_lst, used_ch)
                # un-choose
                # 還原步驟，將該字母的使用狀態改為尚未使用（False）
                used_ch[i] = False
                current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: 從current_lst中組成的字串，可能為多種排列組合
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
