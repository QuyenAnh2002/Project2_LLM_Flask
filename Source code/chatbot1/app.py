from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import requests




app = Flask(__name__)

@app.route("/gpt-3.5")
def index_gpt():
    return render_template('chatgpt-3.5.html')

@app.route("/postgpt-3.5", methods=["GET", "POST"])
def chat_gpt():
    msg = request.form["msg"]
    input = msg
    return handel_response_flowise(input)


@app.route("/huggingface")
def index_huggingface():
    return render_template('huggingface.html')

@app.route("/posthuggingface", methods=["GET", "POST"])
def chat_huggingface():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)





#model lấy trên hugging face sử dụng thông qua flowise




# model gpt 3.5 sử dụng thông qua flowise
API_URL = "http://localhost:3000/api/v1/prediction/6b9c5975-99e8-46ba-95d7-329ce0a2d500"
def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
def handel_response_flowise(text: str) -> str:
    output = query({
    "question": text,
    })
    return output


# model đ nào lấy trên mạng mà nó trả lời như buồi ấy 
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
def get_Chat_response(text):
    for step in range(5):       
        new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids    
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)







if __name__ == '__main__':
    app.run()
