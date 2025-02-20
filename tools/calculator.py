from langchain.tools import Tool

def calculate(expression: str) -> str:
    try:
        return str(eval(expression))
    except:
        return "Invalid mathematical expression"

calculator_tool = Tool(
    name="Calculator",
    func=calculate,
    description="Useful for performing mathematical calculations"
)
