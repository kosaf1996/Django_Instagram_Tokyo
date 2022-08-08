# Django_Instagram

### 1. 피드 생성
- templates/instagram/main.html
- content/models.py
- content/views.py -> img 파일 저장 기능
- AJAX
- 모달
- 이미지 드래그 & 드롭
- Django_MEDIA 폴더 기능

 ### 2. 피드 목록 불러오기
- templates/instagram/main.html
- content/models.py
- content/views.py


### 3. 회원가입
- templates/user/join.html
- instagram/views.py
- user/models.py
- 패스워드 암호화

### 4. 로그인
- templates/user/login.html
- instagram/views.py
- user/models.py
- 세션과 쿠키

### 5,6,7 좋아요,댓글,북마크
- templates/instagram/main.html
- content/urls.py
- content/models.py
- content/views.py

### 8. 프로필 페이지
- templates/content/profile.html
- content/urls.py
- content/views.py

### 9. 프로필 사진 변경
- templates/content/profile.html
- user/views.py

### 10. 피드 목록 필터 조회


## 기타
### Django REST framwork
 - DRF(Django Rest Framework)란Django 안에서 RESTful API 서버를 쉽게 만들게 도와주는 라이브러리다.

### 아이콘
- 구글 머티리얼 아이콘
https://fonts.google.com/icons
```
 <link
    href="https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Two+Tone|Material+Icons+Round|Material+Icons+Sharp"
    rel="stylesheet">
```
- 아이콘을 여러개 불러올때 위의 코드처럼 여러개를 묶어 가져와야함

### Django ORM
- 객체(Object)와 관계형 데이터베이스(Relational)을 연결(Mapping)해 주는 것을 의미
- 데이터베이스의 테이블을 객체(Object)와 연결하여 테이블에 CRUD를 할 때, SQL 쿼리를 사용하지 않고도, 가능하게 하는 것
- Django ORM 에서는 auth_user 라는 user 정보 테이블이 생성된다 하지만 이 프로그램에서 커스텀 user 테이블 을 사용한다.
- user/models.py -> User 클래스
- instagram/settings.py -> USER 모델 사용을 변경하기위해 알려줘야함


### 모달 vs 팝업
- 팝업 : 새로운 브라우저창이 생성되 정보를 전달
- 모달 : 현재 브라우저의 부모 자식관계의 창을 생성
- templates/instagram/main.html

### 이미지 드래그 & 드롭
- templates/instagram/main.html
- https://kutar37.tistory.com/entry/HTML5-Javasciprt-DragDrop-%EA%B5%AC%ED%98%84-%EC%98%88%EC%A0%9C

### AJAX -> 파일업로드
- 비동기 자바스크립트와 XML -> 동적 웹 페이지를 만들어 주기위함
- content/views.py
- templates/instagram/main.html

### Django_MEDIA 폴더 기능
- 파일서버가 없을시 img, 등의 파일들을 저장할수 있는 기능
- instagram/settings.py
- instagram/urls.py
- media 디렉토리 생성

### 패스워드 암호화
- 암호화는 단방향과 양방향 암호화가 있음
- 양방향 암호화는 비밀번호를 암호화하고 다시 복호화 할 수 있는 알고리즘
- 단방향 암호화는 평문을 암호화하는 것은 가능하지만 암호화된 비밀번호를 다시 평문으로 복호화하는 것이 어려움
- user/views.py


### 세션과 쿠키
- 브라우저와 서버와 연결이된것을 세션이라고 한다.
- 서버 입장에서는 여러개 연결된 단말들의 정보를 서버 사이드에 저장하는걸 세션이라한다.
- 반대로 클라이언트에서 저장되는걸 쿠키라고 한다.
- content/views.py
- user/views.py

## 완료 PPT/ 개발자 정보

[Django_Instagram.pptx](https://github.com/kosaf1996/Django_Instagram/files/8661475/Django_Instagram.pptx)


