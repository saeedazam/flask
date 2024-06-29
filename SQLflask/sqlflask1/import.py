import csv
import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

db_path = "RL.db"
engine = create_engine(os.getenv("RL.db", f"sqlite:///{db_path}"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("RL.csv")
    reader = csv.reader(f)
    for name, rank, peak_rank in reader:
        db.execute(text("INSERT INTO rl (name, rank, peak_rank) VALUES (:name, :rank, :peak_rank)"),
                   {"name": name, "rank": rank, "peak_rank": peak_rank})
        print(f"Added username  {name}. The rank is {rank} and the peak rank is {peak_rank}.")
    db.commit()

if __name__ == "__main__":
    main()
