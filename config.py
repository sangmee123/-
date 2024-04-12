import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
DB_URL = os.getenv("DB_URL")

TEMPLATE_CLOVA_OCR_INVOKE_URL = os.getenv("TEMPLATE_CLOVA_OCR_INVOKE_URL")
TEMPLATE_CLOVA_OCR_SECRET_KEY = os.getenv("TEMPLATE_CLOVA_OCR_SECRET_KEY")

NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID') 
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')  
NAVER_AUTH_ENDPOINT = "https://nid.naver.com/oauth2.0/authorize"
NAVER_REDIRECT_URI = "http://localhost:8000/naver/callback" 
NAVER_TOKEN_ENDPOINT = "https://nid.naver.com/oauth2.0/token"
NAVER_USER_INFO_ENDPOINT = "https://openapi.naver.com/v1/nid/me"

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_AUTH_ENDPOINT="https://accounts.google.com/o/oauth2/auth"
GOOGLE_REDIRECT_URI = "http://localhost:8000/google/callback" 
GOOGLE_TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
GOOGLE_USER_INFO_ENDPOINT = "https://www.googleapis.com/oauth2/v2/userinfo"

JSON_FILE_PATH = "./google-sheet-key.json"
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1A9jVQw5IdimIi_W-NKXaMiVQ3KZMSHVqZDl1x5LaWeU/edit#gid=0"
WORKSHEET_NAME = '시트1'
GOOGLE_CLOUD_API_KEY = os.getenv('GOOGLE_CLOUD_API_KEY')

OPENAPI_URL = "http://openapi.kepco.co.kr/service/dispersedGenerationService/getDispersedGerSearch"
OPENAPI_SERVICE_KEY = 'yePXmaGSUDC24GevqocamLNfFWPuhPb2cHDcGEm6YbWa7f3ykQQ4%2FvJinVsNrDGJ9vyS0popC616QiJlkOVjdA%3D%3D'