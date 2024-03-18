from flask import Flask, render_template
from database import load_projects_from_db
app=Flask(__name__)


@app.route('/')#الصفحه الرئيسية 
def hello_world():
  projects=load_projects_from_db()
  return render_template("home.html",myskills=projects,
                        myname = 'Reem')
#first class applecktion 

if __name__=='__main__':
   app.run(host="0.0.0.0",port=True)#run flask server 
  