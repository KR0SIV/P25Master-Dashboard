from flask import Blueprint, render_template
from flask_login import login_required
from modules import dockerData
from modules import dContent

blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix='/home',
    template_folder='templates',
    static_folder='static'
)



@blueprint.route('/index')
@login_required
def index():
    return render_template('index.html', uTime=dContent.upTime(), cCount=dockerData.conCount(), talkgroups=dContent.talkgroups(), tableContent=dContent.tableContent())
#https://stackoverflow.com/questions/40963401/flask-dynamic-data-update-without-reload-page


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')
