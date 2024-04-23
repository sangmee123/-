# 1. TodoList 프로젝트

## DB CRUD 연동

<br>

# 2. Clova OCR 프로젝트

이미지 속 텍스트를 인식하고 추출할 수 있는 기능을 제공하는 API

### 사용 기술 스택

- Naver CLOVA OCR API
- JavaScript: `Vue2`
- Python: `FastAPI`

### 데이터 출력 성공

<img src="images/데이터출력성공.png">

1. Send 버튼을 누를 시, 로딩 화면이 나타나며 해당 이미지 URL이 서버에 전송된다.
2. 서버는 Naver Clova OCR API를 호출하여 신분증 이미지의 특정 영역에서 text를 읽어온 결과를 JSON객체로 반환한다.
3. 서버에서 응답을 받으면 로딩 화면이 사라지고, 응답 받은 결과를 화면에 출력한다.

### 데이터 출력 실패(서버 Off)

<img src="images/데이터출력실패.png">

1. Send 버튼을 누를 시, 서버가 Off 돼 있어 해당 이미지 URL이 서버에 전송되지 않는다.
2. 로딩 화면이 나타나며 팝업창이 뜬다.
