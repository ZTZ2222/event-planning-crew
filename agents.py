from textwrap import dedent
from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool


class EventAgents:
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()

    _venue_coordinator = None
    _logistics_manager = None
    _marketing_agent = None

    @classmethod
    def _create_agent(cls, **kwargs):
        return Agent(
            **kwargs,
            verbose=True,
        )

    @classmethod
    def get_venue_coordinator(cls):
        if cls._venue_coordinator is None:
            cls._venue_coordinator = cls._create_agent(
                role="Venue Coordinator",
                goal=dedent(
                    """
                    Identify and book an appropriate venue 
                    based on event requirements
                    """
                ),
                backstory=dedent(
                    """
                    With a keen sense of space and 
                    understanding of event logistics, 
                    you excel at finding and securing 
                    the perfect venue that fits the event's theme, 
                    size, and budget constraints.
                    """
                ),
                tools=[cls.search_tool, cls.scrape_tool],
            )
        return cls._venue_coordinator

    @classmethod
    def get_logistics_manager(cls):
        if cls._logistics_manager is None:
            cls._logistics_manager = cls._create_agent(
                role="Logistics Manager",
                goal=dedent(
                    """
                    Manage all logistics for the event 
                    including catering and equipmen
                    """
                ),
                backstory=dedent(
                    """
                    Organized and detail-oriented, 
                    you ensure that every logistical aspect of the event 
                    from catering to equipment setup 
                    is flawlessly executed to create a seamless experience.
                    """
                ),
                tools=[cls.search_tool, cls.scrape_tool],
            )
        return cls._logistics_manager

    @classmethod
    def get_marketing_agent(cls):
        if cls._marketing_agent is None:
            cls._marketing_agent = cls._create_agent(
                role="Marketing and Communications Agent",
                goal=dedent(
                    """
                    Effectively market the event and 
                    communicate with participants.
                    """
                ),
                backstory=dedent(
                    """
                    Creative and communicative, 
                    you craft compelling messages and 
                    engage with potential attendees 
                    to maximize event exposure and participation.
                    """
                ),
                tools=[cls.search_tool, cls.scrape_tool],
            )
        return cls._marketing_agent
