from flask import Flask

app=Flask(__name__)


@app.route('/')#الصفحه الرئيسية 
def hello_world():
  return 'Hello, Reem!'
#first class applecktion 

if __name__=='__main__':
   app.run(host="0.0.0.0",port=True)#run flask server 
  