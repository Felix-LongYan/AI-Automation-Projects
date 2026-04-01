import os
from openai import OpenAI

def generate_ai_copy(product, client):
    prompt = f"""
请根据以下商品信息，生成一段自然、简洁的中文商品文案：

商品名称：{product['name']}
商品特点：{product['feature']}
适用人群：{product['target']}
价格：{product['price']}
使用场景：{product['scene']}

要求：
1. 语言自然
2. 不要太夸张
3. 像电商真实描述
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def load_products(filename):
    products = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip().split(",")

            product = {
                "name": data[0],
                "feature": data[1],
                "target": data[2],
                "price": data[3],
                "scene": data[4]
            }

            products.append(product)

    return products

def generate_copy(product):
    return (
        f"这款{product['name']}具备{product['feature']}等优势，"
        f"适合{product['target']}，"
        f"适用于{product['scene']}等场景，"
        f"目前售价仅{product['price']}元。"
    )


def save_to_file(results, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for r in results:
            f.write(r + "\n")


# 主程序
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

products = load_products("products.txt")

results = []

for p in products:
    copy = generate_ai_copy(p, client)
    print(copy)
    results.append(copy)

# 最后再调用
save_to_file(results, "output.txt")