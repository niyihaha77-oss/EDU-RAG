"""
    该脚本作用:在LangChain中使用Embedding模型的作用:将文本转换为向量
    实际的应用场景:
    1. 文本向量化:将文本转换为向量，以便进行相似度计算
    2. 文本嵌入:将文本嵌入到向量空间中，以便进行向量运算
    3. 文本分类:将文本分类为不同的类别
    4. 文本聚类:将文本聚类为不同的簇
    5. 文本检索:从大量文本中检索出与查询文本最相似的文本

"""
def dm01():
    from langchain_ollama import OllamaEmbeddings

    # 1. 初始化本地的向量模型
    model = OllamaEmbeddings(
        model='bge-m3',
        temperature=0.1
    )

    # 2. 单个文本向量化
    res1 = model.embed_query('这是一个测试文档')

    print(f"res1:{res1}")
    # print(f"res1.len:{len(res1)}")
    # 3. 多个文本向量化
    res2 = model.embed_documents(['这是一个测试文档', '这是第二个测试文档'])
    print(f"res2:{res2[0]}")
    # print(f"res2.len:{len(res2)}")
if __name__ == '__main__':
    dm01()