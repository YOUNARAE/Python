from flask import Flask, json
from flask.globals import request
from flask import Flask, render_template
from flask.json import jsonify
from day13.dao_student import DaoStudent

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    #data = request.get_json()
    dm = DaoStudent()
    list = dm.selects()
    print(list)
    return jsonify(list = list)

@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    dict = request.get_json()
    print(dict['s_id'])
    dm = DaoStudent()
    stu = dm.select(dict['s_id'])
    print(stu)
    return jsonify(stu = stu)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    dict = request.get_json()
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    address = dict['address']
    dm = DaoStudent()
    cnt = dm.insert(s_id,s_name,mobile,address)
    return jsonify(cnt = cnt)

@app.route('/ajax_edit', methods=['POST'])
def ajax_edit():
    dict = request.get_json()
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    address = dict['address']
    dm = DaoStudent()
    cnt = dm.update(s_id,s_name,mobile,address)
    return jsonify(cnt = cnt)

@app.route('/ajax_del', methods=['POST'])
def ajax_del():
    dict = request.get_json()
    s_id = dict['s_id']
    dm = DaoStudent()
    cnt = dm.delete(s_id)
    return jsonify(cnt = cnt)


if __name__ == '__main__':
    app.run(debug=True)