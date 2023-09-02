import xml.etree.ElementTree as ET
import pandas as pd
import requests
import os
from datetime import datetime

print ("엑셀 파일을 저장할 경로를 지정합니다")
file_path = os.path.join(os.path.expanduser('~'), 'Desktop')
file_path = file_path + "\\어린이집_정보조회_결과"

#시군구 데이터로드
sido_name = {
    "서울": "11",
    "부산": "26",
    "대구": "27",
    "인천": "28",
    "광주": "29",
    "대전": "30",
    "울산": '31',
    '세종': '29',
    '경기': '41',
    '강원': '42',
    '충청북도': '43',
    '충청남도': '44',
    '전라북도': '45',
    '전라남도': '46',
    '경상북도': '47',
    '경상남도': '48',
    '제주': '50'
}
print("목록: 서울, 부산, 대구, 인천, 광주, 대전, 울산, 세종, 경기, 강원, 충청북도, 충청남도, 전라북도, 전라남도, 경상북도, 경상남도, 제주")
sido_input = input("시도명을 입력하세요:")
if sido_input in sido_name:
    sido_code = (sido_name[sido_input])
    print("입력된 값의 시도 코드 앞 2자리: " + sido_code)
else:
    print(f"{sido_input}에 해당하는 시도 코드를 찾지 못했습니다.")

try:
    code_df = pd.read_excel('시군코드모음.xlsx', dtype=str)
    filtered_df = code_df[code_df['시군구코드'].str[:2] == str(sido_code)]
    print(filtered_df)
    arcode_list = filtered_df['시군구코드'].tolist()
except:
    print("시군구코드 검색을 위한 파일이 없거나 찾지 못했습니다, 시군구코드를 수동으로 입력해주십시오")
    arcode_list = [x for x in input('\n검색할 코드를 입력해주세요. 띄어쓰기로 구분합니다\n').split()]

# 필요한 정보 추출하여 데이터프레임 생성하기 위한 리스트 준비
data = []
error = []

def search():
    api_key = "api_key_info" #api key는 별도로 넣어주세요
    if api_key == "api_key_info":
        print("api key는 보육통합정보시스템 어린이집정보조회 사이트에서 별도로 받아서 넣어주십시오")
    url = "http://api.childcare.go.kr/mediate/rest/cpmsapi021/cpmsapi021/request?key=" + api_key +"&arcode=" + arcode

    # 웹 요청하여 XML 데이터 받아오기
    try:
        response = requests.get(url)
        root = ET.fromstring(response.content)
        for item in root.findall('.//item'):
            stcode = item.find('stcode').text if item.find('stcode') is not None else ''
            crname = item.find('crname').text if item.find('crname') is not None else ''
            crtelno = item.find('crtelno').text if item.find('crtelno') is not None else ''
            crfaxno = item.find('crfaxno').text if item.find('crfaxno') is not None else ''
            craddr = item.find('craddr').text if item.find('craddr') is not None else ''
            crhome = item.find('crhome').text if item.find('crhome') is not None else ''
            crcapat = int(item.find("crcapat").text) if (item.findall("crcapat") and len(item.findall("crcapat")) > 0 and
                                                     isinstance(item.findall("crcapat")[0].text, str)) else 0
            data.append({'어린이집코드': stcode, '어린이집명': crname, '전화번호': crtelno,'팩스번호': crfaxno, '주소': craddr, '홈페이지주소': crhome,'인원수': crcapat})
    except:
        print("지역코드 " + arcode +"에 해당하는 데이터가 없습니다. 지역코드가 잘못되었거나 데이터가 서버에 수집되지 않았습니다")
        error.append(arcode)

print("\n검색중입니다. 잠시만 기다려주세요")
for i in arcode_list:
    arcode = i
    search()

# 결과 폴더가 없으면 생성
if not os.path.exists(file_path):
    os.makedirs(file_path)

# 데이터프레임 생성 및 엑셀 파일로 저장
df_childcare_info = pd.DataFrame(data)
date = datetime.now().strftime("%Y%m%d_%H%M%S")

output = file_path + "\\" + date + "_어린이집 정보조회결과_" + sido_input + ".xlsx"
print(output)
df_childcare_info.to_excel(output, index=False)

print("파일이 저장되었습니다")
print("빈 값인 경우. 시도코드가 잘못되었거나 검색결과가 없습니다")
if len(error) > 0:
    print("오류가 발생한 지역코드는 다음과 같습니다:" + str(error))
    with open(file_path + "\\오류항목_" + date + ".txt", "w") as file:
        for item in error:
            file.write("오류가 발생한 지역코드는 다음과 같습니다:" + str(error))
else:
    print("발생된 오류가 없습니다")
a = input()
