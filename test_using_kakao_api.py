# kakao_local_sample.py
import requests
import os
from dotenv import load_dotenv

# .env 파일에서 KAKAO_API_KEY 로드
load_dotenv()
KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")

headers = {
    "Authorization": f"KakaoAK {KAKAO_API_KEY}"
}

def search_place_by_keyword(keyword, x=None, y=None, radius=None):
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    params = {
        "query": keyword
    }
    if x and y:
        params["x"] = x
        params["y"] = y
    if radius:
        params["radius"] = radius

    response = requests.get(url, headers=headers, params=params)
    result = response.json()
    return result

places = search_place_by_keyword("용인 기흥구 반려견 동반 카페")

for place in places['documents']:
    print(place['place_name'], "-", place['address_name'])
