from fastapi import FastAPI, BackgroundTasks
from starlette.middleware.sessions import SessionMiddleware
from routes import todo, auth, oauth_google, oauth_naver
from config import (
    SECRET_KEY,
    OPENAPI_URL,
    OPENAPI_SERVICE_KEY
)
from dependency import engine, Base
import requests
from urllib.parse import urlencode
import xml.etree.ElementTree as ET

from fastapi import Depends, Form, BackgroundTasks
from dependency import get_db, get_current_user
from models import TodoList
from schema import TodoIn
from sqlalchemy.orm import Session
from sqlalchemy.exc import TimeoutError

app = FastAPI()  # fastAPI 앱 생성
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)  # 세션 미들웨어 설정
app.include_router(todo.router)
app.include_router(auth.router)
app.include_router(oauth_google.router)
app.include_router(oauth_naver.router)

Base.metadata.create_all(bind=engine)  # 테이블 생성

###########################################################################################

cnt = 0 

def increase_count():
    global cnt
    cnt += 1
    print('현재 cnt:', cnt)
    
@app.post("/test")
async def backgroundTasks_test(
        background_tasks: BackgroundTasks,
    ):
    background_tasks.add_task(increase_count)
    
    return {"message": "Todo created in the background"}

# def create_todo(payload: TodoIn, db: Session):
#     try:
#         new_todo = TodoList(
#             text=payload.text, date=payload.date, done=payload.done, color=payload.color
#         )
#         db.add(new_todo)
#         db.flush()  # 세션의 변경 내용을 DB에 즉시 반영
#         db.commit()  # 변경 내용을 영구적으로 저장
#         db.refresh(new_todo)  # 데이터베이스에서 새로운 객체의 현재 상태를 다시 로드
#     except TimeoutError as e:
#         print("TimeoutError occurred:", e)
#         db.rollback() 
#     finally:
#         db.close()  # 세션 닫기

# @app.post("/test")
# async def backgroundTasks_test(
#         payload: TodoIn,
#         background_tasks: BackgroundTasks,
#         db: Session = Depends(get_db),
#     ):
#     background_tasks.add_task(create_todo, payload, db)
    
#     return {"message": "Todo created in the background"}

###########################################################################################
    
@app.get("/DL")
async def getDL(jibunAddress):
    addrSi = addrGu = addrLiDong = addrLi = None
    temp = jibunAddress.split()
    addrDo = temp[0]
    addrJibun = temp[-1]
    rest = ' '.join(temp[1:-1])
    for part in rest.split():
      last_char = part[-1]
      if last_char == '시':
          addrSi = part
      elif last_char in ['구', '군']:
          addrGu = part
      elif last_char in ['동', '면']:
          addrLiDong = part
      elif last_char == '리':
          addrLi = part

    print("시/도(Do):", addrDo)
    print("시(addrSi):", addrSi)
    print("구/군(addrGu):", addrGu)
    print("동/면(addrLiDong):", addrLiDong)
    print("리(addrLi):", addrLi)
    print("상세번지(addrJibun):", addrJibun)
    
    # Daum 주소 API의 시/도 표기법을 공공데이터포털 API 표기법으로 변환
    addrDo_mapping = {
        '전남': '전라남도',
        '경남': '경상남도',
        '전북특별자치도': '전북특별자치도',
        '경북': '경상북도',
        '충북': '충청북도',
        '충남': '충청남도',
        '강원특별자치도': '강원도',
        '제주특별자치도': '제주도',
        '서울': '서울특별시',
        '경기': '경기도',
        '인천':'인천광역시'
    }

    addrDo = addrDo_mapping.get(addrDo, addrDo)
    
    decoded_key = requests.utils.unquote(OPENAPI_SERVICE_KEY)
    # addrDo 시/도, addrSi 시, addrGu 구/군, addrLiDong 동/면, addrLi 리
    # substCd 변전소코드 - 구하는 법을 모르겠어서 생략
    params = {'serviceKey': decoded_key, 'pageNo': '1', 'numOfRows': '10', 'addrDo': addrDo, 'addrJibun': addrJibun}

    if addrSi is not None:
        params['addrSi'] = addrSi
    if addrGu is not None:
        params['addrGu'] = addrGu
    if addrLiDong is not None:
        params['addrLidong'] = addrLiDong
    if addrLi is not None:
        params['AddrLi'] = addrLi
        
    url_params = '&'.join([f"{key}={value}" for key, value in params.items()])
    final_url = f"{OPENAPI_URL}?{url_params}"
    print("최종 요청 URL:", final_url)
    
    # https로 하면 에러 발생
    response = requests.get(OPENAPI_URL, params=params)
    root = ET.fromstring(response.content)

    results = []
    for item in root.findall('.//item'):
        dlNm = item.find('dlNm').text
        jsDlPwr = item.find('jsDlPwr').text
        vol_3 = item.find('vol_3').text
        print(f'dlNm: {dlNm}, jsDlPwr: {jsDlPwr}, vol_3: {vol_3}')
        results.append({'dlNm': dlNm, 'jsDlPwr': jsDlPwr, 'vol_3': vol_3})
        
    return results
  
###########################################################################################

# def perform_ocr():
#     request_json = {
#         "images": [
#             {
#                 "format": "png",
#                 "name": "medium",
#                 "url": "https://storage.googleapis.com/cdn-asia/ocr/S25C-923071315520.jpg",
#             }
#         ],
#         "lang": "ko",
#         "requestId": "string",
#         "resultType": "string",
#         "timestamp": int(round(time.time() * 1000)),
#         "version": "V1",
#     }

#     payload = json.dumps(request_json).encode("UTF-8")
#     headers = {
#         "X-OCR-SECRET": TEMPLATE_CLOVA_OCR_SECRET_KEY,
#         "Content-Type": "application/json",
#     }

#     response = requests.post(
#         TEMPLATE_CLOVA_OCR_INVOKE_URL, headers=headers, data=payload
#     )
#     data_dict = json.loads(response.text)

#     return data_dict

# def process_ocr_result(data_dict):
#     results = {}
#     for field in data_dict["images"][0]["fields"]:
#         field_name = field["name"]
#         infer_text = field["inferText"]
#         if field_name == "사업장소재지" or field_name == "본점소재지":
#             infer_text = infer_text.replace("\n", "")
#         results[field_name] = infer_text
#     return results

# ocr_data = perform_ocr()
# ocr_results = process_ocr_result(ocr_data)

# # 결과 출력
# print("등록번호:", ocr_results.get('등록번호'))
# print("법인명:", ocr_results.get('법인명'))
# print("대표자:", ocr_results.get('대표자'))
# print("개업연월일:", ocr_results.get('개업연월일'))
# print("법인등록번호:", ocr_results.get('법인등록번호'))
# print("사업장소재지:", ocr_results.get('사업장소재지'))
# print("본점소재지:", ocr_results.get('본점소재지'))
