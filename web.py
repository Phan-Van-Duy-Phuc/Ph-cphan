# cac thu vien can thiet
import requests
from bs4 import BeautifulSoup
import re

# hàm để chinh sửa các URL xuat phat

def sua_url_goc(url_goc):
    if url_goc[-1] =="/":
       url_goc = url_goc[0:-1]
       return url_goc
    else:
        return url_goc

def tim_url(url, url_goc):
    url_can_tim = set()
    link = requests.get(url)
    soup = BeautifulSoup(link.text,"html.parser")
    content = soup('a', attrs={'href': True})
    for i in content:
        a_tag = i['href']
        raw = f'^{url_goc}[^?#]*$'
        raw2 = f'^/[^?#]*$'
        if re.match(raw, a_tag):
            url_can_tim.add(a_tag)
        elif re.match(raw2, a_tag):
            url_lien_quan = f'{url_goc}{a_tag}'
            url_can_tim.add(url_lien_quan)
    return url_can_tim

def tim_va_duyet_hang_cho(hang_cho, url_goc, so_luong_trang):
    history = hang_cho
    while (len(hang_cho) > 0) and (len(history) < so_luong_trang):
        url_tim_duoc = tim_url(hang_cho.pop(), url_goc)
        hang_cho = hang_cho | (url_tim_duoc - history)
        history = history | url_tim_duoc
    return history
