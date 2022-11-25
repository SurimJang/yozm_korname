#TODO: check_url func - url 중복 검사 
def get_url():
"""
가상 드라이버 연결
try:
    html 객체에서 다음 버튼 찾기
    > button = response.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[4]/div/div[2]/button').text
    if 다음 버튼 존재:
        현재 url 저장
        > driver.current_url
        (또는) url page_num +1
except:
    버튼 찾기 중 에러 발생 프린트
else:
    url 리스트 반환
"""

