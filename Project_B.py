import os
from openai import OpenAI

def clean_text(text: str) -> str:
    return text.encode("utf-8", errors="replace").decode("utf-8")

def safe_input(prompt: str) -> str:
    raw = input(prompt)
    return clean_text(raw).strip()

name = safe_input("请输入商品的名称：")
feature = safe_input("请输入商品的特点：")
user = safe_input("请输入适合的人群：")
price = safe_input("请输入你认为的价格是多少：")
scene = safe_input("请输入使用场景：")



client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
name = clean_text(name)
feature = clean_text(feature)
user = clean_text(user)
price = clean_text(price)
scene = clean_text(scene)


prompt = f"""
请根据以下商品信息，生成3种不同风格的商品文案：

商品名称：{name}
商品特点：{feature}
适用人群：{user}
价格：{price}
使用场景：{scene}

要求：
1. 输出【版本1：标准介绍版】
2. 输出【版本2：营销推荐版】
3. 输出【版本3：简短推荐版】
4. 文案用中文
5. 风格自然，像真实电商文案
"""

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result = clean_text(response.choices[0].message.content or "")
    print(result)

    with open("copywriting.txt", "a", encoding="utf-8", errors="replace") as f:
        f.write(result)
        f.write("\n" + "=" * 50 + "\n")

except Exception as e:
    print("发生错误：", repr(e))