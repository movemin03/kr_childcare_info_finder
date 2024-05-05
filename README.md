# 한국 어린이집 정보 검색기 (kr_childcare_info_finder.py) 👍❤️

어린이집 정보 검색기 프로그램은 선택한 지역 내 어린이집에 관한 정보를 가져올 수 있습니다. 원하는 위치를 제공하면 해당 지역에 위치한 어린이집에 대한 데이터를 가져옵니다.

## 사용법
1. 보육통합정보시스템 웹사이트 [여기](https://info.childcare.go.kr/info/oais/openapi/OpenApiInfoSl.jsp)에서 API 키를 발급받습니다.
2. `kindergarten_info_finder.py` 스크립트를 실행합니다.
3. 원하는 위치를 입력합니다.
4. 프로그램은 선택한 지역의 어린이집 정보를 가져옵니다.

## 요구사항
다음 라이브러리가 설치되어 있는지 확인하세요:
```cmd
pip install pandas, requests, xml.etree.ElementTree
```

## 참고
이 프로그램은 보육통합정보시스템에서 제공하는 데이터를 기반으로 합니다. API 키를 사용할 때 적절한 액세스 권한을 보유하고 이용약관을 준수해야 합니다.

---

# kr_childcare_info_finder (English) 👍❤️

The Kindergarten Information Finder program allows you to retrieve information about kindergartens within a selected area. By providing the desired location, the program fetches data on kindergartens located in that area.

## Usage
1. Obtain an API key from the Childcare Integrated Information System website [here](https://info.childcare.go.kr/info/oais/openapi/OpenApiInfoSl.jsp).
2. Run the `kindergarten_info_finder.py` script.
3. Input the desired location.
4. The program will fetch information about kindergartens in the selected area.

## Requirements
Ensure you have the following libraries installed:
```cmd
pip install pandas, requests, xml.etree.ElementTree
```


## Note
This program relies on the data provided by the Childcare Integrated Information System. Ensure you have proper access rights and adhere to their terms of service while using the API key.
