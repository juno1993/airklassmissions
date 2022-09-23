# airklassmissions

##### 프로젝트 다운로드
    git clone 프로젝트명
    
##### 설치
    pip install --upgrade pip
    pip install -r djangomission/requirements.txt
    
##### 환경변수
    DJANGO_SETTINGS_MODULE=djangomission.settings

##### 마이그레이션 (윈도우)
    1. makemigrations.bat 실행
    2. migrate.bat 실행

##### 마이그레이션 (mac)
    1. makemigrations.sh 실행
    2. migrate.sh 실행

##### command 실행 (윈도우) 유저 생성
    set DJANGO_SETTINGS_MODULE=djangomission.settings
    python djangomission/manage.py create_user

##### command 실행 (mac) 유저 생성
    export DJANGO_SETTINGS_MODULE=djangomission.settings
    ./djangomission/manage.py create_user    
    
##### POSTMAN을 이용한 API 테스트
    해당 파일은 메일로 첨부
    
##### 요구사항
    ● 수강생, 강사, 강의, 질문, 답변 모델간의 관계를 구현 해야 합니다.
    ● 강의 생성 기능
        ○ 강의는 강사만 생성이 가능해야 합니다.
    ● 유저가 질문 남기는 기능
        ○ 유저는 모든 강의에 질문을 남길 수 있습니다.
        ○ 작성한 질문은 삭제할 수 있습니다.
        ○ 답변이 달린 질문은 삭제가 불가능 합니다.
    ● 강사가 질문에 답변을 남길 수 있는 기능
        ○ 강사는 자신이 생성한 모든 강의에 작성된 질문에 답변을 남길 수 있습니다.
        ○ 작성한 질문은 삭제할 수 있습니다.
    ● 강의에 작성된 질문과 답변을 확인할 수 있는 기능
        ○ 모든 사용자는 특정 강의에 작성된 질문과 답변을 확인할 수 있습니다.

#####추가된 기능
    utils package
    > custom_exception 추가
    > custom api_view 추가
    > permission 추가
    > 토큰 인증 처리
    > 조회, 생성, 상세, 삭제 api mixin 사용
    
    2. BaseCommand
    경로: commands > management > commands > create_user.py
    User를 생성하면 Master도 생성이 됩니다. (마스터 등록 api는 따로 만들어 두지 않았습니다)
    
    
    
    