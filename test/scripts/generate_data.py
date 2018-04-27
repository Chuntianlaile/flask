import os, json
from random import randint
from faker import Faker
from test.models import db, User, Course, Chapter

f = Faker('zh-cn')
# image_url='http://www.hinews.cn/pic/0/11/43/80/11438010_485243.jpg'

def iter_user():
    return User(
        name='Kobe', 
        email='kobe@qq.com',
        password='shiyanlou',
        job='前 NBA 超级巨星'
    )

def iter_course():
    author = User.query.filter_by(name='Kobe').first()
    with open(os.path.join(os.path.dirname(__file__), 'data.json')) as file:
        courses = json.load(file)
    for c in courses:
        yield Course(
            name=c['name'],
            description=c['description'],
            image_url=c['image_url'],
            author=author
        )

def iter_chapter():
    for c in Course.query:
        for i in range(randint(3, 10)):
            yield Chapter(
                name=f.sentence(),
                course=c,
                video_url='https://labfile.oss.aliyuncs.com/courses/923/week2_mp4/2-1-1-mac.mp4',
                video_duration='{}:{}'.format(randint(10, 30), randint(10, 60))
            )

def run():
    db.session.add(iter_user())
    for i in iter_course():
        db.session.add(i)
    for i in iter_chapter():
        db.session.add(i)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()

if __name__ == '__main__':
    run()
