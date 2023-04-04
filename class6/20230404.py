# class Person():
#     def __init__(self, name, age, favoritefood):
#         self.name = name
#         self.age = age
#         self.favoritefood = favoritefood

#     def introduce(self):
#         print("我是"+self.name+"，"+"我今年"+str(self.age)+"歲，"+"最喜歡吃"+self.favoritefood)


#     def shout(self, content):
#         print("我大喊: 「"+content)

# AA = Person("Prince", 20, "roast beef")

# AA.introduce()
# AA.shout("我討厭看牙醫!」")

# class Cars:
#     #類別屬性: 屬於類跌的屬性，而不是物件!
#     door = 4

#     #實體方法(Instance Method)
#     def drive(self):
#         self.__class__.door = 5


# print("Cars original door: ", Cars.door)
# mazda = Cars()
# mazda.drive()
# print("Cars new door: ", Cars.door)

# class Person():
#     state = "healthy"

#     def getcold(self):
#         self.__class__.state = "I'm sick."


# print("Original: I'm", Person.state, ".")
# Prince = Person()
# Prince.getcold()
# print("After getcold(): ", Person.state)



#顏色類別
# class Person():


#     #建構式
#     def __init__(self, eyescolor, haircolor):
#         self.eyescolor = eyescolor
#         self.haircolor = haircolor

#     #美國人
#     @classmethod
#     def american(cls):
#         return cls("blue", "brown")
    
#     #台灣人
#     @classmethod
#     def taiwanese(cls):
#         return cls("black", "black")


#     def introduce(self):
#         print("My eyescolor is"+self.eyescolor+", and my hair color is "+self.haircolor+".")
    

# American = Person.american()
# Taiwanese = Person.taiwanese()

# American.introduce()
# Taiwanese.introduce()


# class Person():

#     @staticmethod
#     def work(working_hours):
#         return working_hours

# working_hours = 8

# print("Working hours: ", working_hours)

