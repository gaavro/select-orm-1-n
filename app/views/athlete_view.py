from flask import Blueprint, jsonify, request
from app.models.athletes_model import AthletesModel
bp_athlete = Blueprint("bp_athlete", __name__)

@bp_athlete.get("/athlete")

def get_athlete():
    list = AthletesModel.query.all()
    if request.args != {}:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
        start = (page - 1) * per_page
        end = page * per_page
        limited_list = list[start:end]
    if request.args == {}:
        limited_list = list[0:10]
    return jsonify([{
        "name": athlete.name,
        "medal": athlete.medal,
        "team": athlete.team.team_name,
        "sex": athlete.sex,
        "sport": athlete.sport
    } for athlete in limited_list]), 200

@bp_athlete.get("/athlete/by_sex/<sex>")
def get_sex(sex):
    list = AthletesModel.query.filter(AthletesModel.sex == sex.title()).all()
    if request.args != {}:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
        start = (page - 1) * per_page
        end = page * per_page
        limited_list = list[start:end]
    if request.args == {}:
        limited_list = list[0:10]
    return jsonify([{
        "name": athlete.name,
        "medal": athlete.medal,
        "team": athlete.team.team_name,
        "sex": athlete.sex,
        "sport": athlete.sport
    } for athlete in limited_list]), 200

@bp_athlete.get("/athlete/by_name/<name>")
def get_name(name):
    list = AthletesModel.query.filter(AthletesModel.name.contains(name.title() or name.lower())).all()
    if request.args != {}:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
        start = (page - 1) * per_page
        end = page * per_page
        limited_list = list[start:end]
    if request.args == {}:
        limited_list = list[0:10]
    return jsonify([{
        "name": athlete.name,
        "medal": athlete.medal,
        "team": athlete.team.team_name,
        "sex": athlete.sex,
        "sport": athlete.sport
    } for athlete in limited_list]), 200

@bp_athlete.get("/athlete/by_medal_sport/<medal>")

def get_medal(medal):
    list = AthletesModel.query.filter(AthletesModel.medal.contains(medal.title())).all()
    if request.args != {}:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
        start = (page - 1) * per_page
        end = page * per_page
        limited_list = list[start:end]
    if request.args == {}:
        limited_list = list[0:10]
    return jsonify([{
        "name": athlete.name,
        "medal": athlete.medal,
        "team": athlete.team.team_name,
        "sex": athlete.sex,
        "sport": athlete.sport
    } for athlete in limited_list]), 200