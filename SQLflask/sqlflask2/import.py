import csv
import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

db_path = "class.db"
engine = create_engine(os.getenv("class.db", f"sqlite:///{db_path}"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("class.csv")
    reader = csv.reader(f)
    for name, marks, grade in reader:
        db.execute(text("INSERT INTO class (name, marks, grade) VALUES (:name, :marks, :grade)"),
                   {"name": name, "marks": marks, "grade": grade})
        print(f"Student name is {name}. The student marks is {marks} and the grade is {grade}.")
    db.commit()

if __name__ == "__main__":
    main()
