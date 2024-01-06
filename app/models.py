from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Boolean, Time, DateTime, Enum
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app import db
from enum import Enum as UserEnum

class Role(UserEnum):
    Customer = 1
    Admin = 2
    Employee = 3

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
class Account(BaseModel, UserMixin):
    __tablename__ = 'account'

    name = Column(String(50), nullable=False)
    account_id = Column(String(20), nullable=False, unique=True)
    password = Column(String(50), nullable=False)

    customer = relationship("Customer", uselist=False, back_populates="acccount")
    employee = relationship("Employee", uselist=False, back_populates="account")
    admin = relationship("Admin", uselist=False, back_populates="account")
    type_account = Column(Enum(Role))

class Employee(db.Model):
    __tablename__ = 'employee'

    id = Column(Integer, ForeignKey('account.id'), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    phone_number = Column(String(15), nullable=False)
    account = relationship("Account", back_populates="employee")
    flight_ticket = relationship("FlightTicket", uselist=False, backref="employee")
    schedule = relationship("Schedule", uselist=False, backref="employee")
    receipt = relationship('Receipt', backref='employee', lazy=True)


class Admin(db.Model):
    __tablename__ = 'admin'

    id = Column(Integer, ForeignKey('account.id') , primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    account = relationship("Account", back_populates="admin")
    regulation = relationship('Regulation', backref='admin', lazy=True)

class Regulation(BaseModel):
    __tablename__ = 'regulation'

    id = Column(String(10), primary_key=True)
    airport_count = Column(Integer)
    max_flight_time = Column(Integer)
    min_flight_time = Column(Integer)
    max_stopover_time = Column(Integer)
    min_stopover_time = Column(Integer)
    ticket_class_count = Column(Integer)
    ticket_class_table = Column(String(50))
    ticket_sales_time = Column(Integer)
    ticket_booking_time = Column(Integer)

    admin_id = Column(Integer, ForeignKey(Admin.id), nullable=False)
class Customer(db.Model):
    __tablename__ = 'customer'

    id = Column(Integer, ForeignKey('account.id'), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    cccd = Column(String(12), nullable=False, unique=True)
    sdt = Column(String(15), nullable=False)
    account = relationship("Account", back_populates="customer")
    flight_ticket = relationship('FlightTicket', backref='customer', lazy=True)
class Revenue(BaseModel):
    __tablename__ = 'revenue'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    flight_count = Column(Integer)
    rate = Column(Float)
    revenue = Column(Float)
    receipt = relationship("Receipt", backref="revenue")
    route = relationship("Route", backref="revenue")

class Receipt(BaseModel):
    __tablename__ = 'receipt'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    receipt_date = Column(Date, nullable=False)
    total_amount = Column(Float, nullable=False)

    # flight_ticket = relationship("FlightTicket", backref="receipt")
    employee_id = Column(Integer, ForeignKey(Employee.id), nullable=False)
    revenue_id = Column(Integer, ForeignKey(Revenue.id), nullable=False)
class FlightTicket(BaseModel):
    __tablename__ = 'flight_ticket'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_status = Column(Enum('booked', 'confirmed', 'canceled'))
    ticket_price = Column(Float)
    receipt = Column(Integer, ForeignKey('receipt.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    # revenue = relationship("Revenue", back_populates="route")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
class Schedule(BaseModel):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True, autoincrement=True)
    departure_airport = Column(String(50))
    arrival_airport = Column(String(50))
    flight_duration = Column(Time)
    seats_class1 = Column(Integer)
    seats_class2 = Column(Integer)
    datetime = Column(DateTime)

    employee_id = Column(Integer, ForeignKey(Employee.id), nullable=False)

class Flight(BaseModel):
    __tablename__ = 'flight'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_name = Column(String(50))

    schedule = relationship("Schedule", back_populates="flight")

    route_id = Column(ForeignKey("route.id"), primary_key=True)
    schedule_id = Column(ForeignKey("schedule.id"), primary_key=True)
class Route(BaseModel):

    __tablename__ = 'route'

    id = Column(Integer, primary_key=True, autoincrement=True)
    departure_location = Column(String(50))
    arrival_location = Column(String(50))
    departure_time = Column(Time)
    arrival_time = Column(Time)

    revenue = Column(Integer, ForeignKey(Revenue.id), nullable=False)

# class Airport(BaseModel):
#     __tablename__ = 'airport'
#
#     id = Column(String(50), primary_key=True)
#     airport_name = Column(String(50))
#
#     route = relationship("Flight", backref="airport")


if __name__ == "__main__":
    from app import app
    with app.app_context():

    # db.session.commit()
        db.drop_all()
        db.create_all()