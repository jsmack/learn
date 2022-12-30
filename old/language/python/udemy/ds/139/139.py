# import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# sqllite inmemory をオブジェクト化
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost/test_mysql_database2', echo=True)

#sqlアルカミーのdeclarative_baseを継承したBaseクラスを作成
Base = sqlalchemy.ext.declarative.declarative_base()


# Personクラスを作成
class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(sqlalchemy.String(14))

# engineに　Personの形をしたテーブル情報を書き込み
Base.metadata.create_all(engine)
#engine.execute('DROP TABLE zoo')
#engine.execute('CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)')


# セッションクラスを定義
Session = sqlalchemy.orm.sessionmaker(bind=engine)

#オブジェクト化
session = Session()

#personオブジェクト生成にMikeを設定
p1 = Person(name='Mike')
#ins = "INSERT INTO zoo (critter, count, damages) VALUES (%s, %s, %s)"
#engine.execute(ins, "あひる", 10, 0.0)
#engine.execute(ins, "くま", 2, 1000.0)
session.add(p1)

p2 = Person(name='Nancy')
session.add(p2)

p3 = Person(name='Jun')
session.add(p3)


# sessionオブジェクトにadd
session.commit()

p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
session.commit()


p5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p5)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)

#rows = engine.execute('SELECT * FROM zoo')
#for row in rows:
#    print(row)

