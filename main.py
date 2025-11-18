import yaml
from flask import Flask

from app.my_project import db

from app.my_project.supermarket.route.retail_network_route import retail_network_bp
from app.my_project.supermarket.route.supermarket_route import supermarket_bp
from app.my_project.supermarket.route.department_route import department_bp

from app.my_project.video.route.brand_route import brand_bp
from app.my_project.video.route.video_producer_route import video_producer_bp
from app.my_project.video.route.video_route import video_bp

from app.my_project.panel.route.panel_manufacturer_route import panel_manufacturer_bp
from app.my_project.panel.route.panel_spec_route import panel_spec_bp
from app.my_project.panel.route.panel_route import panel_bp


def create_app():
    app = Flask(__name__)

    try:
        with open('app/config/app.yml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            db_config = config['database']
    except FileNotFoundError:
        print("ПОМИЛКА: Файл app/config/app.yml не знайдено.")
        exit(1)
    except KeyError:
        print("ПОМИЛКА: Неправильна структура app/config/app.yml. "
              "Переконайтеся, що 'database' ключ існує.")
        exit(1)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{db_config['user']}:{db_config['password']}@"
        f"{db_config['host']}:{db_config['port']}/{db_config['database_name']}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    api_prefix = '/api'

    app.register_blueprint(retail_network_bp, url_prefix=f'{api_prefix}/networks')
    app.register_blueprint(supermarket_bp, url_prefix=f'{api_prefix}/supermarkets')
    app.register_blueprint(department_bp, url_prefix=f'{api_prefix}/departments')

    app.register_blueprint(brand_bp, url_prefix=f'{api_prefix}/brands')
    app.register_blueprint(video_producer_bp, url_prefix=f'{api_prefix}/video-producers')
    app.register_blueprint(video_bp, url_prefix=f'{api_prefix}/videos')

    app.register_blueprint(panel_manufacturer_bp, url_prefix=f'{api_prefix}/panel-manufacturers')
    app.register_blueprint(panel_spec_bp, url_prefix=f'{api_prefix}/panel-specs')
    app.register_blueprint(panel_bp, url_prefix=f'{api_prefix}/panels')

    print("Додаток успішно створено та підключено до БД.")
    print("Доступні роути:")
    for rule in app.url_map.iter_rules():
        print(f"- {rule.endpoint} -> {rule.rule}")

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)