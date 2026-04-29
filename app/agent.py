from tools.search_tool import SearchTool
from tools.summary_tool import SummaryTool
from tools.analysis_tool import AnalysisTool
from memory import Memory

class Agent:
    def __init__(self, search_tool: SearchTool, summary_tool: SummaryTool, 
                 analysis_tool: AnalysisTool, memory: Memory):
        self.search_tool = search_tool
        self.summary_tool = summary_tool
        self.analysis_tool = analysis_tool
        self.memory = memory

    def run(self, query: str):
        # 任务处理逻辑：搜索、总结、分析
        search_results = self.search_tool.search(query)
        summary = self.summary_tool.summarize(search_results)
        analysis = self.analysis_tool.analyze(search_results)

        # 将结果保存到内存
        self.memory.save("search_results", search_results)
        self.memory.save("summary", summary)
        self.memory.save("analysis", analysis)

        # 返回最终输出
        return f"搜索结果: {search_results}, 摘要: {summary}, 分析: {analysis}"