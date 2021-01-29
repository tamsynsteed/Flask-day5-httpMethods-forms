from flask import Flask, render_template, url_for, redirect, request

app=Flask(__name__)
@app.route('/')
def hello():
    type_of_request=request.method
    return render_template("Hello.html", request_method=type_of_request)






if __name__=='__main__':
    app.run(debug=True)
