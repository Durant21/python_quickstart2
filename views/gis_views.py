import flask

from infrastructure.view_modifiers import response
import services.package_service as package_service

blueprint = flask.Blueprint('gis', __name__, template_folder='templates')


@blueprint.route('/gis')
@response(template_file='/GIS/map.html')
def index():
    test_packages = package_service.get_latest_packages()
    return {'gis': test_packages}
    # return flask.render_template('home/index.html', packages=test_packages)


# @blueprint.route('/documents')
# @response(template_file='documents/about.html')
# def about():
#     return {}
