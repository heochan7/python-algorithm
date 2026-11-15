import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status() # 오류 발생 시 예외 처리
    except requests.exceptions.RequestException as e:
        print(f"웹페이지 요청 실패: {e}")
        return

    # BeautifulSoup으로 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 예시: 웹페이지의 모든 타이틀(h1 태그) 출력
    titles = soup.find_all('h1')
    
    print(f"--- '{url}' 크롤링 결과 ---")
    for idx, title in enumerate(titles, 1):
        print(f"{idx}. {title.get_text(strip=True)}")

# 사용 예시
# simple_web_scraper("https://example.com")