from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class Barber(Base):
    __tablename__ = "barbers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    rating = Column(Integer, nullable=True, default=0)

    appointments = relationship("Appointment", back_populates="barber")

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    client_name = Column(String, nullable=False)
    time = Column(String)
    barber_id = Column(Integer, ForeignKey("barbers.id"), index=True)

    barber = relationship("Barber", back_populates="appointments",)