import ollama
# todo 1. 生成式
def dem01():
    res = ollama.generate(
    model='qwen2.5:7b',
    prompt='为什么天空是蓝色的'

    )
    print(res['response'])
    pass
# todo 2. 聊天室
def dem02():
    res = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {"role": "user", "content": "讲个笑话吧?"}
        ],
    )
    print(res['message']['content'])
# todo 3. 流式输出
def dm04():
    res = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {"role": "user", "content": "地球为什么是球形?"}
        ],
        stream=True
    )
    for chunk in res:
        print(chunk['message']['content'], end="", flush=True)
if __name__ == '__main__':

    # dem01()
    # dem02()
    dm04()