from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')#الصفحه الرئيسية 
def hello_world():
  return render_template("home.html")
#first class applecktion 

if __name__=='__main__':
   app.run(host="0.0.0.0",port=True)#run flask server 
  