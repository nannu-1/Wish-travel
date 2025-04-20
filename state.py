# Define State
from typing import TypedDict, Annotated, List
from langchain_core.messages import HumanMessage, AIMessage

class PlannerState(TypedDict):

    # Manages the state of the travel planning process.
    messages: Annotated[List[HumanMessage | AIMessage], "Chat memory"]
    city: str
    country: str
    interests: List[str]
    travel_dates: str
    budget: str
    itinerary: str
