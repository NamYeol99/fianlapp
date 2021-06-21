
print("게임 시작")			
print("누구를 만났습니다")			
print("누구를 만났을까요? (엔터~)")			
input()			
print("과연 누구를 ~~~ (엔터~)")			
input()			
import random			
# import hello			
from hello import ret_input, if_show, input_money, money_pung
# 입력담당하는 기능			
a = ret_input()			
# 값이 들어 왔을 때 해당하는 내용으로 출력 하는 기능			
# 입력을 받아서 그 입력값을 넣으면			
if_show(a)			
			
# 돈을 입력하는 기능			
m = input_money()			
# 넣은 돈 출력			
print("당신의 돈은 {}원".format(m))			
# 그 돈을 넣으면 3배로 뻥튀기 해주는 기능			
input("수리 수리 마수리~~ 얍!!(엔터)")			
# 뻥튀기 된 돈을 출력			fdsfdfdsf
print("당신의 돈은 {}원".format(money_pung(m)))		


