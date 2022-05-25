import requests
from bs4 import BeautifulSoup
from email import message
import smtplib
from email.message import EmailMessage
from fileinput import filename
from datetime import datetime
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://www.daegufc.co.kr/team/staff2.php"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

file = open("daegu.txt", "w")

date = datetime.today().strftime("%Y년 %m월 %d일 \n")
print(date)
file.write(date + "\n")


team = soup.findAll("div", "staff-section")
for team in team:
    file.write(team.get_text().strip() + "\n")
    print(team.get_text().strip())

file.close()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")


message = EmailMessage()
message.set_content("대구FC 선수들을 소개합니다.")
message["Subject"] = "크롤링해서 메일보내기[정유경]"
message["From"] = "********@likelion.org"
message["To"] = "********@likelion.org"

with open("daegu.txt", "rb") as txt:
    txt_file = txt.read()

message.add_attachment(txt_file, maintype='txt',
                       subtype='txt', filename=txt.name)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("*********@likelion.org", "*********")

sendEmail("********@likelion.org")

smtp.quit()