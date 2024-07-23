# Git과 Github

## [1] Git이란?
 - (분산) 버전 관리 프로그램 

## [2] Git 시작하기
누가 어떠한 변경 사항을 남겼는지, git이 자동으로 만들어 주기 위해서 필요하다! 
global 한 정보를 주었기 때문에 "최초" 한번만 설정하면 됩니다. 
- git init 저장소 만들 때 마다 / config는 한번만 해도 됨 

```
git config --global user.name "이름"
git config --global user.email "메일 주소"
```

확인하기 위해서는
```
git config --global --list 
```
## [3] Git의 3공간 
1. wroking directory -> 분장실  
2. Staging Area -> 무대 
3. Repository -> 사진 저장소 

분장실  -> 무대 -> 사진 저장소로 우리가 사진을 찍어 내기 위해서?
기본 명령어를 사용한다!

## [4] Git 기본 명령어 
### (1) git init : 로컬 저장소 생성 
```
# 로컬 저장소를 만든다 -> 현재 작업 중인 디렉토리(폴더)를 Git으로 관리할 것이라는 선언
git init
```
`(master)` 표시 생성

### (2) git add : Staging Area로 부르는 명령어

Wokring directory 에서 작업이 완료된 파일을 무대 위로 올린다. 
```
git add 파일명 (버전을 관리하고자 하는 파일명)
```

### (3) git commit -m '변경사항 사유'

Staging area 즉, 무대 위에 있는 모델의 사진을 찍는다. 기록한다. 

```
git commit -m "변경사항이 기록된 이유"
``` 

> 메세지를 남기는 이유 ? 
버전 관리 프로그램 git이 자동으로 변경사항에 대한 "육하원칙"을 작성하기 위해
왜 바꾸었는지에 대한 정보가 필요함. 

## (4) Git status

각 파일들의 상태를 알려줌 (Untracked, Modified, New file...)

```
git status
```
## (5) Git log

의미 : 변경 사항들의 기록을 보여줘 

```
git log ---oneline 
```
더 다양하게 배우면 - 그래프도 그려낼 수 있음 

===> 로컬 저장소 : 내 컴퓨터에서 버전관리하기 


## Github
서버 컴퓨터처럼! 원격에서 나의 변경 사항 기록들을 가지고 있도록 사용할 수 있다!

### (1) repository 생성
1. 우측 상단 + 버튼 눌러서, repository 만든다. 
2. URL 생성된다. -> 원격 저장소의 주소를 의미합니다.
3. 복사!
   
### (2) 로컬 저장소와 연결 
```
# 원격 저장소 연결  (in Vs code terminal)

git remote add origin URL

# 원격 저장소 연결을 확인 
git remote -v
(연결된 길목을 보여주는 명령어)
```

### (3) 변경사항을 로컬 저장소에서 원격저장소로 보내기

psuh origin master: 로컬 저장소의 커밋(변경사항)을 원격 저장소에 반영 
```
git push origin master
```
의미 : 깃아 올려다오 origin이라고 이름붙인 master 브랜치에

