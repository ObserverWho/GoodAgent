from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain_openai import ChatOpenAI

from config.settings import Settings


def initialize_agent(tools, memory):
    # 加载提示模板
    prompt = hub.pull("hwchase17/react")

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
