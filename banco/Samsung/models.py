from sqlalchemy import create_engine, Column,Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividade.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Sintomas(Base):
    __tablename__='sintomas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))

    def __repr__(self):
        return '<sintoma {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Doencas(Base):
    __tablename__='doencas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    sintoma_id = Column(Integer, ForeignKey('sintomas.id'))
    sintoma = relationship("Sintomas")


    def __repr__(self):
        return '<doenca {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':

    init_db()


