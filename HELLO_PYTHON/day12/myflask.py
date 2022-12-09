from flask import Flask, json
from flask.globals import request
from flask import Flask, render_template
from flask.json import jsonify
from day12.dao_emp import DaoEmp

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    #data = request.get_json()
    dm = DaoEmp()
    list = dm.selects()
    print(list)
    return jsonify(list = list)

@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    dict = request.get_json()
    print(dict['e_id'])
    dm = DaoEmp()
    emp = dm.select(dict['e_id'])
    print(emp)
    return jsonify(emp = emp)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    dict = request.get_json()
    e_id = dict['e_id']
    e_name = dict['e_name']
    sex = dict['sex']
    addr = dict['addr']
    dm = DaoEmp()
    cnt = dm.insert(e_id,e_name,sex,addr)
    return jsonify(cnt = cnt)

@app.route('/ajax_edit', methods=['POST'])
def ajax_edit():
    dict = request.get_json()
    e_id = dict['e_id']
    e_name = dict['e_name']
    sex = dict['sex']
    addr = dict['addr']
    dm = DaoEmp()
    cnt = dm.update(e_id,e_name,sex,addr)
    return jsonify(cnt = cnt)

@app.route('/ajax_del', methods=['POST'])
def ajax_del():
    dict = request.get_json()
    e_id = dict['e_id']
    dm = DaoEmp()
    cnt = dm.delete(e_id)
    return jsonify(cnt = cnt)


if __name__ == '__main__':
    app.run(debug=True)