from flask import *

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'

@app.route('/')
def main():
    return render_template('main.html') 


@app.route('/predict' ,methods=['GET','POST'])
def prd():
    return render_template('predict_home.html')


@app.route('/prediction' ,methods=['GET','POST'])
def prdct():
    if request.method == 'POST':  

        size = request.form['size']  
        year = request.form['year']  
        roof = request.form['roof']
        ROOF = roof
        pool = request.form['pool']
        POOL = pool
        labi = request.form['labi']
        LABI = labi
        parcking = request.form['parcking']
        PARCKING = parcking

        roof = 1 if roof == 'دارد' else 0
        pool = 1 if pool == 'دارد' else 0
        labi = 1 if labi == 'دارد' else 0
        if parcking == 'دارد':
            parcking = 0
        elif parcking == 'ندارد':
            parcking = 2
        else:
            parcking = 1

        size = int(size)
        year = int(year)
        roof = int(roof)
        pool = int(pool)
        labi = int(labi)
        parcking = int(parcking)

        if size <= 49 or year <= 1349:
            return redirect(url_for('wrn'))
        
        import joblib
        Model = joblib.load(r'C:\Users\Mahdi_1001\Desktop\Flask_Test/model.pkl','r+') 
        Predict = Model.predict([[size,year,roof,pool,labi,parcking]])[0]

        Predict = int(Predict)
        Predict = str(Predict)[::-1]
        Counter,Edit_Predict = 0 ,''
        for i in Predict:
            Counter +=1
            Edit_Predict +=i
            if (Counter == 3 and len(Predict) > 3) or (len(Predict) > 6 and Counter == 6) or ((len(Predict) >= 10 and  Counter == 9)): 
                Edit_Predict +=','

        x1,x2 = '',''
        if len(Edit_Predict) > 11 :
            x1 = Edit_Predict[::-1]
        else:
            x2 = Edit_Predict[::-1]

        return render_template('predict_home.html' ,size = size ,
                                                    year=year ,
                                                    roof=roof ,ROOF=ROOF,
                                                    pool = pool ,POOL = POOL,
                                                    labi = labi ,LABI = LABI,
                                                    parcking = parcking,PARCKING = PARCKING,
                                                    x1 = x1,
                                                    x2 = x2
                                                    )


@app.route('/warnning' ,methods=['GET','POST'])
def wrn():
    w = '!!مقادیر را در محدوده صحیح وارد کنید '
    return render_template('predict_home.html',w = w)

if __name__ == '__main__':
    app.run(debug=True ,port=5000)