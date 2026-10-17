from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter

def dm01_text_splitter():
    # 1.初始化文档分割器对象
    # 参1: 分割符 参2: 每个分块的大小 参3: 每个分块的重叠部分
    text_splitter = CharacterTextSplitter(separator=' ',chunk_size=5,chunk_overlap=1)

    # 2.场景1:纯文本切割
    res1 = text_splitter.split_text('今 天 的 天 气 特 别 好')
    print(f"res1:{res1}")
    print(f"len(res1):{len(res1)}")
    print(f"type(res1):{type(res1)}")
    print("="*100)
    pass
    # 3.场景2:多句话切割
    res2 = text_splitter.create_documents(['今 天 的 天 气 特 别 好','我 很 感 兴 味'])
    print(f"res2:{res2}")
    print(f"len(res2):{len(res2)}")
    print(f"type(res2):{type(res2)}")
    print("="*100)
    # 场景3:切割Document对象,细节:Document对象的元数据会被字块继承
    res3 = text_splitter.split_documents([Document(page_content='今 天 的 天 气 特 别 好',metadata={'id':1})])
    print(f"res3:{res3}")
    print(f"len(res3):{len(res3)}")
    print(f"type(res3):{type(res3)}")
# 递归切割
def dm02():
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,  # 每个块最多 20 个字符
    chunk_overlap=6,  # 相邻分块会共享 6 个字符
    length_function=len,  # 用字符数来衡量长度
    separators=["\n\n", "\n", " ", ""]  # 会优先尝试按 \n\n 分段，如果太长，再按 \n → 空格 → 逐字符切分。
)

    text = """
    人工智能正在快速发展，尤其是大语言模型的应用，正在改变人类的工作方式。
    它们可以帮助人们进行写作、代码生成、甚至是科研探索。
    相比之下，新能源的发展同样重要。
    电动车和太阳能正在逐渐替代传统能源，减少碳排放，对全球环境保护至关重要。
    """
    docs = text_splitter.split_text(text)
    print(docs)
# 语义切割
def dm03():
    from langchain_experimental.text_splitter import SemanticChunker
    from langchain_ollama import OllamaEmbeddings

    embed = OllamaEmbeddings(model="mxbai-embed-large")

    text_splitter = SemanticChunker(
        embeddings=embed,
        breakpoint_threshold_type='percentile',
        # 更低的百分位会更“积极”地切分（数值越小 => 切得越多）
        breakpoint_threshold_amount=20.0,
        # 句子拆分正则为同时识别中/英文终结符
        sentence_split_regex=r'(?<=[。！？.!?])\s*',
        # 每个切分后片段（chunk）至少要有多少个字符
        min_chunk_size=10
    )

    text = """
    人工智能正在快速发展，尤其是大语言模型的应用，正在改变人类的工作方式。
    它们可以帮助人们进行写作、代码生成、甚至是科研探索。
    相比之下，新能源的发展同样重要。
    电动车和太阳能正在逐渐替代传统能源，减少碳排放，对全球环境保护至关重要。
    """

    docs = text_splitter.split_text(text)
    for i, d in enumerate(docs):
        if d.strip():
            print(f"------ Chunk {i + 1} ------")
            print(d.strip())
            print()
def md():
    from langchain_text_splitters import MarkdownHeaderTextSplitter

    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

    markdown_text = "# Header 1\nSome text\n## Header 2\nMore text\n### Header 3\nEven more text"
    docs = markdown_splitter.split_text(markdown_text)
    print(docs)
if __name__ == '__main__':

    # dm01_text_splitter()
    # dm02()
    # print('='*100)
    # dm03()
    md()