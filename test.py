#!/usr/bin/env python
from flask import Flask, jsonify, request
app = Flask(__name__)

import psycopg2

conn = psycopg2.connect(database = "postgres", user = "postgres", password = "namespace1", hostaddr="35.198.246.100", port = "5432")
print ('Opened database successfully')
cur = conn.cursor()

cur.execute("SELECT * from OPENWEATHER")
rows = cur.fetchall()

openweatherdata=[]
worldweatherdata=[]
metgisdata=[]
for row in rows:
    temp = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    for i in range(0,24):
        temp[i] = row[i].replace(" ","")
    a=temp[0]
    b=temp[1]
    c=temp[2]
    d=temp[3]
    e=temp[4]
    f=temp[5]
    g=temp[6]
    h=temp[7]
    i=temp[8]
    j=temp[9]
    k=temp[10]
    l=temp[11]
    m=temp[12]
    n=temp[13]
    o=temp[14]
    p=temp[15]
    q=temp[16]
    r=temp[17]
    s=temp[18]
    t=temp[19]
    u=temp[20]
    v=temp[21]
    w=temp[22]
    x=temp[23]
    openweatherdata += [{'lat':a,'lon':b,'id1':c,'main':d,'description':e,'icon':f,'temp':g,'pressure':h,'humidity':i,'temp_min':j,'temp_max':k,'visibility':l,'speed':m,'deg':n,'clouds':o,'dt':p,'typ':q,'id2':r,'message':s,'country':t,'sunrise':u,'sunset':v,'idn':w,'name':x}]

cur.execute("SELECT * from METGIS")
rows = cur.fetchall()
for row in rows:
    temp = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    for i in range(0,25):
        temp[i] = row[i].replace(" ","")
    a=temp[0]
    b=temp[1]
    c=temp[2]
    d=temp[3]
    e=temp[4]
    f=temp[5]
    g=temp[6]
    h=temp[7]
    i=temp[8]
    j=temp[9]
    k=temp[10]
    l=temp[11]
    m=temp[12]
    n=temp[13]
    o=temp[14]
    p=temp[15]
    q=temp[16]
    r=temp[17]
    s=temp[18]
    t=temp[19]
    u=temp[20]
    v=temp[21]
    w=temp[22]
    x=temp[23]
    y=temp[24]
    metgisdata += [{'lat':a,'lon':b,'alt':c,'sunrise':d,'daycount':e,'weathericon':f,'snowfall':g,'unitlin':h,'maxtemp':i,'description':j,'daterequest':k,'winddir':l,'sunshineduration':m,'precipitaton':n,'windicon':o,'windspeed':p,'lang':q,'rainfall':r,'unitwind':s,'forecastissued':t,'mintemp':u,'unittemp':v,'sunset':w,'relativehumidity':x,'forecastshorttext':y,}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works'})

@app.route('/openweather', methods=['GET'])
def ow():
    return jsonify({'openweather': openweatherdata})

@app.route('/worldWeather', methods=['GET'])
def ww():
    return jsonify({'worldweather': worldweatherdata})

@app.route('/metgis', methods=['GET'])
def metgis():
    return jsonify({'metgis': metgisdata})




if __name__ == '__main__':
    app.run(debug=True)
