array = [1, 2, 3, "four", "five", True]
print(array) # 리스트 전체가 출력됨
print(array[4:])
print(array[-1]) # 마지막 원소만 출력한다 
print(array[-2]) 


dust = {'abc' : 50, 'cdf' : 40}
print(dust)
# value만 뽑기 : [key]사용 키값은 반드시 스트링 형태 
print(dust['abc'])

dust_two = dict(abc = 50, cdf = 40)  #dict(변수형태) 스트링이 들어가면 안됨
print(dust_two)
print(dust_two['abc'])
