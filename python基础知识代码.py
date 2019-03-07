'''
message="hello world!"
print(message)

message="hello python world!"
print(message)

favorite_language=' python '
f_lag1=favorite_language.rstrip()
f_lag2=favorite_language.lstrip()
f_lag3=favorite_language.strip()
print(f_lag1)
print(f_lag2)
print(f_lag3)

bicycle=['trek','cannondale','redline','specialized']
print(bicycle[-1].title())
message='My first bicycle is a '+bicycle[0].title()+'.'
print(message)

cars=['bwm','audi','toyato','subaru']
print(sorted(cars))
cars.sort(reverse=True)
print(cars)

# 操作列表
magicians=['alice','david','carolina']                                       成绩 觉得  的
for magician in magicians:
    print(magician.title()+",that was a great trick!")
    print("I can't wait to see your next trick,"+magician.title()+".\n") 
print("Thank you,everyone!")

# range函数
squares=[]
for value in range(1,11):  # 注意只到10!!
    square=value**2
    squares.append(square)   
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# 切片
print(squares[:4])
print(squares[-3:])

# 遍历：for循环
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
for bicycle in bicycles[:3]: 
    print(bicycle.title())  # 缩进使用制表符，一般四个空格

my_bicycles=bicycles       # 两个变量同时关联一个列表！！！！
my_bicycles.append('ofobike')
print(bicycles)
print(my_bicycles) 
my_bicycles=bicycles[:]    # 复制一个新的列表！！！！
my_bicycles.append('ofobike')
print(bicycles)
print(my_bicycles)

# 元组——不可修改的列表，用圆括号
dimensions=(200,50)
# 若想修改，只能重新赋值；


cars=['bmw','audi','toyato','subaru']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

# 条件测试：if elif else
age=12
if age<4:
    print("Your admission cost is $0.")
elif age<18:                     # 第一条不通过的才会执行第二条，因此不用写大于等于4
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# 有时也可以不使用else,用elif意思更明确
age=12

if age < 4:
    price=0
elif age < 18:
    price=10
elif age < 65:
    price=10
elif age >= 65:
    price=5

print("Your admission cost is $"+str(price)+".")

# 条件测试：是否在列表内
cars=['bmw','audi','toyato','subaru']
if 'bmw' in cars:
    print("宝马在售！")

# 字典: 遍历键和值：cars.items()；键：cars.keys();值：cars.values().
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

print("the following languages have been mentionedL")
for language in set(favorite_languages.values()):  # 包含重复元素的列表调用set()
    print(language.title())

# 字典嵌套字典,包括键和值
users={
    'aeinstein':{
        'first':'albert',
        'last' :  'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first': 'marine',
        'last' :'curie',
        'location':'paris',
        },
    }

for username, user_info in users.items():
    print("\nUsername:"+username)
    fullname = user_info['first']+user_info['last']
    location = user_info['location']

    print("\tFullname:"+fullname.title())
    print("\tLocation:"+location.title())


# 用户输入input，输入解读为字符串； int()将字符串转化为数值；
message=input("please input your name: ") 
print("Hello,"+message+"!")

height =  input("how tall are you ? ")
height = int(height)
if height>=180:
    print("\nYou're tall enough!")
else:
    print("Sorry,u are not tall enough to jump in team!")

a=8%3
print(a)





# ——————while循环————————
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1



prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""     # 必须指定初始值，否则循环的第一步没法执行
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)



# ————使用标志————
prompt  = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active=True
while active:
    message=input(prompt)
    if message == 'quit':
        active=False
    else:
        print(message)


# ————continue 返回到循环开头————
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


# ——————函数，设置默认参数————
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)


#————————返回字典——————
def build_person(first_name,last_name,age=''):
    """返回字典"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person

musician = build_person('jimi','hendrix',27)
print(musician)


#——————函数和while循环，一定记得设置退出————
def get_formatted_name(first_name,last_name):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

while True:
    print('\nPlease input your name!')
    print("Enter 'q' at any time to quit!")

    f_name = input('first name: ')
    if f_name == 'q':
        break
    l_name = input('last name: ')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print('\n'+ formatted_name)



#——————传递列表————————
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

# 模拟打印每个设计
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print('Printing model: '+current_design)
    completed_models.append(current_design)

# 显示打印好的所有模型
print('\nThe following models have been printed:')
for completed_model in completed_models:
    print(completed_model.title())


#————————接纳任意数量的形参*toppings,列表————————
# 必须放在最后
def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print("\nMaking a "+ str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')


#————————使用任意数量的关键字实参**user_info,字典————————
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们直到的有关用户的一切"""
    profile={}
    profile['first name'] = first
    profile['last name']  = last
    for key,value in user_info.items():
        profile[key] = value

    return profile

# Main program
user_profile=build_profile('alert','smith',location='princeton',field='physics')

print('user_profile{')
for key,value in user_profile.items():
    print('  '+ key + ':  '+ value)
print('}')


print(user_profile)


# ————— 导入函数模块：import function_name
# ————— 导入模块中的函数：from module_name import function_0, function_1, function_2
# ————— 起别名：from module_name import function_name as fn
# ————— 导入模块中所有的函数：from pizza import *

#——————创建类，使用类——————
class Dog():
    """一次模拟狗的简单尝试"""

    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age  = age
        
    def sit(self):
        """小狗蹲下"""
        print(self.name.title() + 'is now sitting.')

    def roll_over(self):
        """小狗打滚"""
        print(self.name.title() + 'rolled over!')


my_dog = Dog('audi',6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "years old.")

'''
















    



 
