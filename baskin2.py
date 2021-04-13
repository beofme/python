from random import *
print('게임시작!')
게임수=0
while True:
    입력값=int(input'숫자몇개?(1~3):'))
    for 숫자 in range(입력값):
        print('{}!'.format(게임수+1+숫자))
    게임수=게임수+입력값
    if 게임수>=31:
        break
    print('게임시작!')
게임수=0
while True:
    입력값=int(input('[참가자1]숫자몇개?(1~3):'))
    for 숫자 in range(입력값):
        print('{}!'.format(게임수+1+숫자))
    게임수=게임수+입력값
    if 게임수>=31:
        break

    입력값=randit(1,3)
    for 숫자 in range(입력값):
        print('{}!'.format(게임수+1+숫자))
    게임수=게임수+입력값
    if 게임수>=31:
        break
print('벌칙당첨!')
print('벌칙당첨!')