import csv
import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

db_path = "RL.db"
engine = create_engine(os.getenv("RL.db", f"sqlite:///{db_path}"))
db = scoped_session(sessionmaker(bind=engine))

def main():

    rls = db.execute(text("SELECT id, name, rank, peak_rank FROM rl")).fetchall()
    for rl in rls:
        print(f"Id and username is {rl.id}, {rl.name}, rank is {rl.rank} and the peak rank is {rl.peak_rank}.")

    rl_id = int(input("\nRL ID: "))
    rl = db.execute(text("SELECT name, rank, peak_rank FROM rl WHERE id = :id"), 
    {"id": rl_id}).fetchone()


    if rl is None:
        print("Error: Not found.")
        return

    deezs = db.execute(text("SELECT name FROM rl WHERE id = :id"), 
    {"id": rl_id}).fetchall()


    print("\nNames: ")
    for deez in deezs:
        print(deez.name)
    if len(deezs) == 0:
        print("No name found.")

if __name__ == "__main__":
    main()
