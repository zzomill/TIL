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

상태가 붉은색 -> commit 할 수 있는 대상으로 바뀐다. (초록색)

2) **commit** : 사진을 찍는다.(저장관리를 한다.) 기본적으로 깃헙 가입 이메일 

$ git commit 이전에 global user.name, email 입력

반드시 무엇을 했는지 m를 남기면서 commit



되돌아가기 



$ git commit -m "first commit"

message : 무엇을 했는지 기록 

3) 버전 목록 보기 

$ git log : 찍었던 사진, 목록, 어떤 메세지인지 확인 가능 

. 

저장을 여러번 한다 : 

00 markdown  : 과거로 돌아간다. 버전관리 . 

git log 에서 나온 commit 16진수의 맨 앞의 5자리 ; 복사 후 $git checkout 26306(다섯자리)

.

빠져나오기 : $git checkout master

$ status : 중간중간 깃의 상태를 확인한다. 

버전을 통해 관리 후 ,  git hub에 저장한다.

`$ git  init `폴더 안에 git으로 관리를 시작 할 때 .git파일을 만든다. 

git이 프로젝트 파일 상태를 계속 주시할 수 있다. 

`$ ls -a` : 숨김파일까지 모두 보기 **`.`으로 시작하는 모든 파일, 폴더는 숨길으로 보인다 **

`$ git status` : git의  상태 확인 

`$ touch`[파일명] : 파일 생성 명령

`$ rm`[파일명] : 파일 삭제 



# 2. 구글드라이버(원격저장소)에 저장 

~/TIL(git)

멀캠에서 썼던 코드들 : 원격저장소에 보관 (실제 git hub) > 원격으로 git hub으로 받아서 쓸 수 있다. 

clm으로 명령하기 

1. 어디에 ?

git hub에 저장소 생성 :  new repository > name만 지정 후 저장한다

코드 올리는 방법: https://github.com/zzomill/TIL.git http주소 복사 후 clm으로 깃에게 말해준다 

2. 올린다. 

   원격저장소 올림 $ git remote add origin [원격저장소 주소] / 저장소 별명 

   확인 : 

   YOUR profile 화면에서 확인 