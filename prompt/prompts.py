# config/prompts.py
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def build_react_prompt():
    return ChatPromptTemplate.from_messages([

        ("system",
         "你是一个多功能助理，请根据用户问题类型选择响应方式：\n"
         "1. 当问题包含天气信息请求（如'天气'、'温度'、'湿度'）或明确地点时，必须调用 get_current_weather 工具\n"
         "2. 其他问题直接使用你的知识回答\n"
         "注意：不要假设用户位置，必须明确要求城市名称！"
         ),
        MessagesPlaceholder(variable_name="chat_history"),  # 关键历史占位符
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),

    ])
