"""
ChatModels的角色:
SystemMessage,HumanMessage,AIMessage
"""
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
def dm01():
    from langchain_openai import ChatOpenAI
    import os
    from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
    # 1. 实例化大模型
    model = ChatOpenAI(
        base_url=os.getenv('qw_base_url'),
        model='qwen-plus',
        api_key=os.environ.get('DASHSCOPE_API_KEY'),
        temperature=0.1

    )
    # messages = [
    #     SystemMessage(content='你是一个唐朝诗人'),
    #     HumanMessage(content='给我写一首关于河南的诗')
    # ]
    messages=[
        SystemMessage(content='你是一个唐朝诗人'),
        HumanMessage(content='给我写一首关于河南的诗词'),
        AIMessage(content='《豫州行》——长安客过中州作\n嵩岳云开万古青，黄河浪卷九霄霆。洛阳花落隋堤柳，汴水舟横唐寺铃。少林松影摇禅月，白马钟声渡晚汀。莫道中原风物老，一城烟火半唐经。 '),
        HumanMessage(content='给我写一首关于杭州的诗词')
    ]
    res = model.invoke(messages)

    # 2. 构建对话上下文消息列表
    print(res.content)
    # 3. 执行模型得到结果
if __name__ == '__main__':
    dm01()