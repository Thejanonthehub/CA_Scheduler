#This file for visualising index.html file as a form and passing given output from that form(index.html) to back-end python code.
from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalues():
    #passing front-end output data to variables
    name=request.form['name']
    n_ca=request.form['n_ca'] 
    due_d=request.form['due_date']
    due=request.form['due']
    print(name,"\n",n_ca,"\n",due_d,"\n",due)
    return render_template('pass.html', n=name, n_ca=n_ca, due_d=due_d, due=due)

if __name__ =='__main__':
    app.run(debug=True)
