import requests
from bs4 import BeautifulSoup

lotto_url = 'https://www.dhlottery.co.kr/common.do?method=main'

res = requests.get(lotto_url)

soup = BeautifulSoup(res.text, 'html.parser')

for ball in soup.select('span.ball_645'):
    print(ball.text)