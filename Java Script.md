## 1. Java Script 

- html에서 **직접보여지는 요소**들을 직접 제어 

- 웹 브라우저에서 사용된다 
  - html의 정적 요소를 동적으로 지원
  - 숫자연산.. 아닌 html요소를 건드리는 쪽으로 쓰인다. 

- 서버에서 바로 구동 : Node.js 로 만든다
- 텐서플로우 등 결과물을 표현할 때 JS를 활용하면 자유자재로 쓸 수 있다.
  - 파이썬 - 그래프 표현까지 한계

참고 

- angular JS
- react JS

형식 

- CSS와 비슷하다 :  `<script> </script>`구조 (style 태그는 위치 상관 없음)



## 2. 규칙

### 2.1 변수 사용

- 변수의 자료 type이 없다.  : 초기화 할 필요가 없음 
- 모든 변수는 무조건 `var`를 선언한다. 
  - 브라우저 별로(IE, Chrome) 알아서 변수를 해석해서 동작하게 한다. 
  - 변수는 재선언이 가능하지만, 위험하다.
- 변수에 함수자체를 담을 수 있다. `var myFunc = funtion(){};` (자바는 불가능)



### 2.2 함수 사용

> 매개변수 타입이 없다. 리턴도 없다. `변수()` 형태. 

##### 출력함수

- alert()  : 사용자에게 pop-up창으로 출력
- write() : 써버린다. => 기존에 작성된 것들 다 날리고 새로써진다(실제로 잘 안 씀)
  - 예. `document.forms[index]` 
- console.log : 개발자페이지에서만 확인 가능 



##### 입력함수 2가지 

- prompt() : 많은 것들을 출력 가능
- confirm() : True/False 로 입력 



### 2.3 연산자	

##### Boolean 

- `===`  : 자료의 형태까지 비교
- 0, 1을 False/True로 인지
  - 예. true == 1



##### 숫자, 문자 

- `" "` 안의 숫자를 String으로 구분하지 않는다.

  - "1" == 1 , "23" = 23
  - '10' * '2' = 20  // 숫자로 연산 

- 숫자보다 문자열이 더 강하다 

  - 10 + '2' = 102  // 문자열로 출력
  - 문자를 숫자로 바꿀 때 : `*1`로 처리한 후 계산한다. 

  

##### 배열

- index값을 'a' 문자열로 쓸 수 있게 지원한다
  - 반복문으로 문자열을 index로 가지는 배열의 요소를 `for in`형태로 뽑아낼 수 있다. 

## 3. Json 형태 

>  자바스크립트에서 object를 Notation(표기)하는 방법. 배열이 아니다. 

