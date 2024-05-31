from dotenv import load_dotenv
from crewai import Crew
import agentops


from agents import EventAgents
from tasks import EventTasks


if __name__ == "__main__":
    load_dotenv()
    agentops.init(tags=["event-planning-crew"])

    crew = Crew(
        agents=[
            EventAgents.get_venue_coordinator(),
            EventAgents.get_logistics_manager(),
            EventAgents.get_marketing_agent(),
        ],
        tasks=[
            EventTasks.venue_task(),
            EventTasks.logistics_task(),
            EventTasks.marketing_task(),
        ],
        verbose=True,
        embedder={"provider": "openai", "config": {"model": "text-embedding-3-small"}},
    )

    result = crew.kickoff(
        inputs={
            "event_topic": "Tech Innovation Conference",
            "event_description": "A gathering of tech innovators "
            "and industry leaders "
            "to explore future technologies.",
            "event_city": "Bishkek",
            "tentative_date": "2024-09-15",
            "expected_participants": 500,
            "budget": 20000,
            "venue_type": "Conference Hall",
        }
    )
