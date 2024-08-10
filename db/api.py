from flask import Flask, jsonify, request
from db_manager import init_db, query_cf_data

app = Flask(__name__)
db_path = 'db/calibration_files.db'

@app.route('/query', methods=['GET'])
def query():
    key = request.args.get('key')
    conn = init_db(db_path)
    results = query_cf_data(conn, key)
    conn.close()
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
