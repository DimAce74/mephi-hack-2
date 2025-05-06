from flask import Flask, request, render_template
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# загружаем модель из файла
model = BertForSequenceClassification.from_pretrained("./models/bert_other", problem_type="multi_label_classification")
tokenizer = BertTokenizer.from_pretrained("./models/bert_other")

# создаём приложение
app = Flask(__name__)

def predict(text):
    # Токенизация текста
    inputs = tokenizer(
        text,
        padding=True,
        truncation=True,
        max_length=512,
        return_tensors="pt"
    )
    
    # Предсказание
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Получение метки класса
    probs = torch.sigmoid(outputs.logits)
    pred_class = torch.argmax(probs).item()

    print(outputs.logits)
    print(probs)
    print(torch.argmax(outputs.logits))
    print(torch.softmax(outputs.logits, dim=1))
    
    id2label = {
        0: 'другое',
        1: "личная жизнь",
        2: "политика", 
        3: "реклама",
        4: "соцсети",
        5: "спорт",
        6: "юмор"
    }

    res = {}
    
    for class_id, prob in enumerate(probs.cpu().numpy()[0]):
       res[id2label[class_id]] = round(prob, 4)

    return res

@app.route('/', methods=['GET', 'POST'])
def index():
    readable_result = None
    user_text = None
    if request.method == 'POST':
        user_text = request.form['user_text']
        result = predict(user_text)
    
        sorted_result = sorted(
            result.items(),
            key=lambda x: x[1],
            reverse=True
        )

        print(sorted_result)
    
        readable_result = "\n".join(
            f"{category}: {prob:.2%}" for category, prob in sorted_result
        )

        print(readable_result)

    return render_template('index.html', text = user_text, result=readable_result)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)