'''
Programmer: Buse Batmaz
CIS 403 - Webscraper Project
Date: 7/20/20
This program takes the stock price of Netflix and depending on the price, it will send you an email.
'''

#Importing all necessary modules
import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime
import time

URL = "https://finance.yahoo.com/quote/NFLX?p=NFLX"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

#This function collects the text and date from the URL
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('data-reactid' == '49').get_text()
    price = soup.find("data-reactid" == "50").get_text()
    converted_price = price[511:517]
    #Determines the current time and date
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M")
    #print(converted_price)
    #print("\n" + price)

    #These two while loops check the price and send an email, if necessary.
    while converted_price != '500':
        if converted_price > '500':
            print("Date/Time: " + dt_string)
            print("The current price is $" + converted_price)
            send_mail()
            time.sleep(60)
            continue
        else:
            print("Whoops, the current stock price is below $500. We'll send you an email when it goes above $500.")
            break

#This function sets up the email to send
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',  587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('busebtmz@gmail.com', 'tikgwlyvufydgcyd')

    subject = "Stock Price Increased"
    body = "Check the stock price of Netflix on https://finance.yahoo.com/quote/NFLX?p=NFLX"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'busebtmz@gmail.com',
        'busebtmz@gmail.com',
        msg
    )
    print("\nEMAIL HAS BEEN SENT!\n")

    server.quit()

check_price()
