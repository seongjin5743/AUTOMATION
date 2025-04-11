import requests
import time
from datetime import datetime
import csv

upbit_url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"

start_time = time.time()

bit_data_list = []

res = requests.get(upbit_url)
while time.time() - start_time < 60:
    res = requests.get(upbit_url)
    data = res.json()

    bit_data = [
        data[0]['market'],
        data[0]['trade_date'],
        data[0]['trade_time'],
        data[0]['trade_price'],
    ]
    bit_data_list.append(bit_data)
    time.sleep(10)
local_file_path = "/home/ubuntu/damf2/data/bitcoin/"

now = datetime.now()
file_name = now.strftime('%H-%M-%S') + '.csv'

with open(local_file_path + file_name, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(bit_data_list)