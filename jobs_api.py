import flask
import requests

from data import db_session

from data.users import User
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return flask.jsonify({'jobs': [item.to_dict(
        only=('id', 'job', 'team_leader', 'work_size', 'collaboration',
              'start_date', 'end_date', 'is_finished', 'category')
    )
    for item in jobs]})


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_jobs(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return flask.jsonify({'errore': 'Not found'})
    return flask.jsonify({'jobs': [item.to_dict(
        only=('id', 'job', 'team_leader', 'work_size', 'collaboration',
              'start_date', 'end_date', 'is_finished', 'category'))
        for item in jobs]})

@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not requests.json:
        return flask.jsonify({'jobs':})