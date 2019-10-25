import flask

from infrastructure import cookie_auth
from infrastructure.view_modifiers import response
import services.package_service as package_service
from viewmodels.account.index_viewmodel import IndexViewModel

blueprint = flask.Blueprint('gis', __name__, template_folder='templates')


@blueprint.route('/gis')
@response(template_file='/GIS/map.html')
def index():
    vm = IndexViewModel()
    if not vm.user:
        return flask.redirect('/account/login')

    test_packages = package_service.get_latest_packages()
    return {'gis': test_packages,
        'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),}
    # return flask.render_template('home/index.html', packages=test_packages)


# @blueprint.route('/documents')
# @response(template_file='documents/about.html')
# def about():
#     return {}
