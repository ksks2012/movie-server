# Movie-API-Server


## Member
| 이름  | github                                   |
|-------|-----------------------------------------|
|최신혁 |[shchoi94](https://github.com/shchoi94)     | 


## 사용 기술 및 tools
- Django, DRF, drf-spectacular, sqlite3
## 모델링
![image](https://user-images.githubusercontent.com/68194553/145079543-d82bbc58-683b-46e4-a89b-ebadaa771c2c.png)

## API 문서 (로컬 환경 실행 후)
- http://127.0.0.1:8000/api/schema/swagger-ui/
<details>
 <summary><b>API 리스트</b></summary>
<div markdown="1">

- **사용자 생성 : POST /users/**
- **사용자 로그인 : POST /users/login/**
- **사용자 로그아웃: POST /users/logout/**   


- **영화 리스트 조회: GET /movies/**
- **영화 디테일 조회: GET /movies/{movie_id}/**
- **영화 생성: POST /movies/**


- **영화리뷰 디테일 조회: GET /reviews/{review_id}/**
- **영화리뷰 생성: POST /reviews/**
  - 영화 평점이 업데이트 됩니다.
- **영화리뷰 삭제: DELETE /reviews/{review_id}/**
  - 영화 평점이 업데이트 됩니다.

- **영화리뷰추천 생성: POST /review_votes/**
  - 리뷰 추천수가 업데이트 됩니다.
- **영화리뷰추천 삭제: DELETE /review_votes/{review_vote_id}/**
  - 리뷰 추천수가 업데이트 됩니다.

</div>
</details>

## 설치 및 실행 방법
<details>
 <summary><b>설치 및 실행 방법 자세히 보기</b></summary>
<div markdown="1">
  
###  Local 개발 및 테스트용

1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    $ git clone https://github.com/shchoi94/movie-server.git
    $ cd movie-server
    ```

2. 가상환경 생성 및 프로젝트 실행
    ```bash
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py runserver
    ```


</div>
</details>

