from flask import Blueprint, jsonify, request
from app.models.team_model import TeamModel

bp_team = Blueprint("bp_team", __name__)

@bp_team.get("/team")
def get_teams():
    list = TeamModel.query.all()
    if request.args != {}:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
        start = (page - 1) * per_page
        end = page * per_page
        limited_list = list[start:end]
    if request.args == {}:
        limited_list = list[0:10]
    return jsonify([
        {"team_name": team.team_name,
        "athletes": [
            {
                "name": athlete.name,
                "sex": athlete.sex,
                "sport": athlete.sport,
                "medal": athlete.medal
            } for athlete in team.athletes
        ]}
    for team in limited_list]), 200


@bp_team.get("/team/by_limit/<int:limit>")
def get_limit(limit):
    list = TeamModel.query.all()
    limited_list = list[0:limit]
    return jsonify([
        {"team_name": team.team_name,
        "athletes": [
            {
                "name": athlete.name,
                "sex": athlete.sex,
                "sport": athlete.sport,
                "medal": athlete.medal
            } for athlete in team.athletes
        ]}
    for team in limited_list]), 200

    
@bp_team.get("/team/by_name/<name>")
def get_name(name):
    team = TeamModel.query.filter(TeamModel.team_name == name.title()).first()
    return {"team_name": team.team_name,
        "athletes": [
            {
                "name": athlete.name,
                "sex": athlete.sex,
                "sport": athlete.sport,
                "medal": athlete.medal
            } for athlete in team.athletes
        ]}, 200