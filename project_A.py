while True:
    question=input("请输入客服问题(按q退出）: ")

    if question=="q":
        break
    if"发货" in question:
        reply="尊敬的客户您好,我们一般在48小时内安排发货，请您耐心等待"
    elif "多久到" in question:
        reply="尊敬的客服您好，发货后一般3-7天达到，具体以物流信息为准."
    elif"退款" in question:
        reply="尊敬的客服您好，如需退款或退货，请联系客服，我们会尽快为您处理"
    else:
        reply="尊敬的客服您好，您的问题我已经收到，请你稍等，我们会尽快回复"

    print("====客服回复======")
    print(reply)
    print("--------")