from flask import Flask, render_template

from cmath import sin

out=[]
app = Flask(__name__)
@app.route('/numericalintegralservice/<float:x>/<float:y>')
def cal_integral_calc(x=None,y=None):
    N = [1,10,100,1000,10000,100000,1000000]
    out=[]
    for j in range(len(N)):
        i = 0
        di = 0.0
        while i<N[j]:
            parts = ((y-x)/N[j])*i 
            length = (y-x)/N[j]
            breadth = abs(sin(parts))
            di += length*breadth
            i+=1
        out.append(di)
    return str(out)


if __name__ == "__main__":
    app.run(debug=True)