from config.settings import settings
from agents.good_agent import initialize_agent
from memory.conversation import create_memory
from tools.web_search import setup_search_tool
from tools.calculator import calculator_tool
from tools.custom_tool import joke_tool

def main():
    # 初始化工具集
    tools = [
        setup_search_tool(),
        calculator_tool,
        joke_tool
    ]

    # 创建记忆系统
    memory = create_memory()

    # 初始化智能体
    agent = initialize_agent(tools, memory)

    # 交互循环
    while True:
        try:
            query = input("\nUser: ")
            if query.lower() in ['exit', 'quit']:
                break

            result = agent.invoke({"input": query})
            print(f"\nAgent: {result['output']}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
