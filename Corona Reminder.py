from plyer import notification

import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,    # HERE WE SHOULD PASTE THE PATH OF ICON IN .ico form
        timeout = 3
    )

def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        #notifyMe("Pranshu", "Lets stop the spread of this virus together")
        myHTMLdata = getData('https://www.mohfw.gov.in/')


        soup = BeautifulSoup(myHTMLdata, 'html.parser')
        #print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody').find_all('tr'):
            myDataStr += tr.get_text()

        itemList = myDataStr.split("\n")

        states = ['Chandigarh', 'Uttar Pradesh']
        for item in itemList[0:22]:
            dataList = item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid 19'
                ntext = f"{dataList[1]} Indian:{dataList[2]}\n Foreign: {dataList[3]}\n Cured: {dataList[4]}\n Deaths: {dataList[5]}"
                notifyMe(nTitle, ntext)
                time.sleep(2)

        time.sleep(3600)