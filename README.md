# q-net-
# 프로젝트 내용
q-net 정기기사시험 원하는 지역을 자동화 신청해줍니다. 
신청 마감된 지역을 모니터링 하며, 자리가 생기면 자동으로 신청해주는 프로그램입니다. 

아직 제작중에 있습니다!

# 사용법

### 1. q-net 아이디 비번 설정
```
input_data('//input[@id="mem_id"]', '여기에 : q-net아이디를 입력하세요!!', 0.3)
input_data('//input[@id="mem_pswd"]', '여기에 : q-net 비밀번호를 입력하세요!!', 0.3)
```

Test_Application_Automation_Program.py 파일에 q-net 아이디와 비밀번호를 입력해주세요

아래는 예시입니다. 참고하세요!.
```
input_data('//input[@id="mem_id"]', 'Your_ID', 0.3)
input_data('//input[@id="mem_pswd"]', 'Your_password', 0.3)
```

그리고 실행하면 정상적으로 실행됩니다. 

```
python3 Test_Application_Automation_Program.py 
```

### 2. chormedriver:  자신의 크롬에 맞게 설치해주어야합니다. 
https://chromedriver.chromium.org/downloads
사이트에 들어가 본인의 크롬버전과 같은 드라이버를 설칭하세요.

다운 받은 cromedriver는 기존의 cromedriver와 바꿔주면 됩니다!



