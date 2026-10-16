from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

#DB url
DATABASE_URL = "sqlite:///./expense.db"

#create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread":False
    }
)


#session

LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#dependency
#This function is used as a fast api dependency
def get_db():
    db=LocalSession()
    #return db
    try:
        # This gives the session to the fast api
        yield db
    finally:
        # always execuetes :  db clone home imp hai 
        db.close()



Base = declarative_base()
 