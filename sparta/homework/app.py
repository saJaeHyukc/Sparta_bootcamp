from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
#client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    addr_receive = request.form['addr_give']
    number_receive = request.form['number_give']
    hour_receive = request.form['hour_give']

    doc = {
        'name':name_receive,
        'addr':addr_receive,
        'number':number_receive,
        'hour':hour_receive
    }
    
    db.dbhomework.insert_one(doc)

    return jsonify({'msg': '신청이 완료되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    user_info = list(db.dbhomework.find({}, {'_id': False}))
    return jsonify({'all_user_info': user_info})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)