from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
import requests
import xmltodict
import json

app = FastAPI()
ROUTER = APIRouter()
origins = [
    # "http://localhost:8080",
    # "http://localhost:8081",
    # "http://localhost:3000",
    # "http://localhost:5050",
    # "http://localhost",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

END_POINT = 'http://openapi.kepco.co.kr/service/dispersedGenerationService/getDispersedGerSearch'
ENCODING = "QFe9f5oRsATvM5PcpU4oZB4z%2FY8zR%2F5UJnYnkdPHK8vs10UuV0zUzSV%2BGTw0SJSMgUFDM1Q4WrDoqEl1QR5PmA%3D%3D"
DECODING = "QFe9f5oRsATvM5PcpU4oZB4z/Y8zR/5UJnYnkdPHK8vs10UuV0zUzSV+GTw0SJSMgUFDM1Q4WrDoqEl1QR5PmA=="


@ROUTER.get('/')
def test(
    addrDo: str = None,
    addrSi: str = None,
    addrGu: str = None,
    addrLidong: str = None,
    AddrLi: str = None,
    addrJibun: str = None,
    substCd: str = None,
    ):

    Doname = {
        '인천시': '인천광역시',
        '경기': '경기도',
        '전남': '전라남도',
        '부산': '부산광역시',
        '서울시': '서울특별시',
        '대구시': '대구특별시',
        '광주시': '광주광역시',
        '울산시': '울산광역시',
        '세종시': '세종특별자치시',
        '강원도': '강원특별자치도',
        '전북': '전북특별자치도',
        '제주도': '제주특별자치도',
        '경북': '경상북도',
        '경남': '경상남도',
        '충북': '충청북도',
        '충남': '충청남도'
    }

    data = {
        'serviceKey': DECODING,
        'pageNo': '1',
        'numOfRows': '10',
    }
    if addrDo:
        if addrDo in list(Doname.keys()):
            data['addrDo'] = Doname[addrDo]
        else:
            data['addrDo'] = addrDo
    if addrSi:
        data['addrSi'] = addrSi
    if addrGu:
        data['addrGu'] = addrGu
    if addrLidong:
        data['addrLidong'] = addrLidong
    if AddrLi:
        data['AddrLi'] = AddrLi
    if addrJibun:
        data['addrJibun'] = addrJibun
    if substCd:
        data['substCd'] = substCd
    
    response = requests.get(END_POINT, params=data)
    hotspots_data = response.content
    json_data = json.dumps(xmltodict.parse(hotspots_data), indent=4, ensure_ascii=False)
    json_data = json.loads(json_data)
    print(json_data)

    data_len = int(json_data['response']['body']['totalCount'])

    if data_len == 0:
        return {'jsDlPwr': '해당사항 없음', 'vol_3': '해당사항 없음'}
    else:
        DL_data = json_data['response']['body']['items']['item'] if data_len == 1 else json_data['response']['body']['items']['item'][0]
        
        return DL_data if len(DL_data) ==1 else DL_data[0]

    
app.include_router(ROUTER)