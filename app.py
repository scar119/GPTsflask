from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ... 其余代码 ...


# 模拟数据库数据
# links = [
#     {"python大师": "链接1", "url": "https://chat.openai.com/g/g-UAR3CJ1uo-42master-pythontutor/c/b9c8a2fe-aa5a-427f-a76e-2dd44e8ceefc", "description": "代码python大师"},
#     # {"数据分析": "链接2", "url": "http://example2.com", "description": "链接2的简介"}
#     # 更多链接...
# ]

links = [
    {
        "name": "python大师",
        "url": "https://chat.openai.com/g/g-UAR3CJ1uo-42master-pythontutor",
        "description": "Python初学者到高级工程师的学习导师",
        "category": "编程",
        "logo": "/static/python.png"
     },
    {
        "name": "Strategic Insight AI战略洞察",
        "url": "https://chat.openai.com/g/g-9X1D8otzy-strategic-insight-ai",
        "description": "精通数据的人工智能业务顾问，具有收入预测技能。",
        "category": "数据分析",
        "logo": "/static/data.png"
    },
    {
        "name": "哲学大师",
        "url": "https://chat.openai.com/g/g-UAR3CJ1uo-42master-pythontutor/c/b9c8a2fe-aa5a-427f-a76e-2dd44e8ceefc",
        "description": "当我们在讨论哲学时",
        "category": "编程",
        "logo": "/static/logo.png"
    },
    {
        "name": "哲学大师",
        "url": "https://chat.openai.com/g/g-UAR3CJ1uo-42master-pythontutor/c/b9c8a2fe-aa5a-427f-a76e-2dd44e8ceefc",
        "description": "当我们在讨论哲学时",
        "category": "编程",
        "logo": "/static/logo.png"
    },
    {
        "name": "大师",
        "url": "https://chat.openai.com/g/g-UAR3CJ1uo-42master-pythontutor/c/b9c8a2fe-aa5a-427f-a76e-2dd44e8ceefc",
        "description": "当我们在讨论哲学时",
        "category": "编程",
        "logo": "/static/logo.png"
    },
    {
        "name": "哲学大师",
        "url": "https://chat.openai.com/g/g-UAR3CJ1uo-42master-pythontutor/c/b9c8a2fe-aa5a-427f-a76e-2dd44e8ceefc",
        "description": "当我们在讨论哲学时",
        "category": "编程",
        "logo": "/static/logo.png"
    }


    # 您可以继续添加更多的链接
]


@app.route('/links')
def get_links():
    return jsonify(links)

if __name__ == '__main__':
    app.run(debug=True)
