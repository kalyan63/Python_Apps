from flask import Flask,render_template,jsonify

app=Flask(__name__)

@app.route('/')
def index():
    return "Nothing on this page"

@app.route('/<int:a>',methods=['GET'])
def main(a):
    # return render_template('index.html')
    return jsonify({"square":a**2})

if __name__=="__main__":
    app.run(debug=True)