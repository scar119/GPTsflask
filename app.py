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
        "category_weight":10,  # 分组权重
        "logo": "/static/python.png",
        "weight":76
     },
    {
        "name": "Strategic Insight AI战略洞察",
        "url": "https://chat.openai.com/g/g-9X1D8otzy-strategic-insight-ai",
        "description": "精通数据的人工智能业务顾问，具有收入预测技能。",
        "category": "数据分析",
        "category_weight":10,
        "logo": "/static/data.png",
        "weight":21
    },
    {
        "name": "哲学大师",
        "url": "https://chat.openai.com/g/g-rRzyV648Z-zhe-xue-jia",
        "description": "精通哲学的教师专家，指导哲学知识和批判性思维。",
        "category": "人文",
        "category_weight":200,
        "logo": "/static/zhexue.png",
        "weight":32
    },
    {
        "name": "博客写作",
        "url": "https://chat.openai.com/g/g-enlZNdcmd-bo-ke-zhuan-xie-zhuan-jia",
        "description": "撰写引人入胜且经过充分研究的博客文章的创意助手。",
        "category": "写作",
        "category_weight": 10009999,
        "logo": "/static/boke.png",
        "weight":300
    },
    {
        "name": "家庭大夫",
        "url": "https://chat.openai.com/g/g-Xkworw3jp-jia-ting-da-fu",
        "description": "提供一般健康资讯及生活小贴士，同时提醒线下咨询专业人士。",
        "category": "艺术与生活",
        "category_weight":10,
        "logo": "/static/dafu.png",
        "weight":19
    },
    {
        "name": "赚钱顾问",
        "url": "https://chat.openai.com/g/g-ks5jWgmkN-profit-pioneer",
        "description": "创业型人工智能，通过具体的、可操作的想法将资本转化为利润。",
        "category": "赚钱",
        "category_weight":100,
        "logo": "/static/money.png",
        "weight":11
    },
    {
        "name": "旅程伴侣Journey Companion",
        "url": "https://chat.openai.com/g/g-URDNLWl3W-journey-companion",
        "description": "专门针对中国目的地的专家旅游指南。",
        "category": "艺术与生活",
        "category_weight":10,
        "logo": "/static/lvcheng.png",
        "weight":10
    },
    {
        "name": "心理学专家",
        "url": "https://chat.openai.com/g/g-Bpp6vOR8k-xin-li-zhuan-jia",
        "description": "善解人意的聊天机器人为个人挑战提供指导和支持。",
        "category": "心理",
        "category_weight": 10,
        "logo": "/static/xinli.png",
        "weight":400
    },
    {
        "name": "职业指南",
        "url": "https://chat.openai.com/g/g-ULiN6PJtJ-career-guide",
        "description": "职业顾问助理，提供有关职业道路和求职策略的指导。",
        "category": "职业",
        "category_weight":10,
        "logo": "/static/zhiye.png",
        "weight":6
    },
    {
        "name": "生活教练",
        "url": "https://chat.openai.com/g/g-YpxL3kZ9S-sheng-huo-jiao-lian",
        "description": "一位富有同情心的生活教练，为平衡和成功提供指导。",
        "category": "艺术与生活",
        "category_weight":10,
        "logo": "/static/shenghuo.png",
        "weight":300
    },
    {
        "name": "音乐专家",
        "url": "https://chat.openai.com/g/g-nprHoSdAO-yin-le-zhuan-jia",
        "description": "一个音乐专家聊天机器人，提供建议和有趣的事情",
        "category": "艺术与生活",
        "category_weight":10,
        "logo": "/static/yinyue.png",
        "weight":3
    },
    {
        "name": "大反派",
        "url": "https://chat.openai.com/g/g-LfYbPkb2D-da-fan-pai",
        "description": "一个原始的、未经过滤的 GPT,它说话挑衅并寻求澄清。",
        "category": "艺术与生活",
        "category_weight": 10,
        "logo": "/static/fanpai.png",
        "weight": 2
    },
    {
        "name": "骂醒恋爱脑",
        "url": "https://chat.openai.com/g/g-qAbgTFqoa-ma-xing-lian-ai-nao",
        "description": "一个讽刺而直率的爱情评论家，用强烈的语言来解决浪漫的幻想。",
        "category": "艺术与生活",
        "category_weight": 10,
        "logo": "/static/lianai.png",
        "weight":1
    }


    # 您可以继续添加更多的链接
]


@app.route('/links')
def get_links():
    return jsonify(links)

if __name__ == '__main__':
    app.run(debug=True)
