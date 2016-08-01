from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+mysqldb://root:wahty0673@localhost:3306/test?charset=utf8')
# metadata = MetaData(engine)
# user_table = Table('user',metadata,
#                    Column('user_id', Integer, primary_key=True),
#                    Column('user_name', String(40)),
#                    Column('password', String(10))
#                    )
#metadata.engine.echo = True
# user_table.create()
# i = user_table.select(user_table.c.user_name == 'Mary')
# print i
# print i.execute().fetchone()

# print i.execute(user_name='Mary', password='secure')
engine = create_engine('mysql+mysqldb://root:wahty0673@localhost:3306/spider?charset=utf8')
base = declarative_base()
class User(base):
    __tablename__ = 'test1'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))

# base.metadata.create_all(engine)
DBsession = sessionmaker(bind=engine)
session = DBsession()
# add
# h1 = User(name='fanyuhao')
# session.add(h1)
# session.commit()

# update
people = session.query(User).filter(User.name =='fanyuhao').first()
print people.id