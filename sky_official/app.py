from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    achievements = [
        {
            "title": "项目方案设计",
            "desc": "已完成项目整体结构设计，包括长期记忆、人格画像与智能遗忘三大核心模块。"
        },
        {
            "title": "官网展示系统",
            "desc": "已完成项目官网展示平台，用于内容介绍、成果展示、截图整理与软著辅助说明。"
        },
        {
            "title": "功能原型规划",
            "desc": "已完成AI陪伴系统的功能规划，包括登录注册、聊天交互、记忆管理与用户画像。"
        },
        {
            "title": "申报材料整理",
            "desc": "支持项目展示、比赛申报、作品包装与后续软件著作权材料整理。"
        }
    ]

    workflow_steps = [
        "用户进入系统并建立基础资料",
        "通过初始问答或量表形成个体画像",
        "在持续对话中筛选重要信息",
        "将高价值内容纳入长期记忆",
        "在后续互动中调用记忆形成连续陪伴"
    ]

    demo_images = [
        {
            "name": "官网首页展示",
            "desc": "展示项目定位、核心亮点与引导入口。",
            "tag": "Homepage",
            "image": "images/demo1.jpg"
        },
        {
            "name": "产品功能展示",
            "desc": "展示长期记忆、人格画像与智能遗忘机制。",
            "tag": "Product",
            "image": "images/demo2.jpg"
        },
        {
            "name": "作者介绍展示",
            "desc": "展示作者背景、研究方向与项目角色。",
            "tag": "Author",
            "image": "images/demo3.jpg"
        }
    ]

    return render_template(
        "index.html",
        page_title="SKY蓝天官网 - 首页",
        achievements=achievements,
        workflow_steps=workflow_steps,
        demo_images=demo_images
    )


@app.route("/product")
def product():
    return render_template("product.html", page_title="SKY蓝天官网 - 产品介绍")


@app.route("/about")
def about():
    return render_template("about.html", page_title="SKY蓝天官网 - 项目介绍")


@app.route("/author")
def author():
    return render_template("author.html", page_title="SKY蓝天官网 - 作者介绍")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        content = request.form.get("content", "").strip()

        if name and email and content:
            message = f"提交成功，感谢你，{name}！我会尽快查看你的留言。"
        else:
            message = "请完整填写姓名、邮箱和留言内容。"

    return render_template("contact.html", page_title="SKY蓝天官网 - 联系我", message=message)


if __name__ == "__main__":
    app.run(debug=True)