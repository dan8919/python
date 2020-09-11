class Dog:
    a,b=0,0
    def __init__(self,name):
        self.name = name
        print(self.name,"Dog was Born")

    def speak(self,a,b):
        print("yelop!",self.name,a,b)

    def wag(self):
        print("Dog's wag tail")

    def __q(self):
       print("__붙이면 비밀공간. 밖에서 못부름")


    def __del__(self):
        print("destry!!")


#dog 를 상속받음
#class 는 명세에 있음,static 명세에 있음



#class Puppy(Dog):
#     def __init__(self):
#
#    # def __q(self):
#         print("__붙이면 비밀공간. 밖에서 못부름")
#
#     def __del__(self):


puddle = Dog("puddle")
sheperd = Dog("sheperd")
puddle.speak(1,2)


#self 진짜 나 instence