#!/usr/bin/env python
from flask import Flask, jsonify, request
app = Flask(__name__)

import psycopg2

conn = psycopg2.connect(database = "postgres", user = "postgres", password = "namespace1", hostaddr="35.198.246.100", port = "5432")
print ('Opened database successfully')
cur = conn.cursor()

openweatherdata=[]
worldweatherdata=[]
metgisdata=[]

@app.route('/openweather', methods=['GET'])
def ow():
    cur.execute("SELECT * from OPENWEATHER")
    rows = cur.fetchall()
    global openweatherdata
    openweatherdata =[]
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
    return jsonify({'openweather': openweatherdata})


@app.route('/metgis', methods=['GET'])
def metgis():
    global metgisdata
    metgisdata = []
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
    return jsonify({'metgis': metgisdata})


@app.route('/worldweather', methods=['GET'])
def ww():
    global worldweatherdata
    worldweatherdata = []
    cur.execute("SELECT * from WORLDWEATHER")
    rows = cur.fetchall()
    for row in rows:
        # 79
        temp = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        for i in range(0,79):
            temp[i] = row[i].replace(" ","")
        a = temp[0]
        b = temp[1]
        c = temp[2]
        d = temp[3]
        e = temp[4]
        f = temp[5]
        g = temp[6]
        h = temp[7]
        i = temp[8]
        j = temp[9]
        k = temp[10]
        l = temp[11]
        m = temp[12]
        n = temp[13]
        o = temp[14]
        p = temp[15]
        q = temp[16]
        r = temp[17]
        s = temp[18]
        t = temp[19]
        u = temp[20]
        v = temp[21]
        w = temp[22]
        x = temp[23]
        y = temp[24]
        z = temp[25]
        aa = temp[26]
        bb = temp[27]
        cc = temp[28]
        dd = temp[29]
        ee = temp[30]
        ff = temp[31]
        gg = temp[32]
        hh = temp[33]
        ii = temp[34]
        jj = temp[35]
        kk = temp[36]
        ll = temp[37]
        mm = temp[38]
        nn = temp[39]
        oo = temp[40]
        pp = temp[41]
        qq = temp[42]
        rr = temp[43]
        ss = temp[44]
        tt = temp[45]
        uu = temp[46]
        vv = temp[47]
        ww = temp[48]
        xx = temp[49]
        yy = temp[50]
        zz = temp[51]
        aaa = temp[52]
        bbb = temp[53]
        ccc = temp[54]
        ddd = temp[55]
        eee = temp[56]
        fff = temp[57]
        ggg = temp[58]
        hhh = temp[59]
        iii = temp[60]
        jjj = temp[61]
        kkk = temp[62]
        lll = temp[63]
        mmm = temp[64]
        nnn = temp[65]
        ooo = temp[66]
        ppp = temp[67]
        qqq = temp[68]
        rrr = temp[69]
        sss = temp[70]
        ttt = temp[71]
        uuu = temp[72]
        vvv = temp[73]
        www = temp[74]
        xxx = temp[75]
        yyy = temp[76]
        zzz = temp[77]
        aaa = temp[78]
        worldweatherdata +=[{'lat':a,'lon':b,'types':c,'querys':d,'observation_time':e,'temp_c':f,'temp_f':g,'weathercode':h,'weathericonurl':i,'weatherdesc':j,'windspeedmiles':k,'windspeedkmph':l,'winddirdegree':m,'winddir16point':n,'precipmm':o,'humidity':p,'visibility':q,'pressure':r,'cloudcover':s,'feelslikec':t,'feelslikef':u,'uvindex':v,'day_date':w,'day_sunrise':x,'day_sunset':y,'day_moonrise':z,'day_moonset':aa,'day_moon_phase':bb,'day_moon_illumination':cc,'day_maxtempc':dd,'day_maxtempf':ee,'day_mintempc':ff,'day_mintempf':gg,'day_totalsnow_cm':hh,'day_sunhour':ii,'day_uvindex':jj,'hour_times':kk,'hour_tempc':ll,'hour_tempf':mm,'hour_windspeedmile':nn,'hour_windspeedkmph':oo,'hour_winddirdegree':pp,'hour_weathercode':qq,'hour_winddir16point':rr,'hour_weathericonurl':ss,'hour_weatherdesc':tt,'hour_precipmm':uu,'hour_humidity':vv,'hour_visibility':ww,'hour_pressure':xx,'hour_cloudcover':yy,'hour_heatindexc':zz,'hour_heatindexf':aaa,'hour_dewpointc':bbb,'hour_dewpointf':ccc,'hour_windchillc':ddd,'hour_windchillf':eee,'hour_windgustmiles':fff,'hour_windgustkmph':ggg,'hour_feelslikec':hhh,'hour_feelslikef':iii,'hour_chanceofrain':jjj,'hour_chanceofremdry':kkk,'hour_chanceofwindy':lll,'hour_chanceofovercast':mmm,'hour_chanceofsunshine':nnn,'hour_chanceoffros':ooo,'hour_chanceofhightemp':ppp,'hour_chanceoffog':qqq,'hour_chanceofsnow':rrr,'hour_chanceofthunder':sss,'hour_uvindex':ttt,'month_index':uuu,'month_name':vvv,'month_avgmintemp':www,'month_avgmintemp_f':xxx,'month_absmaxtemp':yyy,'month_absmaxtemp_f':zzz,'month_avgdailyrainfall':aaa}]
    return jsonify({'worldweather': worldweatherdata})


@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works'})


if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="33")