# -*- coding:utf-8 -*-
__author__ = 'flybrower'
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print('len(classmates)=', len(classmates))

def print_scores(**kw):
    print('-------------score------------')
    print('------------------------------')
    for name,score  in kw.items():
        print('%10s %d' %(name,score))
        print()

data = {
       'tom' : 89,
       'sundy': 90,
       'jim' : 78
}

def print_info(name,*,gender,city='beijing',age):
    print('Personal Info')
    print('----------------')
    print(' name:%s ' %name)
    print(' gender:%s ' %gender)
    print(' City: %s' % city)
    print(' Age: %s' % age)

if __name__ == '__main__':
    print_scores(tom=78,jenny=98,john=87)
    print_scores(**data)

