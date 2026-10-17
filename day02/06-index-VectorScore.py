"""
RAG核心前4步:
1. 文档加载(load)
2. 文档分割(split)
3. 向量存储(Embedding & store)
4. 搜索(search)
"""
def dm01_index_vector():
    # 回顾: 完整RAG知识库构建流程: 加载txt文档 -> 文本分块 -> 向量化存入Chroma本地向量库 -> 相似度检索查询
    from langchain_text_splitters import CharacterTextSplitter          # 导入文本分割器
    from langchain_chroma import Chroma                                 # 轻量级本地向量数据库
    from langchain_community.document_loaders import TextLoader         # 导入纯文本加载器
    from langchain_ollama import OllamaEmbeddings                       # 本地嵌入向量模型
    # ---------------------------------- 步骤1: 加载本地txt知识库文档 ----------------------------------

    # 1. 实例化txt加载器, 指定文件路径 和 编码.
    loader = TextLoader('./data/pku.txt',encoding='utf-8')
    docs = loader.load()
    # print(f"docs:{docs}")

    # 2. 文本分割
    text_splitter = CharacterTextSplitter(separator='\n\n',chunk_size=200, chunk_overlap=30)

    split_docs = text_splitter.split_documents(docs)
    # 3. 向量化
    embeddings = OllamaEmbeddings(model='mxbai-embed-large')

    chromadb = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        persist_directory='./chroma_db'
    )

    # 3.扩展说明: 如果向量库已经提前建好,数据已存入, 后续程序可直接加载使用, 无需重复向量化.
    # chromaDB = Chroma(persist_directory='./chromaDB', embedding_function=embeddings)
    # print(split_docs)
    # 1. 输入问题
    query = '北京师范大学是985吗'
    query2 = '1937年北京大学发生了什么'

    # 2. 去chroma中检索
    results1 = chromadb.similarity_search(query,k=2)
    results2 = chromadb.similarity_search(query2,k=2)
    print(results1)
    print('*'*30)
    print(results2)

if __name__ == '__main__':
    dm01_index_vector()