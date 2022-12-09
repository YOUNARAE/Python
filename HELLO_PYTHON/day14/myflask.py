from flask import Flask, json
from flask.globals import request
from flask import Flask, render_template
from flask.json import jsonify
from day14.dao_teacher import DaoTeacher

app = Flask(__name__)

@app.route('/')
@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/ajax_teacher_list', methods=['POST'])
def ajax_teacher_list():
    dt = DaoTeacher()
    list = dt.selects()
    print(list)
    return jsonify(list = list)

@app.route('/ajax_teacher_one', methods=['POST'])
def ajax_teacher_one():
    dict = request.get_json()
    print(dict)
    t_id = dict['t_id'] 
    dt = DaoTeacher()
    teacher = dt.select(t_id)
    return jsonify(teacher = teacher)

@app.route('/ajax_teacher_add', methods=['POST'])
def ajax_teacher_add():
    dict   = request.get_json()
    t_name = dict['t_name']
    mobile = dict['mobile']
    addr   = dict['addr']
    
    dt = DaoTeacher()
    cnt = dt.insert(t_name,mobile,addr)
    return jsonify(cnt = cnt)

@app.route('/ajax_teacher_edit', methods=['POST'])
def ajax_teacher_edit():
    dict   = request.get_json()
    t_id   = dict['t_id']
    t_name = dict['t_name']
    mobile = dict['mobile']
    addr   = dict['addr']
    
    dt = DaoTeacher()
    cnt = dt.update(t_id,t_name,mobile,addr)
    return jsonify(cnt = cnt)

@app.route('/ajax_teacher_del', methods=['POST'])
def ajax_teacher_del():
    dict = request.get_json()
    t_id = dict['t_id']
    dt = DaoTeacher()
    cnt = dt.delete(t_id)
    return jsonify(cnt = cnt)

if __name__ == '__main__':
    app.run(debug=True)