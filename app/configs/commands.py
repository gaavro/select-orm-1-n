from flask import Flask, current_app
from flask.cli import AppGroup
from app.models.athletes_model import AthletesModel
from app.models.team_model import TeamModel
from ujson import load



def read_json(filename: str):
    with open(filename) as j_file:
        return load(j_file)



def cli_team(app: Flask):
    cli = AppGroup('cli_team')

    @cli.command("create")
    def cli_team_create():
        session = current_app.db.session

        data = read_json("snippet_team.json")

        to_insert = [TeamModel(team_name=key) for key in data.keys()]

        session.add_all(to_insert)
        session.commit()

    app.cli.add_command(cli)


def cli_athletes(app: Flask):
    cli = AppGroup('cli_athletes')

    @cli.command("create")
    def cli_athlets_create():
        session = current_app.db.session

        data_team = read_json("snippet_team.json")
        data_athletes = read_json("snippet_athletes.json")

        for row in data_athletes:
            row["team_id"] = data_team[row["team"]]
            row.pop("team")

        to_insert = [AthletesModel(**data) for data in data_athletes]
        

        session.add_all(to_insert)
        session.commit()

    app.cli.add_command(cli)



def init_app(app: Flask):
    cli_team(app)
    cli_athletes(app)

