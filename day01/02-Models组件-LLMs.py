"""
    该脚本作用:对接LLMs的在线和本地大模型
"""
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
# todo 1. 使用ChatOpenAI调用LLMs
def dm01():
    # 1.1 实例化大模型
    model = ChatOpenAI(
        model=os.getenv('MODEL'),
        temperature=0.5,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.getenv('DEEPSEEK_API_KEY'),
        base_url=os.getenv('BASE_URL'),
        # organization="...",
        # other params...

    )
    res = model.invoke('讲个笑话吧?')
    print(res.content)

    # 1.2 获取结果
    pass
# todo 2. 使用ollama
def dm02():
    from langchain_ollama import OllamaLLM
    model = OllamaLLM(
        model='qwen2.5:7b',
        temperature=0.1

    )
    res = model.invoke('讲个笑话吧?')
    print(res)
# todo 2. 测试代码
if __name__ == '__main__':
    # dm01()
    dm02()