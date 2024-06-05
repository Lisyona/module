import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import select

DSN = 'postgresql://postgres:Lisyona@localhost:5432/books'
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    employee_id = sq.Column(sq.Integer, primary_key=True)
    employee_name = sq.Column(sq.String(length=40), unique=True)
    employee_wage = sq.Column(sq.Float, nullable=False)
    working_hours = sq.Column(sq.Float, nullable=False)

def create_tables(engine):
    Base.metadata.create_all(engine)

def get_employees(employee_name_input):
    if employee_name_input.isdigit()==True:
        wage = employees.employee_wage.session.query(Employee).where(Employee.employee_id==employee_input)
        working_hours = employees.employee_wage.session.query(Employee).where(Employee.employee_id == employee_input)
    else:
        wage = employees.employee_wage.session.query(Employee).where(Employee.employee_name==employee_input)
        working_hours = employees.employee_wage.session.query(Employee).where(Employee.employee_id == employee_input)
    return(wage, working_hours)
