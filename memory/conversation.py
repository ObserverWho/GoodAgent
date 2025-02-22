from langchain.memory import ConversationBufferMemory


def build_react_memory():
    return ConversationBufferMemory(
        memory_key="chat_history",  # 配置支持历史的Memory
        input_key='input',  # 与调用时的输入键匹配
        output_key='output',
        return_messages=True,  # 返回Message对象格式
    )
