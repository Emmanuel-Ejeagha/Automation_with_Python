from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
def home():
  print("Get request string")
  return render_template('index.html')

@app.route('/', methods = ['POST'])
def home_post():
  print(request.form)
  num1 = request.form['1st']
  num2 = request.form['2nd']
  num3 = request.form['3rd']
  result = float(num1) * float(num2) * float(num3)
  print("Get post request")
  return render_template('index.html', output=result, num1=num1, num2=num2, num3=num3)

app.run(debug=True)