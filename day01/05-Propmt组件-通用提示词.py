"""
    该脚本作用:在LangChain中使用Prompt模板组件
    可以是零样本，也可以是少数样本

"""
# todo 1. 通用提示词--> 零样本学习
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_ollama import OllamaLLM
def zero_short_learning(user_name):
    # 1.1 初始化本地大模型
    model = OllamaLLM(
        model='qwen2.5:7b',
        temperature=0.1
    )
    # 1.2 编写通用的提示词模板的文本
    template = '我的邻居姓{lastname},请给他儿子起几个霸气侧漏的中文名字'
    # 1.3 创建通用提示词模板对象
    prompt = PromptTemplate(
        template=template,
        input_variables=['lastname', ]
    )
    # 1.4 填充变量,生成完整的可以发给模型的提示词
    prompt_text = prompt.format(lastname=user_name)
    print(f"prompt_text:{prompt_text}")

    # 1.5 发送提示词给模型，获取结果
    res = model.invoke(prompt_text)
    print(f"res:{res}")
    pass

# todo 2. 通用提示词--> 少数样本学习
def few_shot_learning():
    # 2.1 初始化本地大模型
    model = OllamaLLM(
        model='qwen2.5:7b',
        temperature=0.1
    )
    # 2.2 定义样本实例数据集列表[字典]
    examples = [
        {'word': '开心', 'antonym': '悲伤'},
        {'word': '高', 'antonym': '矮'},

    ]
    # 2.3 单条实例的提示词模板
    example_template = '单词"{word}"的反义词是"{antonym}"'

    # 2.4 创建提示词模板对象
    example_prompt = PromptTemplate(
        template=example_template,

        input_variables=['word','antonym']
    )
    # 2.5 组装完整的少样本提示词模板
    few_shot_prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix='请给出单词的反义词',
        suffix='单词"{input}"的反义词是:',
        input_variables=['input'],
        example_separator='\n',
    )
    prompt_text = few_shot_prompt.format(input='黑马')
    print(prompt_text)
    # 2.6 发送提示词给模型，获取结果
    res = model.invoke(prompt_text)
    print(f"res:{res}")
    pass


if __name__ == '__main__':
    # zero_short_learning('李')
    few_shot_learning()
