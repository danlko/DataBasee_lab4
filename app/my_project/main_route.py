from flask import Blueprint, jsonify, request
from sqlalchemy import text
from app.my_project import db

# --- ОСЬ ТУТ БУЛА ПОМИЛКА ---
# Ми називаємо змінну main_bp, щоб ваш main.py міг її знайти
main_bp = Blueprint('main_bp', __name__)


# url_prefix тут можна не ставити, бо ви вже задали його в register_blueprint

# 1. Вставка супермаркету через процедуру
@main_bp.route('/insert-supermarket', methods=['POST'])
def insert_supermarket():
    data = request.json
    try:
        sql = text("CALL insert_supermarket_proc(:name, :address, :area, :net_id)")
        db.session.execute(sql, {
            'name': data.get('name'),
            'address': data.get('address'),
            'area': data.get('area'),
            'net_id': data.get('network_id')
        })
        db.session.commit()
        return jsonify({"message": "Supermarket inserted via procedure"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# 2. М:М зв'язок (Панель + Відео) через процедуру
@main_bp.route('/link-mm', methods=['POST'])
def link_mm():
    data = request.json
    try:
        sql = text("CALL link_panel_video_by_names(:sn, :title)")
        db.session.execute(sql, {
            'sn': data.get('serial_number'),
            'title': data.get('video_title')
        })
        db.session.commit()
        return jsonify({"message": "M:M link created via procedure"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# 3. Пакетна вставка (10 брендів)
@main_bp.route('/insert-package', methods=['POST'])
def insert_package():
    try:
        db.session.execute(text("CALL insert_ten_brands_package()"))
        db.session.commit()
        return jsonify({"message": "10 brands inserted successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# 4. Функція через процедуру (Середнє)
@main_bp.route('/avg-visitors/<int:network_id>', methods=['GET'])
def get_avg_visitors(network_id):
    try:
        result = db.session.execute(
            text("CALL select_avg_visitors_proc(:nid)"),
            {'nid': network_id}
        ).fetchone()

        avg_val = result[0] if result else 0

        return jsonify({"network_id": network_id, "average_visitors": avg_val}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# 5. Динамічні таблиці (Курсор)
@main_bp.route('/cursor-distribute', methods=['POST'])
def cursor_distribute():
    try:
        result = db.session.execute(text("CALL distribute_supermarkets_cursor()")).fetchone()
        db.session.commit()
        return jsonify({"message": "Cursor executed", "details": result[0] if result else "Done"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400