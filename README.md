# Selenium_image_crawling
### Selenium으로 구글 이미지 크롤링
코드 진행
> 1. 이미지 검색창에 검색어 입력
> 2. 이미지 검색결과에서 **"결과 더보기"** 까지 스크롤을 내림
> 3. **"결과 더보기"** 클릭
> 4. 스크롤을 끝까지 내려서 모든 이미지 검색결과가 노출되게 함
> 5. 이미지마다 클릭해서 **화질이 좋은 이미지**가 노출되도록 함
> 6. 이미지 다운로드

특징
* 스크롤의 높이를 측정해서 스크롤을 끝까지 내리도록 코딩
```python
  height = driver.execute_script("return document.body.scrollHeight")
```
* 이미지 검색결과에서 이미지는 구글에서 보정한 이미지라

  이미지를 한 번 클릭해서 좀 더 나은 이미지를 다운로드 받도록 코딩
```python
  driver.find_element_by_css_selector(".mye4qd").click()
```

![h](https://user-images.githubusercontent.com/72850237/120897142-ad806e00-c65f-11eb-8242-a0651d6c3c74.JPG)

![h2](https://user-images.githubusercontent.com/72850237/120897378-cc333480-c660-11eb-9210-0beeb19d29f0.JPG)
