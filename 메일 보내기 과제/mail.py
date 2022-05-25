import requests
import smtplib
import re
from bs4 import BeautifulSoup
from datetime import datetime
from email import message
from email.message import EmailMessage

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://www.kumoh.ac.kr/ko/sub06_01_01_01.do"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

file = open("kumoh.txt", "w", encoding='UTF-8')

date = datetime.today().strftime("%Y년 %m월 %d일 \n")
print(date)
file.write(date)

news = soup.findAll("span", "title-wrapper")

for new in news:
    result = re.sub('\s\s+', ' ', new.get_text().strip())
    file.write(result)
    file.write('\n')

file.close()




SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("메일 전송이 완료되었습니다")
    else:
        print("유효한 이메일 주소가 아닙니다.")




message = EmailMessage()
message.set_content("금오공대 공지사항")
message["Subject"] = "크롤링해서 메일보내기[김태범]"
message["From"] = "####@likelion.org"
message["To"] = "kit@likelion.org"

with open("kumoh.txt", "rb") as txt:
    txt_file = txt.read()

message.add_attachment(txt_file, maintype='txt', subtype='txt', filename=txt.name)





smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("####@likelion.org", "####")

sendEmail("kit@likelion.org")

smtp.quit()



# 구글 계정 보안 신뢰성 낮은 앱 접근 허용처리 필요