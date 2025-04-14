# Selenium 라이브러리와 필요한 모듈들 임포트
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# 크롬 웹드라이버 객체 생성
driver = webdriver.Chrome()

# 멜론 차트 URL 설정
URL = 'https://www.melon.com/chart/index.htm'

# 설정된 URL로 웹페이지 열기
driver.get(URL)

# 곡 정보 버튼 요소들을 가져오기 (CSS Selector 사용)
song_infos = driver.find_elements(By.CSS_SELECTOR, 'a.btn.song_info')

# 곡 정보를 저장할 리스트 초기화
song_list = []

# 상위 5개의 곡 정보를 순회하며 수집
for i in range(5):
    # 곡 정보 버튼 클릭
    song_infos[i].click()
    time.sleep(2)  # 페이지 로딩 대기

    # 곡 제목 가져오기
    title = driver.find_element(By.CSS_SELECTOR, 'div.song_name').text
    # 아티스트 이름 가져오기
    artist = driver.find_element(By.CSS_SELECTOR, 'div.artist > a > span').text
    # 발매일 가져오기
    meta_data = driver.find_elements(By.CSS_SELECTOR, 'div.meta dd')
    # 발매일 가져오기
    publish_date = driver.find_element(By.CSS_SELECTOR, 'dl.list > dd:nth-of-type(2)').text
    # 좋아요 수 가져오기 (쉼표 제거)
    like_count = driver.find_element(By.CSS_SELECTOR, 'span#d_like_count').text
    like_count = like_count.replace(',', '')
    # 수집한 정보를 리스트에 추가
    song_list.append([title, artist, publish_date, like_count])
    # 이전 페이지로 돌아가기
    driver.back()

# CSV 파일 저장 경로 설정
local_file_path = '/home/ubuntu/damf2/data/melon/'

# 수집한 데이터를 CSV 파일로 저장하는 함수 정의
def save_to_csv(song_list):
    with open(f'{local_file_path}melon.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(song_list)

# 수집한 데이터를 CSV 파일로 저장
save_to_csv(song_list)