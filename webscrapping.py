import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json
doc_detail = []
for i in range(1, 591):
    URL = "https://www.vaidam.com/doctors/india?page="+str(i)
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    doctor_div = soup.find_all('div', attrs={'class': 'col-md-8'})
    doc_detail_each = {}
    for div in doctor_div:
        doc_name = div.find_all('a')[0]["title"]
        doc_detail_each["Name"] = doc_name.split(',')[0]
        doc_detail_each["Specialisation"] = doc_name.split(',')[1]
        doc_detail_each["City"] = doc_name.split(',')[2]
        doc_hos = div.find_all('a')[1].get_text()
        if(doc_hos == ' '):
            doc_detail_each["Hospital/Clinic"] = ''
        else:
            doc_detail_each["Hospital/Clinic"] = doc_hos
        doc_exp = div.find_all(
            'span', attrs={'class': 'secondary-heading-md'})[0].get_text()
        doc_exp_arr = doc_exp.split(',')
        isint = True
        if(len(doc_exp_arr) > 1):
            try:
                int(doc_exp_arr[1][0:3])
            except ValueError:
                isint = False
            if(isint):
                doc_detail_each["Experience"] = doc_exp_arr[1][0:3]
            else:
                doc_detail_each["Experience"] = 0
        doc_high = div.find_all('span', attrs={'class': "lessDesc"})
        award_list = []
        pv = 0
        da = 0
        pb = 0
        ps = 0
        bc = 0
        for awa in doc_high:
            if(awa.get_text().find('Padma Vibhushan') != -1):
                pv = pv+1
            if(awa.get_text().find('Dhanvantari Award') != -1):
                da = da+1
            if(awa.get_text().find('Padma Bhushan') != -1):
                pb = pb+1
            if(awa.get_text().find('Padma Shri') != -1):
                ps = ps+1
            if(awa.get_text().find('Dr. B. C. Roy National Award') != -1):
                bc = bc+1
        doc_detail_each["Padma Vibhushan"] = pv
        doc_detail_each["Padma Bhushan"] = pb
        doc_detail_each["Padma Shri"] = ps
        doc_detail_each["Dhanvantari Award"] = da
        doc_detail_each["Dhanvantari Award"] = da
        doc_detail_each["Dr. B. C. Roy National Award"] = bc
        doc_detail.append(doc_detail_each)
        print(doc_detail_each)
        f = Path("data.json").open('a')
        f.write(str(doc_detail_each)+",")
        f.close()
