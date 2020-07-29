import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Stone-200-Portable-Bluetooth-Speakers/dp/B01JIP44OU/ref=sr_1_6?dchild=1&keywords=boat+bluetooth+speaker&qid=1595853866&sr=8-6'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()[2:7]
    price = price.replace(',', '')    # replace the, with '' in price section

    converted_price = float(price)
    print(converted_price)
    print(title.strip())

    if(converted_price < 1000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # set ur default gmail id which is used to send mails
    server.login('newmahajan123@gmail.com', '12345new')

    subject = 'hey, price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Stone-200-Portable-Bluetooth-Speakers/dp/B01JIP44OU/ref=sr_1_6?dchild=1&keywords=boat+bluetooth+speaker&qid=1595853866&sr=8-6'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'newmahajan123@gmail.com',
        'nikhilmahajan918@gmail.com',
        msg
    )
    print('Hey, email has been sent!')

    server.quit()


while(True):
    check_price()
    time.sleep(86400)  # 1day=86400sec
