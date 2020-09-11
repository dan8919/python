#사각형 클래스
# 사각형 클래스 자식>직사각형(가로,세로), 평행사변형(밑변,높이)
# 각각의 클래스에 넓이를 구하는 메소드가 있습니다
# 이 메소드를 각각의 클래스에 맞도록 작성하시오

class Project:
    def __init__(self):
        print("사각형 만들어짐")

    def weigh(self):
        print("사각형 넓이 구하는 메소드")

    def __del__(self):
        print("사각형이 삭제됨")


class Rectangle(Project):
    def __init__(self,w,l):
        print("직사각형 만들어짐")

     def weigh(self):
         print("직사각형 넓이 구하는 메소드")

    def __del__(self):
        print("직사각형이 삭제됨")



class parallelogram(Project):
    def __init__(self,u,h):
        print("직사각형 만들어짐")

     def weigh(self):
         print("평행사변형 넓이 구하는 메소드")

    def __del__(self):
        print("직사각형이 삭제됨")