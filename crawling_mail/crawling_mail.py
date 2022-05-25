from unittest import result
import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

#홈페이지 크롤링을 위한 HTML
html_file = open("kbo.html","w", encoding='utf8')
html_file.write(response.text)
html_file.close()

k = soup.findAll('td','tm')
rank = 1

kbo_rank_file = open("kbo.txt","w",encoding='utf-8')

day = datetime.today().strftime("%y년 %m월 %d일의 한국야구 팀 순위입니다.\n")
print(day)
kbo_rank_file.write(day + "\n")

for i in k:
    kbo_rank_file.write(str(rank) + "위:" + i.get_text().strip()+ "\n")
    print(rank,"위 : ",i.get_text().strip(),"\n")
    rank += 1

#이메일 전송 파트
import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("금일 한국야구 팀 순위입니다.")

message["Subject"] = "한국야구 팀 순위"
message["From"] = "######6@gmail.com"
message["To"] = "#####@######.org"

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("########@gmail.com", "#############")

with open("kbo.txt","rb") as txt:
    txt_file = txt.read()

message.add_attachment(txt_file, maintype='txt',subtype='txt',filename=txt.name)

def is_valid(addr):
    import re
    if re.match('(^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9-]+.[a-zA-Z]{2,3}$)', addr):
        print("유효한 이메일 주소입니다.")
        return True
    else:
        print("유효하지 않은 이메일 주소입니다.")
        return False

is_valid("#######@######.org")
if smtp.send_message(message)=={} :
    print("성공적으로 메일을 보냈습니다.")
smtp.quit()