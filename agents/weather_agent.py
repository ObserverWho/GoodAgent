# agents/weather_agent.py
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import MessagesPlaceholder
from langchain_openai import ChatOpenAI

from config.settings import Settings


def build_react_agent(tools, prompt, memory):
    llm = ChatOpenAI(
        model_name=Settings.LLM_MODEL_NAME,
        temperature=0,
        openai_api_key=Settings.LLM_API_KEY,
        openai_api_base=Settings.LLM_API_BASE,
    )

    # 配置代理参数
    agent_kwargs = {
        "input_variables": ["input", "chat_history", "agent_scratchpad", "current_time"],
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="chat_history")]
    }

    # 初始化代理
    agent = create_openai_tools_agent(llm, tools, prompt)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
        # 输入键对齐
        input_variables=["input", "chat_history", "agent_scratchpad"],
        # 中间步骤转换
        return_intermediate_steps=True
    )
