from transformers import RobertaTokenizer, AutoModelForSeq2SeqLM

# 加载预训练的 CodeT5 模型和分词器
model_name = "Salesforce/codeT5-base"
tokenizer = RobertaTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def zero_shot_classification(text, categories):
    # 构造输入
    input_text = f"这段文本是关于{'还是'.join(categories)}？文本：{text}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    # 使用模型生成回答
    outputs = model.generate(input_ids, max_new_tokens=50)

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer

# 示例文本和分类
text = "这是一个关于先进计算机技术的文章。"
categories = ["科技", "文学"]
predicted_category = zero_shot_classification(text, categories)
print(predicted_category)
