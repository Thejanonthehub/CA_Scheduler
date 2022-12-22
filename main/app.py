def t1():
    l_n=[]
    l_due=[]
    l_st=[]
    from flask import Flask, render_template, request
    app=Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/', methods=['POST'])
    def getvalues():
        name=request.form['name']
        n_ca=request.form['n_ca'] 
        due_d=request.form['due_date']
        due=request.form['due']
        l_n.append(name)
        print(name,"\n",n_ca,"\n",due_d,"\n",due)
        print(l_n)
        return render_template('pass.html', n=name, n_ca=n_ca, due_d=due_d, due=due)

    if __name__ =='__main__':
        app.run(debug=True)
    return()
t1()