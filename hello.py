# -*- coding: utf-8 -*-
'''print('hello, world')
a = 123
print(a);

print(not True)

classmate = ['Michael','Bob','Tracy']
print(classmate)
print(classmate[0])
classmate.clear()
#classmate.pop()
print(classmate)

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

t =(1,)
print(t) 

age = 20
if age >= 6:
    print('teenager')
elif age > 18:
    print('adult')
else:
    print('kid')

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

names = ['Michael','Bob','Tracy']
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

asum = 0
for y in list(range(101)):
    asum = asum + y
print(asum)

d = {'Michael': 95,'Bob': 75,'Tracy': 85}
print(d['Michael'])

aflag = 'Bob' in d
print(aflag)
print(d.get('Michael'))
print(d.get('Mi',-1))

a = 'abc'
print(a.replace('a','A'))
print(a)
print(1+2+3)
import math

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x

def move(x,y,step,angle=0):
    nx = x + step*math.asin(angle)
    ny = y + step*math.acos(angle)
    return nx,ny

ax,ay = move(2,3,3)
print(ax,ay)
r = move(100,100,60,math.pi / 6)
print(r)

def power(x):
    return x * x

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc())'''

"""def hello(greeting,*args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
         print('%s, %s!' % (greeting, ', '.join(args)))

print(hello('Hello', 'Michael', 'Bob', 'Adam'))

names = ('tom','jmk')
print(hello('Hello',*names))

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
names = ['Micheal','sun','tracy']
for name in names:
    print(name)

print(list(range(5)))
# __name__=='main'

d = {'Michael':95,'Bob':75,"Tracy":85}
print(d['Michael'])
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
d = {'a':1,'b':2,'c':3}
for key  in d:
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():
    print(k,'==',v)
print(list(range(1,11)))
print([x*x for x in range(1,11)])
def  odd():
    print("step1")
    yield(1)
    print("step 2")
    yield(2)
    print("step 3")
    yield(3)
o = odd()
next(o)
next(o)
next(o)"""

"""def triangles():
    N=[1]
    while True:
        yield N
        N.append(0)
        N=[N[i-1] + N[i] for i in range(len(N))]
n=0
for t in triangles():
    print(t)
    n=n+1
    if n == 10:
        break
还是让我们过一遍代码：
1行，定义函数
2行，给N赋值
4行，函数遇到yield返回N=[1]
5行，给N添加一个元素，此时N=[1，0]
6行，高潮来啦，还是分开讲，range(len(N))=[0,1],
so, N = [N[i-1]+N[i] for i in [0,1]] 
so, N = [N[0-1]+N[0] , N[1-1]+N[1]]
so, N = [0+1 , 1+0] = [1,1] 
这样，杨辉三角的第二行就出来啦！"""

def  f(x):
    return x*x

print(list(map(f,[1,2,3,4])))

from functools import reduce
def fn(x,y):
    return 10 * x + y

print(reduce(fn,[1,3,5,7,9]))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '  ', 'B', None, 'C', '  '])))

def lazy_sum(*args):
    def sum():
        ax =  0
        for n in args:
            ax = ax + n
        return  ax
    return sum 

""" def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25') 

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2018-09-08')

now()"""

"""def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)"""

'''from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

from datetime import datetime
print(datetime.now())

print(dir('ABC'))

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print(obj.power())

from datetime import datetime
with open('test.txt','w',encoding='utf-8') as f:
    f.write('今天是')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt','r',encoding='utf-8') as f:
    s = f.read()
    print('prepare read file')
    print(s)

with open('test.txt','rb') as f:
    s = f.read()
    print('prepare read file')
    print(s) '''

def power(x,n=5):
    s= 1
    while n >0 :
        n = n-1
        s = s * x
    return s
print(power(3))

def hello(greeting, *args): 
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi', 'Sarah')
names =  ('Bart', 'Lisa')
hello('Hello', *names)

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('Michael',30,city='Beijing',job='work1')

