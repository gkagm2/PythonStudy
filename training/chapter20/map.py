# map()함수는  map(함수, 리스트) 형태로 사용한다.
# 이 함수는 함수와 리스트를 인자로 받는다. 그리고 리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음,
# 그 결과를 새로운 리스트에 담아준다.

print(map(lambda x: x ** 2, range(5))) # python2 version

print(list(map(lambda x: x**2, range(5)))) # python3 or 2 version
# map함수는 리스트에서 원소를 하나씩 꺼내서 함수를 적용시킨 결과를 새로운 리스트에 담아주니까 위의 예제는 0을 제곱하고 1을 제곱하고
# 2,3,4를 제곱한 것을 새로운 리스트에 넣어주는 것이다.