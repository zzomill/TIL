# 1. git 사용법



## 1.1 Command Line Interface

> cli에서 사용하는 git 명령어 

- `mkdir`[폴더명] : make directory, 폴더 생성 
- `li` 현재위치의 폴더 내부의 파일 & 폴더를 나열  (**기본위치 : home directory : `~` **)
- `pwd` 현재 폴더 경로 출력 
- `cd`: change directory 
- 상대경로  `..` 상위 폴더이동
- `--` : 옵션 부여  예. `--global`전역설정
- `$ git status` : git의  상태 확인
- `$ touch`[파일명] : 파일 생성 명령
- `$ rm`[파일명] : 파일 삭제
- `$ ls -a` : 숨김파일까지 모두 보기 **`.`으로 시작하는 모든 파일, 폴더는 숨길으로 보인다 **



## 1.2 git 폴더 생성 준비

1. git파일 설치 : 모든 설정 기본값으로 설정한다. 

```shell
# 1. 깃 버전 확인
$ git --version
git version 2.24.1.windows.2
    
# 2. ~디렉토리 내 TIL 폴더 생성 후 폴더 리스트 확인 
$ mkdir TIL
$ ls

# 3. TIL 폴더로 이동 후 git폴더로 지정
$ cd TIL
$ git init 
> 폴더 안에 git으로 관리를 시작 할 때 .git파일을 만든다. 

# 4. .git(숨긴파일로 생성) 파일 확인 후 깃 상태 체크 
$ ls -a    
$ git status

# 5. 연습파일 생성 & 삭제하기 
$ touch [파일명] // $ git status 확인 시 붉은색 파일로 확인됨 
$ rm [파일명]
    
# 6. .md파일 깃허브 올리기 : typora에서 작성했던 .md파일 TIL 폴더에 옮긴다. 
    
```



## 1.3 git으로 폴더 관리하기

> git : 폴더단위로 프로젝트 파일 상태를 지속적으로 주시한다. 

##### 버전관리 : 어떤 파일 상태를 찍을 지 지정



##### 	1. **add** : 사진대(staging area)에 사진(file-버전관리 대상)을 올려놓는다.

`$ git add`[파일명]

`$ status` 출력 : 상태가 붉은색 -> commit 할 수 있는 대상으로 바뀐다. (초록색)

​	**2. commit** : 사진을 찍는다.(저장관리를 한다) 기본적으로 깃헙 가입 이메일을 사용 

$ git commit 이전에 global user.name, email 입력

반드시 무엇을 했는지 m를 남기면서 commit

랴

``` shell
# 7. git폴더 내 add명령 실행
$ git add [파일명] # $ git status 확인하면 [파일명] : 녹색으로 변화

# 8. 최초 commit 하기 (최초 아니면 #9.으로 뛰어넘기)
$ git commit
최초 commit 시)
*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
>> user.email과 user.name을 지정한다. 

# 8-2 최초 commit 시, 전역으로 허용되는 email, name config (설정)
$ git config -global user.email "[이메일 주소 입력]"
$ git config -global user.name "[사용자 이름 임력]"
> 설정 후 입력값 확인하기 
$ git config -global user.email 
$ git config -global user.name

# 9. commit 하기 
$ git commit -m "[기록할 메세지 입력]" 
> 반드시 -m(메세지 입력: 무엇을 했는지 기록)과 함께 commit 실행한다. 

# 10. commit 된 파일 확인하기 
$ git log 
> commit 된 모든 파일 확인 가능(찍었던 사진, 목록, 메세지 등 확인 가능)
(두번째 파일도 같은 방식으로 추가한다.)

## 11. 파일 추가 전 이전 상태로 되돌아가보기 ##
$ git log 
>맨 첫번째로 넣은 파일의 commit 263066a70915bb05416b6bb4caa102c3bd79056c : 16진수로 나온 값의 맨 앞 5자리 복사
    
# 11-2 상태 되돌아가기
$ git checkout 26306
> Note: switching to '26306'. 표시되며 두번째 파일 추가 전의 상태로 되돌아간다. 
$ ls 
> 첫번째 파일만 확인 됨

# 11-3 되돌아간 상태 빠져나오기 
$ git checkout master
Previous HEAD position was 263066a first commit
Switched to branch 'master'
> ls 확인 결과 두 개의 파일 확인 됨 
```





# 2. 원격저장소에 저장 

> 위치 : ~/TIL(git)
>
> 원격저장소(git hub)에 보관하고  원격으로 git hub으로 받아서 쓸 수 있다. 



## 2-1 저장소 위치 

git hub 사이트에서 repository 생성 :  new repository > name만 지정 후 생성한다

코드 올리기 : https://github.com/zzomill/TIL.git  > http주소 복사 후 clm으로 깃에 명령한다. 



## 2-2 업로드  

원격저장소 올림 $ git remote add origin [원격저장소 주소] 

$ git remote add origin  https://github.com/zzomill/TIL.git

```shell
# 12. 원격 저장소 생성
> 깃허브 > new repository 생성 후 저장

# 13. 원격저장소 최초 접속
(주의 이미 한 번 접속된 저장소에 다시 remote하게되면 add, commit한 설정이 없어진다.)
$ git remote add origin[new repository에서 생성된 원격저장소 주소]
> 입력 : $ git remote add origin  https://github.com/zzomill/TIL.git
> origin : 원격저장소 별명 
    
$ git remote -v
origin  https://github.com/zzomill/TIL.git (fetch)
origin  https://github.com/zzomill/TIL.git (push)
> 저장소에 접속 확인(처음 한번만 연결하면 됨)

# 14. 원격저장소에 올리기 > Git hub your profile에서 업로드 확인
$ git push origin master
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 8.10 KiB | 4.05 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To https://github.com/zzomill/TIL.git
 * [new branch]      master -> master

# 15. 수정된 파일 다시 올리기 : add, commit을 반복한다. 

```

