import time


from plyer.facades import notification
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
        title = "Please Drink Water"
        message = "Water is important. You should drink 3.7L of water everyday"
        app_icon = "C:\Users\Amit\Desktop\Python\desktop notification\icon.ico"
        timeout = 5
    )

        time.sleep(60*60)
