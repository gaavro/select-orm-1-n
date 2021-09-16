from flask import Flask


def init_app(app: Flask):
    from app.views.team_view import bp_team
    app.register_blueprint(bp_team)

    from app.views.athlete_view import bp_athlete
    app.register_blueprint(bp_athlete)