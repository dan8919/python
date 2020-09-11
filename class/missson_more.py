#이름,나이,성별을 입력받아,"당신의 이름은{},나이는{},성별은{} 입니다"출력하기#
cmd = input("input(usage: 이름,나이,성)>> ")
print(cmd)
cmds = cmd.split(',')
# print("당신의 이름은"+cmds[0]+",나이는"+cmds[1]+",성별은"+cmds[2])
# 1값 존재 여부 확인
error_msg="정확하게 입력해 주세요"
if cmd=="":
    print("정확히 입력해 주세요!!")
    # 나오기
    exit()
#2. ,가 있는지 체크
# if cmd.find(",")==-1
if "," not in cmd:
    print(error_msg)
    exit()

# 3.세개의 값이 있는지 체크
if len(cmds) != 3:
    print(error_msg)
    exit()






outmsg="당신의 이름은 {},나이는 {},성별은 {} 입니다."
print(outmsg.format(cmds[0],cmds[1],cmds[2]))