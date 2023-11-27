"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        total_male = 0
        total_female = 0
        target = ''
        tags = soup.find_all('table', {'class': 't-stripe'})
        for tag in tags:
            target = tag.text.split()
        for i in range(len(target)):
            # 找出list中的規律後，可得之在1～200之間，後面兩格必定是male的人口，後面四格必定是female的人口
            if target[i].isdigit() and 1 <= int(target[i]) <= 200:
                # 在做數字計算前，需要先把逗號去掉，且逗號左邊要*1000
                male_lst = target[i + 2].split(',')
                total_male += int(male_lst[0])*1000 + int(male_lst[1])
                female_lst = target[i + 4].split(',')
                total_female += int(female_lst[0])*1000 + int(female_lst[1])
        print('Male Number: ', total_male)
        print('Female Number: ', total_female)


if __name__ == '__main__':
    main()
