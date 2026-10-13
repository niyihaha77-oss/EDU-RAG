"""
聊天提示词模板组件:
把 普通的文本提示词 转换为 聊天格式的提示词

"""

# todo 1. ChatPrompt --> 直接提问
def dm01_chat_prompt():
    from langchain_ollama import OllamaLLM
    from langchain_core.prompts import ChatPromptTemplate
    # 1. 初始化大模型
    model = OllamaLLM(
        model='qwen2.5:7b',
        temperature=0.1
    )
    # 2. 准备动态占位的提示词文本
    template = '请给出一个关于{topic}的笑话'

    # 3. 创建聊天提示词模板对象
    chat_prompt = ChatPromptTemplate.from_template(template)

    # 4. 填充变量,生成完整的可以发给模型的提示词
    prompt = chat_prompt.format_messages(topic='积极')
    print(prompt)
    print('❤️'*20)
    # 5. 发送提示词给模型，获取结果
    res = model.invoke(prompt)

    print(res)


if __name__ == '__main__':
    dm01_chat_prompt()

