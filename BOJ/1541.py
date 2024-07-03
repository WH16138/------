# 기본 아이디어 : 한번이라도 - 부호가 나오는 순간 뒤에 모든 수는 괄호를 적절히 배치하여 음수로 만들 수 있다. 
numbers = [sum(map(int,x.split('+'))) for x in input().split('-')] # 식을 입력받아 - 기준으로 분할 하고, 합연산을 시행
print(numbers[0]-sum(numbers[1:])) # 맨 앞 값은 더하고, - 뒤의 값들은 모두 음수 처리하여 결과 출력