from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin-db:P@$t@db1@mysql:3306/test_db'
db = SQLAlchemy(app)

class UserAge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)

@app.route('/submit', methods=['POST'])
def submit_age():
    age = request.form['age']
    user_age = UserAge(age=age)
    db.session.add(user_age)
    db.session.commit()
    return "Age submitted successfully!"

@app.route('/average_age', methods=['GET'])
def average_age():
    ages = UserAge.query.all()
    avg_age = sum([user.age for user in ages]) / len(ages) if ages else 0
    return jsonify(average_age=avg_age)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
