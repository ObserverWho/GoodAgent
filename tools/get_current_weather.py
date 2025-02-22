from datetime import datetime

import requests
from langchain.agents import Tool
from langchain.tools import tool

from config.settings import Settings


@tool
def get_current_weather(location: str) -> str:
    """获取指定城市的实时天气数据（国内可用版）"""
    try:
        url = f"https://api.seniverse.com/v3/weather/now.json?key={Settings.WEATHER_API_KEY}&location={location}&language=zh-Hans"
        response = requests.get(url)
        data = response.json()

        if "results" not in data:
            return "天气查询失败，请检查城市名称"

        result = data["results"][0]
        loc = result["location"]
        now = result["now"]

        # 构建基础信息
        report = [
            f"📍 城市：{loc['name']} ({loc['path']})",
            f"🕒 更新时间：{datetime.strptime(result['last_update'], '%Y-%m-%dT%H:%M:%S%z').strftime('%Y年%m月%d日 %H:%M')}"
        ]

        # 天气核心指标
        core_info = [
            f"🌤️ 天气状况：{now['text']}",
            f"🌡️ 温度：{now['temperature']}℃\n",
        ]

        report += core_info
        return "\n".join(report)

    except Exception as e:
        return f"天气查询失败：{str(e)}"


weather_tool = Tool(
    name="get_current_weather",
    func=get_current_weather,
    description="获取指定城市的实时天气数据"
)
