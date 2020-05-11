import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            #attributes
            title="**Please drink water now!",
            message="Its time to drink water again. its been an hour you didnot drink water",
            #app_icon="",
            timeout=12
            )
        time.sleep(60*60)    