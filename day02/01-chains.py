"""
Chains 可以将多个组件组合在一起，形成一个完整的流程。
表现形式:上一个输出 | -> 下一个输入

"""
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# todo 1. 上一个输出 | -> 下一个输入
def dm01():
    # 1. 准备通用提示词
    template = '我的邻居姓{lastname},请给他儿子起几个霸气侧漏的中文名字'
    prompt = PromptTemplate(template=template, input_variables=["lastname"])
    # 2. 实例化大模型
    model = OllamaLLM(
        model='qwen2.5:7b',
        # temperature=0.7
    )
    model2 = OllamaLLM(
        model='qwen2.5:7b',
        # temperature=0.7
    )

    # 3. 使用管道符连接
    chain = prompt | model
    # 4. 执行链条

    res = chain.invoke('王')
    print(res)
    # chain = chain | model2
    # res = chain.invoke('评价一下起的名字怎么样?')
    # print(res)
    pass
# todo 2. 上一个模型的输出 | -> 下一个模型的输入
def dm02():
    # ================== 第一个模型:起名字 =====================
    template = '我的邻居姓{lastname},请给他儿子起几个霸气侧漏的中文名字'
    prompt = PromptTemplate(template=template, input_variables=["lastname"])
    # 2. 实例化大模型
    model = OllamaLLM(
        model='qwen2.5:7b',
    # temperature=0.7
    )
    first_chain = prompt | model
    # ================== 第二个模型:评价名字 =====================
    second_prompt = PromptTemplate(template='邻居儿子名字叫{child_name}评价一下起的名字怎么样?', input_variables=['child_name'])
    second_chain = second_prompt | model

    # 合并执行

    final_chain = first_chain | second_chain
    print(first_chain)
    print("❤️"*20)
    print(second_chain)
    print("❤️"*20)
    print(final_chain)

    res = final_chain.invoke('王')
    print(res)






# todo n. 测试代码
if __name__ == '__main__':
    # dm01()
    dm02()