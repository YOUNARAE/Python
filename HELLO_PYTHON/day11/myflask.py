from flask import Flask, json
from flask.globals import request
from flask import Flask, render_template
from day11.dao_mem import DaoMem

app = Flask(__name__)

@app.route('/mem_list')
def mem_list():
    dm = DaoMem()
    list = dm.selects()
    return render_template('mem_list.html',list=list)

@app.route('/mem_detail')
def mem_detail():
    dm = DaoMem()
    m_id = request.args.get('m_id')
    mem = dm.select(m_id)
    return render_template('mem_detail.html',mem=mem)

@app.route('/mem_edit')
def emp_edit():
    dm = DaoMem()
    m_id = request.args.get('m_id')
    mem = dm.select(m_id)
    return render_template('mem_edit.html',mem=mem)

@app.route('/mem_edit_act',methods=['POST'])
def mem_edit_act():
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    dm = DaoMem()
    cnt = dm.update(m_id, m_nm, tel, ymd)
    return render_template('mem_edit_act.html', cnt=cnt)

@app.route('/mem_add')
def mem_add():
    return render_template('mem_add.html')

@app.route('/mem_add_act',methods=['POST'])
def mem_add_act():
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    dm = DaoMem()
    cnt = dm.insert(m_id, m_nm, tel, ymd)
    return render_template('mem_add_act.html', cnt=cnt)

@app.route('/mem_del_act',methods=['POST'])
def mem_delete():
    m_id = request.form['m_id']
    dm = DaoMem()
    cnt = dm.delete(m_id)
    return render_template('mem_del_act.html', cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)