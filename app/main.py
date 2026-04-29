from agent import Agent
from tools.search_tool import SearchTool
from tools.summary_tool import SummaryTool
from tools.analysis_tool import AnalysisTool
from memory import Memory
import sys

# 初始化工具
search_tool = SearchTool()
summary_tool = SummaryTool()
analysis_tool = AnalysisTool()
memory = Memory()

# 创建 Agent 实例
agent = Agent(search_tool, summary_tool, analysis_tool, memory)

def main():
    # 启动 Agent，等待用户请求
    query = sys.argv[1] if len(sys.argv) > 1 else "请提供问题"
    response = agent.run(query)
    print(response)

if __name__ == "__main__":
    main()