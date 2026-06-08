from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, Session, joinedload

# 1. Engine — connects to SQLite for today
engine = create_engine("sqlite:///cutabove_orm.db", echo=True)

# 2. Base — parent class for all models
class Base(DeclarativeBase):
    pass

# 3. Models
class Barber(Base):
    __tablename__ = "barbers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)

    appointments = relationship("Appointment", back_populates="barber")

    def __repr__(self):
        return f"Barber(id={self.id}, name={self.name})"


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    client_name = Column(String, nullable=False)
    time = Column(String)
    barber_id = Column(Integer, ForeignKey("barbers.id"))

    barber = relationship("Barber", back_populates="appointments")

    def __repr__(self):
        return f"Appointment(id={self.id}, client={self.client_name})"


# Create tables
Base.metadata.create_all(engine)
print("\nTables created")


# Insert data
with Session(engine) as session:
    kwame = Barber(name="Kwame", phone="0241234567")
    kofi = Barber(name="Kofi", phone="0559876543")
    
    session.add_all([kwame, kofi])
    session.flush()  # assigns IDs without committing

    session.add_all([
        Appointment(client_name="Emmanuel", time="09:00", barber_id=kwame.id),
        Appointment(client_name="Kojo", time="10:00", barber_id=kwame.id),
        Appointment(client_name="Abena", time="09:30", barber_id=kofi.id),
    ])
    
    session.commit()
    print("Data inserted")


    # N+1 demonstration
print("\n--- N+1 problem ---")
with Session(engine) as session:
    barbers = session.query(Barber).all()
    for barber in barbers:
        print(f"{barber.name} has {len(barber.appointments)} appointments")


# Fixed with joinedload
print("\n--- Fixed with joinedload ---")
with Session(engine) as session:
    barbers = session.query(Barber).options(
        joinedload(Barber.appointments)
    ).all()
    
    for barber in barbers:
        print(f"{barber.name} has {len(barber.appointments)} appointments")