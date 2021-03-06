# Troubleshooting

1. CORS 에러를 javascript나 client 쪽에서 처리할 방법은 없는 건가요?
   - 아래와 같이 에러를 해결하긴 했으나, client가 아닌 server 측에서 해결한 방법입니다.
2. HTTPS에서 HTTP 사이트로 요청을 보낼 방법이 있을까요?
   - ACM을 발급 받는 방법 외에 다른 방법이 있을까요?

AWS-EB DRF API 서버

- http://edugieungp.xvjby8f4xg.ap-northeast-2.elasticbeanstalk.com/api/v1/problems/

Github Page

- https://edugieun.github.io/edugieun-gh/algorithm

## 1. JS CORS Error

![image](https://user-images.githubusercontent.com/52814897/71397128-f6a55380-265f-11ea-8886-ca38f6d9d9f5.png)

1. API Crawling: Github api를 통해 나의 레포지토리 내부의 파일명, URL 주소 등을 가져온 후, 필요한 데이터만 추출하여 JSON 파일로 만든다.
2. DRF API: JSON 파일에 맞게 Django를 모델링 한 후, API 서버를 만든다.

![image](https://user-images.githubusercontent.com/52814897/71198893-2b1fb500-22d8-11ea-81a4-4d1b6f34daf3.png)

3. Vue - Django DB: Vue 단에서 DRF API를 axios 요청을 하여 정보를 불러와, Vue의 methods와 data를 이용하여 저장해준다.

   ```javascript
   getproblems() {
         axios.get('http://edugieungp.xvjby8f4xg.ap-northeast-2.elasticbeanstalk.com/api/v1/problems/')
   ```

   - 이 때, CORS Error가 발생하므로, Django 에서 `corsheaders` 처리로 접근을 허용해준다.
   - 아래와 같이 DRF API로부터 모든 DB의 객체를 받아와 Vue에서 표시한다. 나열된 문제를 선택하면 해당 문제의 Data 객체만 선택한다.

   ![image](https://user-images.githubusercontent.com/52814897/70956115-588d1880-20b6-11ea-851a-7d8b4e6ed5b3.png)

4. GitHub API Source Code Scraping: 3번 과정에서 DRF로 부터 가져온 정보에 `code_url`이 포함되어 있으므로, **선택된 알고리즘 문제**의 url을 이용해 Vue 내부에서 Github 사이트에 요청하여 javascript로 HTML Source Code를 가져온다.

   :exclamation: 4-1. Javascript로 호출 시, CORS Error

   - 로컬에서 순수 js파일을 이용하였을 경우는 아래와 같이 호출과 응답에 문제가 없었다.
   - <.js 단일 파일에서 실행했을 경우>
   - ![image](https://user-images.githubusercontent.com/52814897/71400705-e8a90000-266a-11ea-8d3f-c85217592360.png)
   - 하지만, 같은 코드를 Vue에서 호출하였을 경우 CORS 에러가 난다.
   - <Vue Instance methods에서 호출할 경우>
   - ![image](https://user-images.githubusercontent.com/52814897/71087906-9a19e280-21e0-11ea-822d-bd6e02b53311.png)
   - 인터넷 서칭 결과, 서로 다른 도메인의 접근을 막는 CORS 에러는 Javascript의 정책상 뚜렷한 처리 방법이 없고, Client 쪽에서는 처리 방법이 없다.
   - 따라서, Javascript를 사용하지 않는 Django서버에서 python을 이용하여 시도하였다.

   :green_heart: 4-2. Django에서 처리

   - **문제 선택**은 Vue 단에서 이루어지므로, 선택된 문제의 id 값을 Django로 다시 보낸 후, github으로 부터 HTML Source Code를 불러온다.

   - ```javascript
     # VUE의 axios 요청
     # Vue methods에서 선택된 문제 pk값을 이용해 DRF API로 데이터 요청
     # AWS EB를 통해 이미 배포한 DRF API서버의 주소이다.
     # {probnum}는 선택된 문제의 pk 값이다.
     axios.get(`http://edugieungp.xvjby8f4xg.ap-northeast-2.elasticbeanstalk.com/api/v1/problems/${probNum}`)
     ```

   - 파이썬에서는 문제없이 `req = requests.get(code_url)`와 같이 소스코드 호출이 가능하였다.

   - Parsing한 HTML Source Code를 다시 Vue로 보낸다.

     - 위의 Vue 단에서 axios 요청에 대한 응답으로 HTML Source Code를 보내주는 것이다.

   - HTML 소스 코드를 templete 에 넣어주면 아래와 같이 정상적인 코드가 나온다.

![image](https://user-images.githubusercontent.com/52814897/71195929-3d96f000-22d2-11ea-8c3d-cd4dc2b1b8dc.png)



## 2. HTTPS To HTTP Mixed Contents Error

- 위처럼 로컬에서는 선택한 문제의 source code를 띄우는 것은 성공하였다.
- 이제 배포만 하면 된다. 위에서 DRF API서버는 이미 AWS EB에 배포를 완료하였고, (AWS EB <-> 로컬 Vue서버)의 통신은 문제없이 요청을 주고 받을 수 있었다.
- 마지막으로 **Github page를 배포**하였는데, 아래와 같은 에러가 떴다.

![image](https://user-images.githubusercontent.com/52814897/71197030-13463200-22d4-11ea-9fa4-f47651eb40f4.png)

:exclamation: Mixed content에러는 아래의 그림에서 볼 수 있듯이, HTTP와 HTTPS가 서로 혼용되어 요청을 주고 받을 때 나타난다.

![image](https://user-images.githubusercontent.com/52814897/71404774-c87f3e00-2676-11ea-9a2a-c48c403a8fd4.png)

- 위의 그림에서 요청이 거부되는 단계는 **3번 단계**로, (Django DRF API 로컬 <-> Vue 로컬) 또는 (http DRF API서버 <-> Vue 로컬)에서는 문제 없이(또는 Django에서 corsheaders를 사용하여 해결한 부분) 작동한 부분이다.

:warning: **찾아본 해결 방법**

- HTTPS -> HTTP의 요청으로 생긴 문제이므로, HTTP인 AWS-EB DRF API 서버를 HTTPS로 만들거나, 추가해주면 된다.
- 이를 위해선, `ACM` 인증서를 만들어주면 되는데,
  - 문제는 개인 소유의 `Domain` 웹 사이트가 있어야 한다는 점이다.