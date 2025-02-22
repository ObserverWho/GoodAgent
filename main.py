from agents.weather_agent import build_react_agent
from memory.conversation import build_react_memory
from prompt.prompts import build_react_prompt
from tools.get_current_weather import weather_tool


def initialize_agent():
    tools = [weather_tool]
    memory = build_react_memory()
    return build_react_agent(
        tools=tools,
        prompt=build_react_prompt(),
        memory=memory,
    )


def main():
    agent = initialize_agent()
    questions = [
        "北京现在多少度？",  # 应触发天气工具
        # "把刚才说的城市换成广州",
        # "写一首秋天的诗？",  # 直接LLM回答
        # "帮我查一下杭州的天气",  # 明确触发工具
        # "今天适合去杭州旅游吗？请先告诉我当地天气"  # 组合查询
    ]

    for q in questions:
        print(f"\n用户问题: {q}")
        result = agent.invoke({"input": q})
        print(f"助理回答: {result['output']}\n{'-' * 50}")
        print("\n📜 当前对话历史：")
        print(agent.memory.buffer)  # 直接输出原始文本格式


if __name__ == "__main__":
    main()
