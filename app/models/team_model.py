from app.configs.database import db
from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy.orm import validates, relationship
import psycopg2


@dataclass
class TeamModel(db.Model):
    id: int
    team_name: str
   
    __tablename__ = 'teams'


    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String, nullable=False)
    

    athletes = relationship('AthletesModel', backref='team', uselist=True)