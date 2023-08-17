from flask import Flask, request, render_template
import requests
app=Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    weatherd=''
    error=0
    cityname=''
    if request.method=="POST":
        cityname=request.form.get("cityname")
        if cityname:
            weatherapi='cc6c0ea1b8f57bc15fbe3d346c1fbf67'
            url="https://api.openweathermap.org/data/2.5/weather?q="+cityname+"&appid="+ weatherapi
            weatherd=requests.get(url).json()
        else:
            error=1;
    return render_template('index.html', data=weatherd, cityname=cityname, error=error)
if__name__=='__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)

    

