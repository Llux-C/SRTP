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

#class definition
#list of all sites
class sites_list(models.Model):
    __tablename__ = 'sites_list'
    id = models.Column(models.String(255), primary_key=True)
    name = models.Column(models.String(255))
    city = models.Column(models.String(255))
    latitude = models.Column(models.String(255))
    longitude = models.Column(models.String(255))

#missing rate of all sites from week1 to week53
class missing_rate(models.Model):
    __tablename__ = 'missing_rate'
    week = models.Column(models.String(255),primary_key=True)
    AQI = models.Column(models.String(255))
    PM25 = models.Column(models.String(255))
    PM25_24h = models.Column(models.String(255))
    PM10 = models.Column(models.String(255))
    PM10_24h = models.Column(models.String(255))
    SO2 = models.Column(models.String(255))
    SO2_24h = models.Column(models.String(255))
    NO2 = models.Column(models.String(255))
    NO2_24h = models.Column(models.String(255))
    O3 = models.Column(models.String(255))
    O3_24h = models.Column(models.String(255))
    O3_8h = models.Column(models.String(255))
    O3_8h_24h = models.Column(models.String(255))
    CO = models.Column(models.String(255))
    CO_24h = models.Column(models.String(255))
    id = models.Column(models.String(255))

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

@app.route('/getMissing', methods=['GET'])
def function():
    site_id = request.args.get('site_id')
    missing = models.session.query(missing_rate).filter(missing_rate.id == site_id).all()

    #data process
    missing_value_AQI = []
    for week in missing:
        missing_value_AQI.append(week.AQI)

    missing_value_PM25 = []
    for week in missing:
        missing_value_PM25.append(week.PM25)

    missing_value_PM25_24h = []
    for week in missing:
        missing_value_PM25_24h.append(week.PM25_24h)

    missing_value_PM10 = []
    for week in missing:
        missing_value_PM10.append(week.PM10)

    missing_value_PM10_24h = []
    for week in missing:
        missing_value_PM10_24h.append(week.PM10_24h)

    missing_value_SO2 = []
    for week in missing:
        missing_value_SO2.append(week.SO2)

    missing_value_SO2_24h = []
    for week in missing:
        missing_value_SO2_24h.append(week.SO2_24h)

    missing_value_NO2 = []
    for week in missing:
        missing_value_NO2.append(week.NO2)

    missing_value_NO2_24h = []
    for week in missing:
        missing_value_NO2_24h.append(week.NO2_24h)

    missing_value_O3 = []
    for week in missing:
        missing_value_O3.append(week.O3)

    missing_value_O3_24h = []
    for week in missing:
        missing_value_O3_24h.append(week.O3_24h)

    missing_value_O3_8h = []
    for week in missing:
        missing_value_O3_8h.append(week.O3_8h)

    missing_value_O3_8h_24h = []
    for week in missing:
        missing_value_O3_8h_24h.append(week.O3_8h_24h)

    missing_value_CO = []
    for week in missing:
        missing_value_CO.append(week.CO)

    missing_value_CO_24h = []
    for week in missing:
        missing_value_CO_24h.append(week.CO_24h)

    missing_dict = {"AQI": missing_value_AQI,
                    "PM25": missing_value_PM25,
                    "PM25_24h": missing_value_PM25_24h,
                    "PM10": missing_value_PM10,
                    "PM10_24h": missing_value_PM10_24h,
                    "SO2": missing_value_SO2,
                    "SO2_24h": missing_value_SO2_24h,
                    "NO2": missing_value_NO2,
                    "NO2_24h": missing_value_NO2_24h,
                    "O3": missing_value_O3,
                    "O3_24h": missing_value_O3_24h,
                    "O3_8h": missing_value_O3_8h,
                    "O3_8h_24h": missing_value_O3_8h_24h,
                    "CO": missing_value_CO,
                    "CO_24h": missing_value_CO_24h}

    return json.dumps(missing_dict, cls=MyEncoder, indent=4)

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
