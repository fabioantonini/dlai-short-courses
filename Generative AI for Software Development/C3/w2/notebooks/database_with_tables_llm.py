from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Association table for many-to-many relationship between People and Hobbies
people_hobbies = Table('people_hobbies', Base.metadata,
    Column('person_id', Integer, ForeignKey('people.id'), primary_key=True),
    Column('hobby_id', Integer, ForeignKey('hobbies.id'), primary_key=True)
)

class Person(Base):
    __tablename__ = 'people'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    hometown = Column(String)
    
    # Many-to-many relationship with hobbies
    hobbies = relationship('Hobby', secondary=people_hobbies, back_populates='people')
    
    # One-to-many relationship with relationships (as person1)
    relationships = relationship('Relationship', back_populates='person1')

class Hobby(Base):
    __tablename__ = 'hobbies'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    # Many-to-many relationship with people
    people = relationship('Person', secondary=people_hobbies, back_populates='hobbies')

class Relationship(Base):
    __tablename__ = 'relationships'
    
    id = Column(Integer, primary_key=True)
    person1_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    person2_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    relationship_type = Column(String, nullable=False)  # e.g., 'family', 'friend', 'colleague', 'schoolmate'
    
    # Relationships to the Person table
    person1 = relationship('Person', foreign_keys=[person1_id], back_populates='relationships')
    person2 = relationship('Person', foreign_keys=[person2_id])

# Create an SQLite database
engine = create_engine('sqlite:///social_network.db', echo=True)

# Create tables
Base.metadata.create_all(engine)