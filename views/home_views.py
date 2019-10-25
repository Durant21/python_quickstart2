import flask

from infrastructure import cookie_auth
from infrastructure.view_modifiers import response
import services.package_service as package_service
# import services.user_service as user_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    return {
        'releases': package_service.get_latest_packages(),
        'package_count': package_service.get_latest_packages(),
        'release_count': package_service.get_latest_packages(),
        'user_count': 11,
        'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
    }


@blueprint.route('/home/about')
@response(template_file='home/about.html')
def about():
    return {}
