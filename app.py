from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Gokul!</p>"

@app.route("/y")
def hello_world2():
    my_world= "gokul"
    message="gokul is sweet"
    friends=['g1','g2','g3',"g4","g5"]
    
    return render_template("xy.html",tingtong=my_world,msg=message,friends=friends,data=[1,2,3,4])

@app.route("/abc")
def hello_world1():
    return "<p>Hello, World1!</p>"

@app.route("/hello/<name>")
def hello_world3(name):
    return f"<p>Hello,{name}!</p>"

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method=='POST':
        name = request.form.get('blah')
        print("hello,", name) 
        return name  
    return redirect("/y")

if __name__ == '__main__':
    app.run(debug=True)
