"""
文档加载器目前主要用两个:
1.UnstructuredFileLoader(万能加载器)
2.TextLoader(纯文本加载器)

"""
from langchain_unstructured import UnstructuredLoader
from langchain_community.document_loaders import TextLoader
def dm01_test_loader():
    # 1. 使用万能加载器 加载 txt文件
    loader = UnstructuredLoader(file_path='./data/衣服属性.txt')
    # 2. 调用load方法
    data = loader.load()
    # 3. 打印读出的内容
    print(data)

    pass
def dm02_txt_loader():
    loader = TextLoader('./data/衣服属性.txt',encoding='utf-8')
    docs = loader.load()
    print(docs)
    print(len(docs))
    print(type(docs[0]))




if __name__ == '__main__':
    # dm01_test_loader()
    dm02_txt_loader()
