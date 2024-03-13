from flask import Flask, render_template

app=Flask(__name__)
project =[
{'id':1,
'project':'web scraping','skill':'urllib python ,python requests,selenium'},
  {'id':2,
  'project':'AI model for flare mointoring','skill':'python padas,sikitlib matblotlib, microsoft azure, pychapgpt'},
  {}
]

@app.route('/')#الصفحه الرئيسية 
def hello_world():
  return render_template("home.html",myskills=project,
                        myname = 'Reem')
#first class applecktion 

if __name__=='__main__':
   app.run(host="0.0.0.0",port=True)#run flask server 
  