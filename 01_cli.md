# 1. git 사용법



## 1.1 CLI 

> 커맨드 라인 인터페이스

- `mkdir`[폴더명] : make directory, 폴더 생성 
- `li` 현재위치 폴더 내부의 파일 & 폴더를 나열 > 기본위치 : home directory : `~`
- `pwd` 현재 폴더 경로 출력 
- `cd`: change directory 
- 상대경로  `..` 상위 폴더이동
- `--` : 옵션 부여 예. `--global`전역설정



## 1.2 git으로 폴더 관리

폴더단위로 관리한다. 현재 폴더 상태를 사진찍는다

버전관리 = 어떤 파일 상태를 찍을 지 지정: 

1) **add**; 사진대(staging area)에 사진(file-버전관리 대상)을 올려놓는다.

$ git add[파일명] 

2) **commit** : 사진을 찍는다.(저장관리를 한다.) 기본적으로 깃헙 가입 이메일 

$ git commit 이전에 global user.name, email 입력

$ git commit -m "first commit"

3) 버전 목록 보기 

$ git log : 찍었던 사진, 목록, 어떤 메세지인지 확인 가능 



버전을 통해 관리 후 ,  git hub에 저장한다.

`$ git  init `폴더 안에 git으로 관리를 시작 할 때 .git파일을 만든다. 

git이 프로젝트 파일 상태를 계속 주시할 수 있다. 

`$ ls -a` : 숨김파일까지 모두 보기 **`.`으로 시작하는 모든 파일, 폴더는 숨길으로 보인다 **

`$ git status` : git의  상태 확인 

`$ touch`[파일명] : 파일 생성 명령

`$ rm`[파일명] : 파일 삭제 

