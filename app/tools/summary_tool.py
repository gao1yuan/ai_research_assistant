from langchain.chains import ChatOpenAI
from langchain.agents import AgentExecutor

class SummaryTool:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4")

    def summarize(self, text: str) -> str:
        # 使用 GPT-4 生成摘要
        prompt = f"Summarize the following text: {text}"
        summary = self.llm.run(prompt)
        return summary