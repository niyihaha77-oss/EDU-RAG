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


if __name__ == '__main__':

    dm01_text_splitter()