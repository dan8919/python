#첫줄입력은 도표 칸이 몇개
n = int(input())
x,y = 1,1
#두번째 줄 경로
plans = input().split()


#LRUD에 따른 이동 ,방향 rlud
dx = [0,0,-1,1]
dy = [1,-1,0,0]
move_type = ['R','L','U','D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
     #밖으로 빠져나가는 경우
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    #밖에 빠져나가지 않으면 이동 수행
    x,y = nx,ny

print(x,y)


