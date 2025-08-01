# Add API KEY in .env file, get from https://app.agentops.ai/settings/projects
# AGENTOPS_API_KEY = "a606fd02-fde0-0c184dd70"
# Install pip install agentops or pip install 'crewai[agentops]'

from crewai import Agent, Crew, Task, Process
from dotenv import load_dotenv
import os
import agentops


class YourCrewName:
    def agent_one(self) -> Agent:
        return Agent(
            role="Data Analyst",
            goal="Analyze data trends in the market",
            backstory="An experienced data analyst with a background in economics",
            verbose=True,
        )

    def agent_two(self) -> Agent:
        return Agent(
            role="Market Researcher",
            goal="Gather information on market dynamics",
            backstory="A diligent researcher with a keen eye for detail",
            verbose=True,
        )

    def task_one(self) -> Task:
        return Task(
            name="Collect Data Task",
            description="Collect recent market data and identify trends.",
            expected_output="A report summarizing key trends in the market.",
            agent=self.agent_one(),
        )

    def task_two(self) -> Task:
        return Task(
            name="Market Research Task",
            description="Research factors affecting market dynamics.",
            expected_output="An analysis of factors influencing the market.",
            agent=self.agent_two(),
        )

    def crew(self) -> Crew:
        return Crew(
            agents=[self.agent_one(), self.agent_two()],
            tasks=[self.task_one(), self.task_two()],
            process=Process.sequential,
            verbose=True,
        )

if __name__ == "__main__":
    load_dotenv()
    my_crew = YourCrewName().crew()
    agentops.init(os.getenv("AGENTOPS_API_KEY"), instrument_llm_calls=True)
    result = my_crew.kickoff()

    print(result)

