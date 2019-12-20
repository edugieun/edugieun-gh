# GitHub Page 제작

## 주제 선정 이유

- SSAFY에서 공부한 내용들을 한눈에 쉽게 볼 수 있는 페이지 제작
- Django, Vue, JS 등의 학습 내용 복습

## 결과물

- AWS 서버 주소
  - (http://edugieungp.xvjby8f4xg.ap-northeast-2.elasticbeanstalk.com/)
- Github page 주소
  - (https://edugieun.github.io/edugieun-gh/)

![image](https://user-images.githubusercontent.com/52814897/71198682-ab91e600-22d7-11ea-8f3e-35977423333d.png)
![image](https://user-images.githubusercontent.com/52814897/71198642-9026db00-22d7-11ea-866e-14f2eb859e81.png)

## 개발일지

![image](https://user-images.githubusercontent.com/52814897/71198009-38d43b00-22d6-11ea-80a7-544bd6b36e04.png)

-------

# 자기주도학습 실적


| **학습 형태**   | [x]개별 [ ] 2인 1조 [ ] 팀별 |
| --------------- | ---------------------------- |
| **구성원**      | 김기은                       |
| **일정**        | 09:00 ~ 14:00                |
| **데일리 목표** | 자기주도학습 계획 작성       |

## * 주요 내용 요약

- 19.12.09 ~ 19.12.19 기간 동안 진행한 자기주도학습 주제 선정 및 계획 작성

### 주제 선정

- Django와 Vue.js 를 바탕으로 Github page 만들기

### 세부 계획

|    Date     |                Content                 |
| :---------: | :------------------------------------: |
| 2019.12.09. |         자기주도학습 계획 작성         |
| 2019.12.10. |         Algorithm 문제 DB 제작         |
| 2019.12.11. | Django Modeling 및 DRF API Server 구축 |
| 2019.12.12. |           Vue / DRF API 접근           |
| 2019.12.13. |            AWS Server 배포             |
| 2019.12.16. |       Code Scraping 및 기능 구현       |
| 2019.12.17. |               기능 구현                |
| 2019.12.18. |               기능 구현                |
| 2019.12.19. |               Vue Design               |

- 세부 계획은 진척도에 따라 변경될 수 있음.

------

# 자기주도학습 실적


|  **학습 형태**  | [x]개별 [ ] 2인 1조 [ ] 팀별 |
| :-------------: | :--------------------------: |
|   **구성원**    |            김기은            |
|    **일정**     |        09:00 ~ 14:00         |
| **데일리 목표** |      Algorithm DB 제작       |

## * 주요 내용 요약

### 1. Github API 접근

- (https://developer.github.com/v3/)
- Github API를 이용하여 알고리즘 레포지토리 컨텐츠 확보
- Algorithm Repository Content API 요청 주소
  - https://api.github.com/repos/edugieun/Algorithm-Solving/contents

![image](https://user-images.githubusercontent.com/52814897/70925771-2906ed80-206f-11ea-816a-f973c8f1c862.png)

### 2. Parsing

- 여기저기 흩어져 있는 정보들을 python을 이용하여 JSON 파일 재구성
- 추출할 데이터
  1. 문제 번호
  2. 문제 출처
  3. 문제 유형
  4. 문제 이름
  5. 소스 코드 URL

#### 코드 구성

- `requests` 라이브러리를 이용한 정보 요청

```python
algo_URL = 'https://api.github.com/repos/edugieun/Algorithm-Solving/contents/'
...
type_list = requests.get(algo_URL, headers=params).json()
```

- 파일명에서 정보를 추출하는 함수 작성

  :exclamation: 추후에 Django를 modeling 해야하므로 Django Model의 양식에 맞춰 작성한다.

```python
def prob_info(dir_name, code_url):
		...;
    prob_obj = {}
    prob_obj['model'] = 'api.algorithm'
    prob_obj['pk'] = pk
    prob_obj['fields'] = {
        'prob_num': prob_num,
        'prob_source': prob_source,
        'prob_name': prob_name,
        'prob_diff': prob_diff,
        'prob_category': prob_category,
        'code_url': code_url
    }
```

- 객체를 `algorithms.json` 파일에 저장

```python
with open('algorithms.json', 'w', encoding='utf-8') as make_files:
    json.dump(problems, make_files, ensure_ascii=False, indent="\t")
```

![image](https://user-images.githubusercontent.com/52814897/70925824-463bbc00-206f-11ea-8cae-fddc775ccf92.png)

------

# 자기주도학습 실적


|  **학습 형태**  |     [x]개별 [ ] 2인 1조 [ ] 팀별      |
| :-------------: | :-----------------------------------: |
|   **구성원**    |                김기은                 |
|    **일정**     |             09:00 ~ 14:00             |
| **데일리 목표** | Django Modeling + DRF API Server 구축 |

## * 주요 내용 요약

### 1. Django Modeling

- Github API에서 parsing한 내용(번호, 출처, 이름, 유형, 코드 URL)에 따라 모델링을 해준다.

```python
# models.py

class Algorithm(models.Model):
    prob_num = models.IntegerField()
    prob_source = models.CharField(max_length=10)
    prob_name = models.CharField(max_length=30)
    prob_diff = models.CharField(max_length=5)
    prob_category = models.CharField(max_length=20)
    code_url = models.TextField()
    
    def __str__(self):
        return self.prob_name
```

- DB 제작 단계에서 생성한 `algorithms.json` 파일을 불러와 장고 DB에 저장한 후 확인한다.

![image](https://user-images.githubusercontent.com/52814897/70926548-abdc7800-2070-11ea-85ca-a80ad3a05b8d.png)

### 2. DRF API Server 구축

- DRF 공식 페이지 (https://www.django-rest-framework.org/)
- drf_yasg 공식 github (https://github.com/axnsan12/drf-yasg)
- `Django rest framework` 와 `drf_yasg` 를 설치한 후 기본 세팅을 진행한다.
- 공식 페이지대로 세팅을 할 경우 비로그인 시 unauth error가 발생한다. 비로그인 사용자에게도 접근 권한을 주고 싶으므로 `permission`을 `AllowAny`로 변경한다.

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
...
}
```

- view 함수를 작성한다.

```python
@api_view(['GET'])
def problem_list(request):
    problems = Algorithm.objects.all()
    serializer = AlgorithmSerializer(problems, many=True)
    return Response(serializer.data
```

- `Postman`으로 api server가 잘 작동하는지 확인한다.

![image](https://user-images.githubusercontent.com/52814897/70638331-098d5080-1c7c-11ea-8733-2bd36bfc2513.png)

![image](https://user-images.githubusercontent.com/52814897/71198893-2b1fb500-22d8-11ea-81a4-4d1b6f34daf3.png)

-------

# 자기주도학습 실적


|  **학습 형태**  | [x]개별 [ ] 2인 1조 [ ] 팀별 |
| :-------------: | :--------------------------: |
|   **구성원**    |            김기은            |
|    **일정**     |        09:00 ~ 14:00         |
| **데일리 목표** |      Vue / DRF API 접근      |

## * 주요 내용 요약

### 1. Vue 

- Vue CLI를 이용하여 Vue project를 생성한다.
- API Server로 요청을 보내기 위해 axios를 사용한다.

```javascript
import axios from 'axios'
...;
methods: {
    getproblems() {
      axios.get('http://127.0.0.1:8000/api/v1/problems/')
      .then(res => {
        this.problems = res.data
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
```

### 2. Django corsheaders

:exclamation: Django가 도메인이 다른 곳에서 API 요청을 받았을 경우, 접근을 허용하기 위해선 `corsheaders` 라이브러리가 필요하다.

![image](https://user-images.githubusercontent.com/52814897/70637641-e7470300-1c7a-11ea-8394-200be94e5379.png)

- 따로 보안이 필요하지 않은 read-only api이므로 모든 도메인에서의 접근을 허용한다.

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]
# 모든 도메인에서의 요청을 허락한다.
CORS_ORIGIN_ALLOW_ALL = True
```

![image](https://user-images.githubusercontent.com/52814897/70638203-ca5eff80-1c7b-11ea-8204-abff7ae4dca9.png)

------

# 자기주도학습 실적


|  **학습 형태**  | [x]개별 [ ] 2인 1조 [ ] 팀별 |
| :-------------: | :--------------------------: |
|   **구성원**    |            김기은            |
|    **일정**     |        09:00 ~ 14:00         |
| **데일리 목표** |       AWS Server 배포        |

## * 주요 내용 요약

### 1. settings.py 분할

- Django의 Secret_key를 숨기고, 서버에서의 Debug를 막기 위해 settings.py 를 분할 해준다.
- `local.py`는 개발단계에서 사용될 설정이고, `production.py`는 서버에서 사용될 설정파일이다. `production.py`의 `DEBUG`는 `False`로 변경해준다.

```python
# production.py
...
DEBUG = False
...
```

### 3. AWS 배포

- Django 프로젝트의 루트 디렉토리에서 `.ebxtensions` 폴더를 생성 후 `config` 파일들을 설정해준다.
- (19.12.14 기준) AWS Elastic Beanstalk에서는 `Djnago 2.1.1` 까지만 지원하므로 가상환경의 Django 버전을 낮춰줘야 한다.
- `awsebcli` 설치 후 `eb create` 명령어로 서버를 생성한다.

:exclamation: Troubleshooting

- `ERROR Your requirements.txt is invalid. Snapshot your logs for details.`
  - 원인: requirements.txt에 awsebcli가 있는 경우 발생한다.
  - 해결: awsebcli 설치 이후에 `pip freeze`는 절대 해서는 안된다. 따라서 새로운 라이브러리를 설치해야 한다면, awsebcli 이전의 가상환경을 모두 재설치해야한다.
- 서버 생성 후 도메인 주소인 `CNAME`을 `production.py` 파일의 `AALOWED_HOSTS` 변수에 할당하고 `eb deploy` 명령어로 배포한다.

```python
ALLOWED_HOSTS = ['edugieungp.xvjby8f4xg.ap-northeast-2.elasticbeanstalk.com']
```

![image](https://user-images.githubusercontent.com/52814897/70954772-e0245880-20b1-11ea-91dc-e08be9cdb522.png)

------

# 자기주도학습 실적


| **학습 형태**   | [x]개별 [ ] 2인 1조 [ ] 팀별 |
| --------------- | ---------------------------- |
| **구성원**      | 김기은                       |
| **일정**        | 09:00 ~ 14:00                |
| **데일리 목표** | Code Scraping 및 기능 구현   |

## * 주요 내용 요약

### 1. Code Scraping

- Web page에서 해당 알고리즘 문제에 대한 Source Code를 제공함에 있어, URL Link를 통해 github 사이트로 연결되는 것이 아닌, web page에서 해당 코드만 바로 보여지도록 구현하고 싶어 github page scraping을 시도하였다.

:exclamation:일반적으로 html의 element를 parsing하는 `BeautifulSoup` 를 아래와 같이 사용하여 시도하였지만, 사진처럼 indent가 제대로 적용되지 않는 모습을 보였다.

```python
req = requests.get('https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py')
raw = req.text
html_source = BeautifulSoup(raw, 'html.parser')
# codes = html_source.select('table.highlight.tab-size.js-file-line-container')
codes = codes[0]
```



![image](https://user-images.githubusercontent.com/52814897/70867037-24313380-1fb4-11ea-9c4e-14b33f57f2ef.png)

- 원인
  - BeautifulSoup를 할 경우 아래와 같이 4칸의 space가 1칸의 space로 변화되는 것을 발견하였고 code의 indent에 영향을 미쳤다.

(Chrome을 통해 확인한 원본 HTML 소스 코드)

![image](https://user-images.githubusercontent.com/52814897/70867031-0a8fec00-1fb4-11ea-8372-9db0e1091c8e.png)

(python을 이용하여 parsing한 소스 코드)

![image](https://user-images.githubusercontent.com/52814897/70867021-e92f0000-1fb3-11ea-9eae-cf100f074dbc.png)

- 해결
  - 보기 좋은 코드는 아니지만, 아래와 같이 문자열로 받은 소스코드를 인덱스로 직접 접근하여 필요한 코드 부분만 추출하였다.

```python
req = requests.get('https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py')
raw = req.text
raw = str(raw)
start = 0
end = 0
for i in range(len(raw)):
    if raw[i] == '<' and raw[i+1] == 't' and raw[i+2] == 'a' and raw[i+3] == 'b' and raw[i+4] == 'l' and raw[i+5] == 'e':
        start = i
    if raw[i] == '<' and raw[i+1] == '/' and raw[i+2] == 't' and raw[i+3] == 'a' and raw[i+4] == 'b' and raw[i+5] == 'l':
        end = i + 8
        break
table_ele = raw[start:end]
print(table_ele)
```

(python을 이용하여 parsing한 소스 코드)

![image](https://user-images.githubusercontent.com/52814897/70867054-4d51c400-1fb4-11ea-89ab-90128b794613.png)

![image](https://user-images.githubusercontent.com/52814897/70867056-55a9ff00-1fb4-11ea-93ba-b512837579d9.png)

### 2. 난이도별 표시하기

- `select` 태그와 `v-model` 로 난이도 값을 `difficulty` 변수에 넘겨준다.

```html
<select v-model="difficulty" @click="sortedProblem">
    <option value="all">All</option>
    <option value="D1">D1</option>
    <option value="D2">D2</option>
    <option value="D3">D3</option>
</select>
```

- `methods` 속성에서 전체 문제 중에 원하는 난이도의 문제를 filtering 해준다.

```javascript
methods: {
  sortedProblem: function(){
	this.sorted_problems = this.problems.filter(problem => problem.prob_diff == this.difficulty)
	}
},
```

![image](https://user-images.githubusercontent.com/52814897/70956115-588d1880-20b6-11ea-851a-7d8b4e6ed5b3.png)

------

## 자기주도학습 실적


|  **학습 형태**  | [x]개별 [ ] 2인 1조 [ ] 팀별 |
| :-------------: | :--------------------------: |
|   **구성원**    |            김기은            |
|    **일정**     |        09:00 ~ 14:00         |
| **데일리 목표** |          기능 구현           |

### * 주요 내용 요약

### 1.  Router 값 전달(1)

- 해당 문제를 클릭 했을 때, 동적 페이지처럼 소스 코드를 새로운 도메인 주소와 페이지에 보여주고자 했다.
- 새로운 페이지로 이동하는 동시에 data를 보내주기 위해 `router.push` 를 사용하였다.

❗ 아래 코드처럼 알고리즘 문제의 정보가 담긴 객체를 전달하였을 때, url 주소 변경과 함께 데이터가 잘 넘어 왔으나, 새로고침을 하면 모든 정보가 사라져 버리는 현상이 나타났다.

```javascript
onProblemSelect(problem) {
  this.$emit('problemSelect', problem)
  router.push({ name: 'detail', params: { 'problem': problem }})
}
```

------

## 자기주도학습 실적


|  **학습 형태**  | [x]개별 [ ] 2인 1조 [ ] 팀별 |
| :-------------: | :--------------------------: |
|   **구성원**    |            김기은            |
|    **일정**     |        09:00 ~ 14:00         |
| **데일리 목표** |          기능 구현           |

### * 주요 내용 요약

### 1. Router 값 전달(2)

- `router.push` 데이터 전달 시 새로고침하면 사라지는 문제를 `localStorage`를 이용하여 해결하였다.
- 이벤트가 발생한 해당 문제를 browser 상의 localStorage에 담는다.
- 동시에 router를 사용하여 새로운 페이지로 연결하며, url 주소가 문제의 id 값에 따라 변하는 동적 라우팅을 해준다.

```javascript
onProblemSelect(problem) {
      localStorage.setItem('localproblem', JSON.stringify(problem))
      router.push({ path: `/algorithm/${problem.id}`})
    }
```

- 아래와 같이 localStorage에 `localproblem`이라는 이름의 객체가 저장된 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/52814897/71056088-4b962500-219b-11ea-8eae-3bdc78c15a76.png)

- 저장된 데이터는 다른 component에서 localStorage로 접근하여 저장할 수 있다.

```javascript
data() {
    return {
        selectedProblem: JSON.parse(localStorage.getItem('localproblem'))
    }
},
```

- `selectedProblem`을 템플릿에서 호출하면 아래와 같이 localStorage에 저장된 객체의 정보를 보여주며, url 주소가 문제의 id값을 가르키게 된다.

![image](https://user-images.githubusercontent.com/52814897/71056192-ae87bc00-219b-11ea-8b9c-75188e3ab9b7.png)

### 2.  알고리즘 문제 Source Code Scraping

#### 2.1 Frontend에서 시도

- 각 문제마다 객체가 넘어오는 것을 확인하였으니, 객체의 `code_url` 로 github에 접근한 후 알고리즘 문제의 source code를 scrap 하고자 했다.
- github 사이트로 접근하기 위해서 frontend 쪽에서 `request` 또는 `XMLHttpRequest` 로 접근을 시도해 봤으나, javascript에서는 서로 다른 도메인의 접근을 차단하는  `CORS` 에러가 발생하였다.

![image](https://user-images.githubusercontent.com/52814897/71087906-9a19e280-21e0-11ea-822d-bd6e02b53311.png)

- 임시 방편으로 chrome에서 제공하는 아래의 확장 프로그램으로 에러를 피할 수 있으나, 확장 프로그램이 깔려있지 않은 곳에서는 해결이 안되기 때문에 적절하지 않다.

![image](https://user-images.githubusercontent.com/52814897/71194798-f60f6480-22cf-11ea-9d7f-76c2722e656e.png)

- 해결방안을 찾아봤지만, CORS는 client인 front 쪽에서는 해결이 쉽지 않았기에 backend 에서 처리하기로 했다.

#### 2.2 Backend에서 처리

- frontend에서 선택된 문제의 id 값을 포함한 주소의 데이터를 axios로 요청한다.

```javascript
getSource() {
        // console.log(this.selectedProblem)
        let probNum = this.selectedProblem.id
        axios.get(`http://edugieungp.xvjby8f4xg.ap-northeast-2.elasticbeanstalk.com/api/v1/problems/${probNum}`)
        .then(res => {
          this.codeHtml = res.data
        })
        .catch(err => {
          console.log(err)
        })
      }
```

- 서버에서 문제의 id 값을 가진 주소를 요청받았을 경우

```python
path('problems/<int:prob_pk>', views.get_source, name='get_source'),
```

- HTML Source로 부터 원하는 부분만 scrap하여 다시 front로 보내준다.

```python
@api_view(['GET'])
def get_source(request, prob_pk):
    problem = get_object_or_404(Algorithm, pk=prob_pk)
    code_url = problem.code_url
    req = requests.get(code_url)
    raw = req.text
    start = 0
    end = 0
    for i in range(len(raw)):
        if raw[i] == '<' and raw[i+1] == 't' and raw[i+2] == 'a' and raw[i+3] == 'b' and raw[i+4] == 'l' and raw[i+5] == 'e':
            start = i
        if raw[i] == '<' and raw[i+1] == '/' and raw[i+2] == 't' and raw[i+3] == 'a' and raw[i+4] == 'b' and raw[i+5] == 'l':
            end = i + 8
            break
    table_ele = raw[start:end]
    return Response(table_ele)
```

- Vue에서는 문자열로 받은 HTML 코드를 element 요소로 바꿔주는 `v-html` 디렉티브가 있어 편리하다.

```html
<template>
  <div v-html="codeHtml">
    {{ codeHtml }}
  </div>
</template>
```

![image](https://user-images.githubusercontent.com/52814897/71104901-ea546d00-21ff-11ea-9c11-634ca19e0d31.png)

- 코드의 가독성을 위해 github에서 적용된 css를 `public/index.html`에 추가해준다.

```html
<link crossorigin="anonymous" media="all" integrity="sha512-7mtunHqp/Bw0ND9akjJME8XCh0WPm3HAXOSeX7skL0qGAhpdfzkQvYcujYcwNPTpWKeKMFUGZGtvnEkcczFgwQ==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-9b5314213e37056ed87b0418056c4f2c.css" />
    <link crossorigin="anonymous" media="all" integrity="sha512-72YAQLJ3wNQBTmzSw8GuhpmRbpFX+Fc7CrVI80DxyM6hItKFtd8SmRqzdqhHWxcFLVI91GmT9+jBiIxzvAvbWw==" rel="stylesheet" href="https://github.githubassets.com/assets/github-858574b4b94fdd617a9aeeb43ae58986.css" />
```

![image](https://user-images.githubusercontent.com/52814897/71195929-3d96f000-22d2-11ea-8c3d-cd4dc2b1b8dc.png)

------

# 자기주도학습 실적


|  **학습 형태**  | [x]개별 [ ] 2인 1조 [ ] 팀별 |
| :-------------: | :--------------------------: |
|   **구성원**    |            김기은            |
|    **일정**     |        09:00 ~ 14:00         |
| **데일리 목표** |         Gitpage 배포         |

## * 주요 내용 요약

### 1. Vue를 github page로 배포하기

- 최종적으로 제작한 Vue 프로젝트를 github page로 사용되도록 배포해야한다.
- 먼저 루프 폴더에 `vue.config.js` 파일을 생성한 후, 리포지토리 이름을 적는다.

```python
#vue.config.js
module.exports = {
  publicPath: '/edugieun-gh/'
}
```

- 그 후 `npm run build` 명령어를 입력해주면 아래와 같은 `/dist/`폴더가 생성된다.

![image](https://user-images.githubusercontent.com/52814897/71196293-1d1b6580-22d3-11ea-8c09-420bef2377a5.png)

- dist 폴더 내부의 파일들을 복사하여 `.git ` 파일이 있는 로컬 저장소 루트 위치에 붙여넣기 한 후 `push`를 진행한다.
- 리포지토리 `settings`로 이동한 후

![image](https://user-images.githubusercontent.com/52814897/71196444-71264a00-22d3-11ea-89eb-eb269b205dc8.png)

- `GitHub Pages` 란의 `Source`를 `master branch`로 변경해준다.

![image](https://user-images.githubusercontent.com/52814897/71196499-8bf8be80-22d3-11ea-850b-47a6f1e668a2.png)

- 위의 `github.io` 주소를 클릭하면 Github Page가 배포된 것을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/52814897/71196945-dc701c00-22d3-11ea-97e7-a0cc383064b6.png)

### 2. Mixed Content Error

- 로컬에서는 잘 동작되던 것들이 안되기 시작한다.

![image](https://user-images.githubusercontent.com/52814897/71197030-13463200-22d4-11ea-9fa4-f47651eb40f4.png)

- `Mixed Content Error(혼합 콘텐츠 에러)`는 `HTTP Browser`와 `HTTPS Browser`의 서로 다른 content가 섞일 때 발생하는 에러이다.
- **Server는 HTTP 방식의 브라우저** 이고,

![image](https://user-images.githubusercontent.com/52814897/71197290-a3847700-22d4-11ea-9ed8-1da0e1d35563.png)

- **Github Page는 HTTPS 방식의 브라우저**이다.

![image](https://user-images.githubusercontent.com/52814897/71197030-13463200-22d4-11ea-9fa4-f47651eb40f4.png)

- 해결방법은 AWS에서 제공하는 ACM 인증서를 발급 받아 server에도 https 포트를 추가하는 것인데, 추후에 진행하도록 하겠다.