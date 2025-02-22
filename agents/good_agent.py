from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from config.settings import Settings


def initialize_agent(tools, memory):
    # 加载提示模板
    # prompt = hub.pull("hwchase17/react")

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "你是一个多功能助理，请根据用户问题类型选择响应方式：\n"
         "1. 当问题包含天气信息请求（如'天气'、'温度'、'湿度'）或明确地点时，必须调用 get_current_weather 工具\n"
         "2. 其他问题直接使用你的知识回答\n"
         "注意：不要假设用户位置，必须明确要求城市名称！\n"
         "可用工具：\n"
         "{tools}\n"
         "工具名称：[{tool_names}]\n"
         ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])

    # 初始化LLM
    llm = ChatOpenAI(
        model_name=Settings.LLM_MODEL_NAME,
        temperature=0,
        openai_api_key=Settings.LLM_API_KEY,
        openai_api_base=Settings.LLM_API_BASE,
    )

    # 创建智能体
    agent = create_react_agent(llm, tools, prompt)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )
