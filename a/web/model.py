# -*- coding: utf-8 -*-
__author__='flybrower'

import time,uuid

'''def next_id():
    return '%015d%s000' % (int(time.time() * 1000),uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(500)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'
    
    id  = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)'''

'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
        print('2015-3-25')'''


def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')


now()


