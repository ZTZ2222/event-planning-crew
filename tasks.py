from textwrap import dedent
from crewai import Task

from agents import EventAgents
from schemas import VenueDetails


class EventTasks:

    @staticmethod
    def venue_task():
        return Task(
            description=dedent(
                """
                Find a venue in {event_city} 
                that meets criteria for {event_topic}.
                """
            ),
            expected_output=dedent(
                """
                All the details of a specifically chosen
                venue you found to accommodate the event.
                """
            ),
            human_input=True,
            output_json=VenueDetails,
            output_file="venue_details.json",
            agent=EventAgents.get_venue_coordinator(),
        )

    @staticmethod
    def logistics_task():
        return Task(
            description=dedent(
                """
                Coordinate catering and 
                equipment for an event 
                with {expected_participants} participants 
                on {tentative_date}.
                """
            ),
            expected_output=dedent(
                """
                Confirmation of all logistics arrangements 
                including catering and equipment setup.
                """
            ),
            human_input=True,
            # async_execution=True,
            agent=EventAgents.get_logistics_manager(),
        )

    @staticmethod
    def marketing_task():
        return Task(
            description=dedent(
                """
                Promote the {event_topic} 
                aiming to engage at least
                {expected_participants} potential attendees.
                """
            ),
            expected_output=dedent(
                """
                Report on marketing activities 
                and attendee engagement formatted as markdown.
                """
            ),
            # async_execution=True,
            output_file="marketing_report.md",
            agent=EventAgents.get_marketing_agent(),
        )
