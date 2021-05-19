import os
import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import pymysql
from backend.MyEncoder import MyEncoder

app = Flask(__name__)
# app.config返回类字典对象，里面用来存放
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# uri统一资源匹配符
# SQLALCHEMY_DATABASE_URI配置数据库连接的参数
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@10.181.235.25:3306/test'

# 请求结束后自动提交数据库修改
app.config['SQLALCHEMY_COMMMIT_ON_TEARDOWN'] = True
# 如果设置成 True (默认情况)，Flask-SQLAlchemy	将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

models = SQLAlchemy(app)  # 关联sqlalchemy和flask


class sites_list(models.Model):
    __tablename__ = 'sites_list'
    id = models.Column(models.String(255), primary_key=True)
    name = models.Column(models.String(255))
    city = models.Column(models.String(255))
    latitude = models.Column(models.String(255))
    longitude = models.Column(models.String(255))


@app.route('/getSiteList', methods=['GET'])
def function():
    city = request.args.get('city')
    sites = models.session.query(sites_list).filter(sites_list.city == city ).all()
    # sites = models.session.query(sites_list).filter(sites_list.city == '北京').all()
    all_sites = []
    for site in sites:
        all_sites.append(site.id)
    sites_dict = {"sites_list": all_sites}
    print(sites_dict)
    return json.dumps(sites_dict, cls=MyEncoder, indent=4)
    # print(sites_dict)


if __name__ == '__main__':
    app.run(debug=True)

'''
@route('/getSiteList', methods=['GET'])
def function():
    topics = models.session.query(sites_list).all()
    tp_list = []
    # print(type(topics))
    for topic in topics:
        tp_list.append({"id": topic.id, "text": topic.text})

    # print(type(tp_list))
    # print(tp_list)
    return json.dumps(tp_list)
'''
