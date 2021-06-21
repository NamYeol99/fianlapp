import random
def ret_input():		
    print("1. 만난다 2. 거절한다.")		
    inp = int(input("입력: "))		
    return inp		
		
# 만약에 1 번이면 해피엔딩 2번이면 새드엔딩		
def if_show(inp):		
    if inp == 1:		
        print("해피엔딩")		
    elif inp == 2:		
        print("새드엔딩")		
    else:		
        print("게임오버")		
		
# 돈 입력 함수		
def input_money():		
    return int(input("돈을 입력: "))		
		
# 돈 뻥티기 함수		
def money_pung(m):		
    return m * 2




def data(id,pw): 
    id = 'a@a.com'
    pw = 123
def idpw_check(email,pswd):   ## 외부로부터 email,pswd 불러오기    
    if (email == 'a@a.com' and pswd == '123') :
        return '로그인성공'
    else :
        return '가입된 이메일이 없거나 패스워드가 다릅니다'
           
def rock(m) :
    print(rock)
    list = ["가위", "바위", "보"]
    com = random.choice(list)
    if m == "가위" :
        if com == "가위" :
            return "비겼습니다"
        elif com == "바위" :
            return "졌습니다"
        else :
            return "이겼습니다"

    elif user == "바위" :
        if com == "가위" :
            return "이겼습니다"
        elif com == "바위" :
            return "비겼습니다"
        else :
            return "졌습니다"

    else :
        if com == "가위" :
            return "졌습니다"
        elif com == "바위" :
            return "이겼습니다"
        else :
            return "비겼습니다"