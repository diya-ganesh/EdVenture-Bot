from flask import Flask, render_template, request
import openai

openai.api_key = "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"
app = Flask(__name__)
def get_completion(prompt, character, model="gpt-3.5-turbo"):
    
    messages = [{"role": "user", "content": f'''Remember you are {character} and
                         I am an elementary school student, and I need you to answer this question 
                         *briefly*: {prompt} Include references to your life and remember 
                         I have no previous knowledge in this topic. If you are asked a math question, 
                         be very careful about arithmetic, and don’t give final answers but rather 
                         walk me through the steps and explain the concepts. 
                         Remember to answer like you are {character} and your goal is to teach me!'''}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model’s output
    )
    return response.choices[0].message["content"]
@app.route("/chatbot")
def chatbot():
    print(request.args.get("character")) 
    return render_template("index.html")
@app.route("/")
def home():
    return render_template("home-page.html")
@app.route("/get", methods=["GET", "POST"])
def get_bot_response():
    print(request.args.get("character"))
    userText = request.args.get("msg")
    userCharacter = request.args.get("character")
    response = str(get_completion(userText, userCharacter))
    return response
    
if __name__ == "__main__":
    app.run()