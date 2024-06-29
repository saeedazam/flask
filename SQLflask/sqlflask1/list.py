import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker


db_path = "RL.db"
engine = create_engine(os.getenv("RL.DB", f"sqlite:///{db_path}"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    rls = db.execute(text("SELECT name, rank, peak_rank FROM rl")).fetchall()
    for rl in rls:
        print(f"username is {rl.name}, rank is {rl.rank} and the peak rank is {rl.peak_rank}.")

if __name__ == "__main__":
    main()
