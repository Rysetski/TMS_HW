from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# Create an engine this will create a new sqlite database in current workingdir
engine = create_engine("sqlite:///shop.sqlite", echo=True) #

# Define a base class using declarative_base
Base = declarative_base()