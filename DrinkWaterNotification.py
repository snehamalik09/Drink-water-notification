import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(title="Please Drink Water Now!!",
                        message="Health experts commonly recommend 8-ounce glasses per day, which equals about 2 liters."
                                " This is called the 8×8 rule and is very easy to remember.",
                        timeout=6,
                        app_icon=r"C:\Users\Sneha\Downloads\Glass-Water-icon.ico",
                        )

        #Notification will pop-up after each hour.
        time.sleep(60*60)

#If you want to make sure that your program will run when you are doing some another task then run the command
#"pythonw .\main.py" in the terminal



