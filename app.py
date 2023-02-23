import openai
from flask import Flask, request

app = Flask(__name__)

@app.route('/ask', methods = ["POST"])
def hello_world():  # put application's code here
    prompt=request.get_json()['key']
    openai.api_key = "yourkey"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=2033,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )
    return response.choices[0].text


if __name__ == '__main__':
    app.run()
