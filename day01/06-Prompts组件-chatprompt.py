"""
聊天提示词模板组件:
把 普通的文本提示词 转换为 聊天格式的提示词

"""
from langchain_core.prompts import MessagesPlaceholder


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
# todo 2. ChatPrompt --> 零样本学习
def dm02_chat_prompt_zero_shot_learning():

    from langchain_ollama import OllamaLLM
    from langchain_core.prompts import ChatPromptTemplate,HumanMessagePromptTemplate
    from langchain_core.messages import SystemMessage

    # 1. 初始化大模型
    model = OllamaLLM(
        model='qwen2.5:7b',
        temperature=0.1
    )

    # 2. 准备系统提示词
    system_message = SystemMessage(
        content='你是一个脾气很差的老人,最讨厌别人问你问题,因为会打扰你抽烟'
    )
    # 3.创建聊天提示词模板对象
    human_str = '我的邻居姓{lastname},请给他儿子起几个霸气侧漏的中文名字'
    human_template = HumanMessagePromptTemplate.from_template(human_str)
    # 4.组装
    chat_template = ChatPromptTemplate.from_messages([system_message, human_template])
    # 5.生成完整的可以发给模型的提示词
    prompt = chat_template.format_messages(lastname='李')
    print(prompt)
    print('❤️'*20)
    # 6.发送提示词给模型，获取结果
    res = model.invoke(prompt)

    print(res)
# todo 3. ChatPrompt --> 少样本学习
def dm03_chat_prompt_few_shot_learning():
    from langchain_ollama import OllamaLLM
    from langchain_core.prompts import ChatPromptTemplate,HumanMessagePromptTemplate
    from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
    # 1. 初始化大模型
    model = OllamaLLM(
        model='qwen2.5:7b',
        temperature=0.1
    )
    # 2.创建模板
    prompt_template = ChatPromptTemplate.from_messages([
        # SystemMessage(content='你是一个 helpful的助手'),
        ("system", "你是一个 helpful的助手"),
        # HumanMessage(content='我的邻居姓李,请给他儿子起一个霸气侧漏的中文名字'),
        # AIMessage(content='好的，李明'),
        # HumanMessage(content='我的邻居姓王,请给他儿子起一个霸气侧漏的中文名字'),
        # AIMessage(content='好的，王伟'),
        MessagesPlaceholder("history"),# 占位符,变量名是history
        # HumanMessage(content='{question}')
        ("human", "{question}")
    ])
    # 3.创建few-short
    history=[
        ('human','我的邻居姓李,请给他儿子起一个霸气侧漏的中文名字'),
        ('ai','好的，李明'),
        ('human','我的邻居姓王,请给他儿子起一个霸气侧漏的中文名字'),
        ('ai','好的，王伟')
    ]
    # 填充变量,生成完整的可以发给模型的提示词
    prompt = prompt_template.format_messages(history=history, question='我的邻居姓张,请给他儿子起一个霸气侧漏的中文名字')
    print(prompt)
    print('❤️'*20)
    # 6.发送提示词给模型，获取结果
    res = model.invoke(prompt)

    print(res)

if __name__ == '__main__':
    # dm01_chat_prompt()

    # dm02_chat_prompt_zero_shot_learning()
    dm03_chat_prompt_few_shot_learning()
