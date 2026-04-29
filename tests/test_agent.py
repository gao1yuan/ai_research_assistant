import unittest
from app.agent import Agent
from app.tools.search_tool import SearchTool
from app.tools.summary_tool import SummaryTool
from app.tools.analysis_tool import AnalysisTool
from app.memory import Memory

class TestAgent(unittest.TestCase):
    def setUp(self):
        search_tool = SearchTool()
        summary_tool = SummaryTool()
        analysis_tool = AnalysisTool()
        memory = Memory()
        self.agent = Agent(search_tool, summary_tool, analysis_tool, memory)

    def test_run(self):
        query = "What are the latest trends in AI?"
        result = self.agent.run(query)
        self.assertIn("Searching for papers", result)
        self.assertIn("Summary", result)
        self.assertIn("Analysis", result)

if __name__ == '__main__':
    unittest.main()