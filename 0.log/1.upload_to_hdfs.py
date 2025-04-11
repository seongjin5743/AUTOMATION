from hdfs import InsecureClient  # HDFS 클라이언트 라이브러리 임포트
import os  # 로컬 파일 시스템과 상호작용하기 위한 os 모듈 임포트

# HDFS 클라이언트를 초기화 (HDFS 웹 인터페이스 URL과 사용자 지정)
client = InsecureClient('http://localhost:9870', user='ubuntu')

# HDFS에 업로드할 디렉토리를 생성 (주석 처리됨)
# client.makedirs('/input/logs')

# 로컬 로그 파일이 저장된 디렉토리 경로
local_file_path = '/home/ubuntu/damf2/data/logs/'

# HDFS에 업로드할 대상 디렉토리 경로
hdfs_path = '/input/logs/'

# 로컬 디렉토리 내 모든 파일 목록 가져오기
local_files = os.listdir(local_file_path)

# 로컬 디렉토리의 각 파일에 대해 반복
for local_file in local_files:
    # HDFS에 해당 파일이 존재하지 않는 경우
    if not client.content(hdfs_path + local_file, strict=False):
        # 로컬 파일을 HDFS 디렉토리로 업로드
        client.upload(hdfs_path + local_file, local_file_path + local_file)