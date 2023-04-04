import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import json


def get_data(url):
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    # r=requests.get(url=url,headers=headers)

    # with open("парсинг5 #/index1.html","w",encoding="utf-8") as file:
    #     file.write(r.text)

     #get hotels urls
    r= requests.get("https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most", headers=headers)
    soup=BeautifulSoup(r.text,"lxml")

    hotel_cards=soup.find_all("div",class_="hotel_card_dv")
    # hotel_cards=hotel_cards.find("div",class_="hotel_info_dv")
    # hotel_card=hotel_cards.find("div",class_="hotel_head_dv")


    for hotel_url in hotel_cards:
        hotel_ur=hotel_url.find("div",class_="hotel_info_dv").find("div",class_="hotel_head_dv").find("a").get("href")
        rep="www.rsrv.me"
        if rep in hotel_ur:
            hotel_ur=hotel_ur.replace(rep,"tury.ru")
            print(hotel_ur)
            

# def get_data_selenium(url):
#     option=webdriver.ChromeOptions()
#     option.set_("general.useragent.override", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")

#     try:
#         driver=webdriver.ChromeOptions()
#         executable_path="C:\Users\Asus\Desktop\парсинги\парсинг5 #\chromedriver.exe"
#         option=option
#     except Exception as  ex:
#         print(ex)

#     finally:
#         driver.close()
#         driver.quit()

# with open("парсинг5 #6/all_cateegories_dict.json","w",encoding="utf-8") as file:
#     json.dump(hotel_ur,file,indent=4,ensure_ascii=False)

def main():
    get_data("https://tury.ru/hotel/most_luxe.php")

if __name__=="__main__":
    main()
