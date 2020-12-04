import requests
# import unicodecsv as csv
import csv
from bs4 import BeautifulSoup


def check_data(field):
    if field == None:
        return True
    else:
        return False
        

f = csv.writer(open('alnd_2310.csv', 'w', encoding='utf-8'))
f.writerow(['date', 'image', 'đường trước nhà', 'số tầng', 'số phòng ngủ', 'chỗ để xe', 'diện tích', 'kích thước','hướng nhà', 'giá', 'địa chỉ', 'quận', 'huyện'])
pages = []

for i in range(2, 165): #164
    url = 'https://alonhadat.com.vn/nha-dat/can-ban/can-ho-chung-cu/1/ha-noi/trang--' + str(i) + '.html'
    #https://alonhadat.com.vn/nha-dat/can-ban/can-ho-chung-cu/1/ha-noi/trang--2.html
    pages.append(url)


for item in pages:
    page = requests.get(item)
    # soup = BeautifulSoup(page.text, 'html.parser')
    # soup = BeautifulSoup(page.content, 'html.parser')
    soup = BeautifulSoup(page.content, 'html5lib')

    # last_links = soup.find(class_='AlphaNav')
    # last_links = soup.find(class_='page')
    # last_links.decompose()

    house_list = soup.find_all(class_='content-item')

    for house in house_list:
        date = house.find(class_='ct_date')
        if check_data(date) == True:
            # date = 'NULL'
            continue
        else:
            date = date.contents[0]

        image = house.find(class_='thumbnail').find("img")['src'] #ảnh

        text = house.find(class_='text')


        house_road_width = text.find(class_='road-width') #đường trước nhà, đơn vị m
        if check_data(house_road_width) == True:
            duong_truoc_nha = 'NULL'
        else:
            duong_truoc_nha = house_road_width.contents[0]
            if duong_truoc_nha.find(",") != -1:
                duong_truoc_nha = duong_truoc_nha.replace(",", ".")
            duong_truoc_nha = float(duong_truoc_nha.split("m")[0])


        house_floors = text.find(class_='floors') #số tầng
        if check_data(house_floors) == True :
            so_tang = 'NULL'
        else:
            so_tang = house_floors.contents[0]
            so_tang = int(so_tang.split(" ")[0])


        house_bedroom = text.find(class_='bedroom')
        if check_data(house_bedroom) == True :
            so_phong_ngu = 'NULL'
        else:
            so_phong_ngu = house_bedroom.contents[0]
            so_phong_ngu = int(so_phong_ngu.split(" ")[0])

        house_parking = text.find(class_='parking') #chỗ để xe: có = 1
        if check_data(house_parking) == True :
            cho_de_xe = 'NULL'
        else:
            # cho_de_xe = house_parking.contents[0]
            cho_de_xe = 1

        house_dientich = text.find(class_='ct_dt') #diện tích, đơn vị mét vuông
        if check_data(house_dientich) == True :
            dien_tich = 'NULL'
        else:
            dien_tich = house_dientich.contents[1]
            if dien_tich.find(".") != -1:
                dien_tich = dien_tich.replace(".", "")
            dien_tich = int(dien_tich.strip().split(" ")[0])


        house_kichthuoc = text.find(class_='ct_kt') #kích thước dài*rộng
        if check_data(house_kichthuoc) == True :
            kich_thuoc = 'NULL'
        else:
            kich_thuoc = house_kichthuoc.contents[1]



        house_direct = text.find(class_='ct_direct')
        if check_data(house_direct) == True :
            huong_nha = 'NULL'
        else:
            huong_nha = house_direct.contents[1]


        house_price = text.find(class_='ct_price') #giá nhà, đơn vị triệu VND
        if check_data(house_price) == True :
            gia = 'NULL'
        else:
            gia = house_price.contents[1].strip()
            if gia.find(",") != -1:
                gia = gia.replace(",",".")
            if gia.find("triệu / m") != -1:
                gia = float(gia.split(" ")[0])*dien_tich
            elif gia.find("tỷ") != -1:
                gia = gia.split(' ')[0]
                gia = float(gia.replace(",","."))*1000
            elif gia.find("Thỏa thuận") != -1:
                gia = "NULL"
            else:
                gia = float(gia.split(" ")[0])
                

        house_diachi = text.find(class_='ct_dis')
        if check_data(house_diachi) == True :
            dia_chi = 'NULL'
        else:
            district = house_diachi.find_all('a')
            dia_chi = ""
            for element in district:
                dia_chi += element.contents[0] + ", "
            dia_chi += "Hà Nội"

            quan = ""
            phuong = ""
            if len(district) == 2:
                phuong = district[0].contents[0]
                quan = district[1].contents[0]
            elif len(district) == 3:
                phuong = district[1].contents[0]
                quan = district[2].contents[0]

            # dia_chi =  house_diachi.contents[0].contents[0] + house_diachi.contents[1] + house_diachi.contents[2].contents[0] + house_diachi.contents[3] + house_diachi.contents[4].contents[0]

        f.writerow([date, image, duong_truoc_nha, so_tang, so_phong_ngu, cho_de_xe, dien_tich, kich_thuoc, huong_nha,gia, dia_chi, quan, phuong])
        # f.writerow(['date', 'image', 'đường trước nhà', 'số tầng', 'số phòng ngủ', 'chỗ để xe', 'diện tích', 'kích thước','hướng nhà', 'giá', 'địa chỉ'])
# f.close()
# print("DONE!!!")