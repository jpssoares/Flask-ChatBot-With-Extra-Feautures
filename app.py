from flask import Flask, render_template, request, jsonify
import gpt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    input = request.form["msg"]

    result = gpt.get_gpt_answer(input)
    print(result)
    quick_replies = ["Hello World", "!Goodbye"]

    return {"result": result, "quick_replies": quick_replies}
    
if __name__ == '__main__':
    app.run()