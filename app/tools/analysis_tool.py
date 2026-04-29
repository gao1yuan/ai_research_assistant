from langchain.chains import ChatOpenAI
from langchain.agents import AgentExecutor

class AnalysisTool:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4")

    def analyze(self, text: str) -> str:
        # 进行文本分析，如情感分析、关键点提取等
        prompt = f"Analyze the following text and extract key points: {text}"
        analysis = self.llm.run(prompt)
        return analysis