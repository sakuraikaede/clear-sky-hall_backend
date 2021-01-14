from flask import Flask, request
import json
import pymysql
app = Flask(__name__)
@app.route('/')

def main():
    print("New request.")
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    db = pymysql.connect(host=settings['ip'],port=settings['port'],user=settings['user'],passwd=settings['passwd'],db=settings['dbname'],charset='utf8')
    cursor = db.cursor()
    tb=settings['table']
    sql = "SELECT * FROM %s ORDER BY RAND() LIMIT 1" % tb
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        num = row[0]
        sentence = row[1]
    cursor.close()
    db.close()
    return sentence

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
