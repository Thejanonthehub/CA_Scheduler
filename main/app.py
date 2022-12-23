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
        c1=request.form['ca1']
        c2=request.form['ca2']
        c3=request.form['ca3']
        c4=request.form['ca4']
        c5=request.form['ca5']
        all=request.form['allca']
        l_n.append(name)
        print(name,"\n",n_ca,"\n",due_d,"\n",due,"\n",c1,"\n",c2,"\n",c3,"\n",c4,"\n",c5,"\n",all)
        print(l_n)
        return render_template('pass.html', n=name, n_ca=n_ca, due_d=due_d, due=due, ca1=c1, ca2=c2, ca3=c3, ca4=c4, ca5=c5, all=all)

    if __name__ =='__main__':
        app.run(debug=True)
    return()
t1()