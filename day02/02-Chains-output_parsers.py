from langchain_core.prompts import ChatPromptTemplate


# todo 1. 字符串解析器

def dm01_string_output_parser():
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_ollama import OllamaLLM,ChatOllama
    model = ChatOllama(
        model='qwen2.5:7b'
    )
    prompt = ChatPromptTemplate.from_template("解释{topic}是什么?回答控制在20字以内")
    chain1 = prompt | model
    result1 = chain1.invoke({'topic':'ai'})
    print(f"result1-->{result1}")

    parser = StrOutputParser()
    chain = prompt|model|parser
    result2 = chain.invoke({'topic':'ai'})
    print(f"result2-->{result2}")



# todo 2. list解析器
def dm02_list_output_parser():
    from langchain_core.output_parsers import CommaSeparatedListOutputParser,JsonOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_ollama import OllamaLLM,ChatOllama

    model = ChatOllama(
        model='qwen2.5:7b'
    )
    parser = CommaSeparatedListOutputParser()

    format_instructions = parser.get_format_instructions()
    print(format_instructions)

    prompt = ChatPromptTemplate.from_template("用中文列出5个{topic}相关的概念. \n{format_instructions}")

    chain = prompt | model | parser

    res = chain.invoke({'topic':'ai', 'format_instructions':format_instructions})

    print(res)
def dm03_json_output_parser():
    from langchain_core.output_parsers import CommaSeparatedListOutputParser,JsonOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_ollama import OllamaLLM,ChatOllama

    model = ChatOllama(
        model='qwen2.5:7b'
    )
    parser = JsonOutputParser()

    format_instructions = parser.get_format_instructions()
    print(format_instructions)

    prompt = ChatPromptTemplate.from_template("用中文列出5个{topic}相关的概念. \n{format_instructions}")

    chain = prompt | model | parser

    res = chain.invoke({'topic':'ai', 'format_instructions':format_instructions})

    print(res)
# todo 4.
def dm04_structured_output_parser():
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import PydanticOutputParser      # Pydantic专用输出解析器(强类型结构化解析器)
    from pydantic import BaseModel, Field           # 导入Pydantic基础父类 与 字段描述工具.
    from typing import List                         # 列表类型注解, 用于多元素字段的定义.
    from langchain_ollama import OllamaLLM

    # 实例化大模型
    model = OllamaLLM(
        model='qwen2.5:7b'
    )
    # 定义Pydantic类
    class Movie(BaseModel):
        title: str = Field(description="电影标题")
        director: str = Field(description="导演姓名")
        year: int = Field(description="上映年份")
        genre: List[str] = Field(description="电影类型")
        rating: float = Field(description="评分（1-10）")
    # 3.创建Pydantic解析器对象
    parser = PydanticOutputParser(pydantic_object=Movie)
    format_instructions = parser.get_format_instructions()
    prompt = ChatPromptTemplate.from_template( "生成一部{genre}电影的信息。\n{format_instructions}")

    chain = prompt | model | parser
    print(chain)
    result = chain.invoke({'genre': '科幻', 'format_instructions': format_instructions})
    print(result)
    print(type(result))

# todo 5. 自定义解析器
def dm05_custom_output_parser():
    from langchain_core.output_parsers import BaseOutputParser
    from langchain_ollama import OllamaLLM
    from typing import Dict, Any

    model = OllamaLLM(
        model='qwen2.5:7b'
    )
    # 2.自定义键值对解析器, 继承LangChain统一解析器基类 BaseOutputParser
    class CustomKeyValueParser(BaseOutputParser[Dict[str, Any]]):
        """解析形如'key: value'的文本"""
        def parse(self, text: str) -> Dict[str, Any]:
            """从文本中解析键值对"""
            result = {}
            lines = text.strip().split('\n')
            for line in lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    result[key.strip()] = value.strip()
            return result

        def get_format_instructions(self) -> str:
            """提供格式指导给模型"""
            return """请以'键: 值'的格式返回信息，每行一个键值对。
                    例如：
                    名称: 爱因斯坦
                    职业: 物理学家
                    贡献: 相对论
                    国家: 美国
                    
                    """
        # 使用自定义解析器
    custom_parser = CustomKeyValueParser()
    format_instructions = custom_parser.get_format_instructions()
    custom_prompt = ChatPromptTemplate.from_template(
        "提供关于{person}的基本信息。\n{format_instructions}"
    )
    # 组合组件
    custom_chain = custom_prompt | model | custom_parser
    # 调用模型
    result = custom_chain.invoke({
        "person": "申帅军",
        "format_instructions": format_instructions
    })
    print(result)

if __name__ == '__main__':

    # dm01_string_output_parser()
    # dm02_list_output_parser()
    dm05_custom_output_parser()