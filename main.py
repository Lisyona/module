import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from people import Employee, get_employees
from salary import calculate_salary

DSN = 'postgresql://postgres:Lisyona@localhost:5432/books'
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

Base.metadata.create_all(engine)


if __name__=='__main__':
    today = datetime.now().year
    print(today)
    employee_name_input = input('Введите имя сотрудника или его табель').title()
    employee_salary = Employee.calculate_salary()
    print(employee_salary)

session.close()