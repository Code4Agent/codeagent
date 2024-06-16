import os
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch

# 加载 CodeBERT 模型和分词器
model_name = "microsoft/codebert-base"
tokenizer = RobertaTokenizer.from_pretrained(model_name)
model = RobertaForSequenceClassification.from_pretrained(model_name, num_labels=1)  # 用于二元分类
model.eval()

def classify_text(text):
    categories = ["vulnerable", "safe"]
    max_similarity = -1
    best_category = None
    for category in categories:
        input_text = f"文本：{text} [SEP] 类别：{category}"
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            similarity = torch.sigmoid(logits)  # 估计相似度
            if similarity > max_similarity:
                max_similarity = similarity
                best_category = category
    return best_category

def extract_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    start_keyword = "Security Analysis:"
    end_keyword = "Format Analysis:"
    start_index = content.find(start_keyword)
    end_index = content.find(end_keyword)
    if start_index != -1 and end_index != -1:
        return content[start_index+len(start_keyword):end_index].strip()
    return ""

def main(directory):
    vulnerable_folders = []
    for folder in os.listdir(directory):
        if folder.startswith('') and os.path.isdir(os.path.join(directory, folder)):
            file_path = os.path.join(directory, folder, 'manual.md')
            if os.path.exists(file_path):
                content = extract_content(file_path)
                if content and classify_text(content) == "vulnerable":
                    vulnerable_folders.append(folder)
    
    print("Folders classified as vulnerable:")
    for folder in vulnerable_folders:
        address = directory+f'/{folder}'
        print(address)

# 设定目录路径
directory_path = "../WareHouse"
main(directory_path)
