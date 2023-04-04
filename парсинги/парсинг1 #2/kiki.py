import requests
from bs4 import BeautifulSoup
import json
import csv
from time import sleep
import random

# url="https://health-diet.ru/table_calorie/?ysclid=lft4nk54oa369958712"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}
# req=requests.get(url,headers=headers)
# src=req.text


# with open("парсинг1 #2/index.html","w",encoding="utf-8") as file:
#     file.write(src)

# with open("парсинг1 #2/index.html","r",encoding="utf-8") as file:
#     src=file.read()

# soup=BeautifulSoup(src,"lxml")

# all_cateegories_dict={}
# all_products_hrreft=soup.find_all(class_="mzr-tc-group-item-href")
# for item in all_products_hrreft:
#     item_text=item.text
#     item_hreft="https://health-diet.ru"+item.get("href")
#     all_cateegories_dict[item_text]=item_hreft

# with open("парсинг1 #2/all_cateegories_dict.json","w",encoding="utf-8") as file:
#     json.dump(all_cateegories_dict,file,indent=4,ensure_ascii=False)





with open("парсинг1 #2/all_cateegories_dict.json",encoding="utf-8") as file:
    all_categories=json.load(file)

iteration_count=int(len(all_categories)) -1
count=0
print (f"Всего итераций", {iteration_count})

for category_name,category_href in all_categories.items():

    rep=[","," ","-","'"]
    for item in rep:
        if item in category_name:
            category_name=category_name.replace(item,"_")
    req=requests.get(url=category_href,headers=headers)
    src=req.text

    with open(f"парсинг1 #2/data/{count}_{category_name}.html","w",encoding="utf-8",newline="") as file:
        file.write(src)

    with open(f"парсинг1 #2/data/{count}_{category_name}.html","r",encoding="utf-8",newline="") as file:
        src=file.read()

    soup=BeautifulSoup(src,"lxml") 

    #проверка страницы на наличие таблицы с продуктами
    alert_block=soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue 

    #собираем заголовок таблицы
    table_heead=soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")  
    product=table_heead[0].text
    calories=table_heead[1].text
    proteins=table_heead[2].text
    fats=table_heead[3].text
    carbohydrates=table_heead[4].text
    
    with open(f"парсинг1 #2/data/{count}_{category_name}.csv","w",encoding="utf-8-sig", newline="") as file:
        writer= csv.writer(file,delimiter=";")
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    #собираем данные продуктов
    product_data=soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

    for item in product_data:
        product_tds= item.find_all("td")

        title=product_tds[0].find("a").text
        calories=product_tds[1].text
        proteins=product_tds[2].text
        fats=product_tds[3].text
        carbohydrates=product_tds[4].text
    
        with open(f"парсинг1 #2/data/{count}_{category_name}.csv","a",encoding="utf-8-sig", newline="") as file:
            writer= csv.writer(file,delimiter=";")
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )
        

    count +=1
    print(f"итерация{count}.{category_name} записан...")
    iteration_count= iteration_count -1

    if iteration_count==0:
        print("работа завершена")
        break

    print(f"осталось итераций:{iteration_count}")
    sleep(random.randrange(2,4))