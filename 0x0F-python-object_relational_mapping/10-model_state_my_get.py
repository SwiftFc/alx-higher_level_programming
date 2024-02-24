from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Check if the number of arguments is correct
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            argv[0]))
        exit()

    # Creating the connection string (engine for database)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Creating an instance of Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying the State Objects with the specified name searched for
    state_name = argv[4]
    queried_state = session.query(State).filter(
        State.name == state_name).first()

    # Displaying the results
    if queried_state:
        print("{:d}".format(queried_state.id))
    else:
        print("Not found")

    # Closing the session
    session.close()
