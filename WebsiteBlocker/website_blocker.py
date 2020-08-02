import time
from datetime  import datetime as dt

host_temp_path="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="27.0.0.1"
website_link=["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,6) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,12):
        print("working hours")
        with open(hosts_path, "r+") as file:
            content= file.read()
            for website in website_link:
                 if website in content:
                     pass
                 else:
                     file.write(redirect+ " " + website +"\n")
    else:
        with open(hosts_path, "r+") as file:
            content= file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_link):
                    file.write(line)
            file.truncate()
        print("Fun hours!!!")

    time.sleep(5)     