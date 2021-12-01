from app.configs.database import db
from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy.orm import validates, relationship
import psycopg2


@dataclass
class AthletesModel(db.Model):
    id: int
    name: str
   
    __tablename__ = 'athletes'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sex= db.Column(db.String, nullable=False)
    sport= db.Column(db.String, nullable=False)
    medal= db.Column(db.String, nullable=False)
    team_id= db.Column(db.Integer, db.ForeignKey('teams.id'), nullable= False)

    
    