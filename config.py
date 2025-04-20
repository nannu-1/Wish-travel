from langchain_groq import ChatGroq
from state import PlannerState


# Load LLM
llm=ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama-3.3-70b-versatile"
)


# Define Agents
def memory_agent(state: PlannerState) -> PlannerState:
    return state  # Extend with ChromaDB lookup

def local_expert_agent(state: PlannerState) -> PlannerState:
    prompt = f" You are a travel expert. Provide safety, culture, and must-know info for visiting {state['city']}, {state['country']}"
    response = llm.invoke([HumanMessage(content=prompt)])
    state["messages"].append(response)
    return state

def experience_curator_agent(state: PlannerState) -> PlannerState:
    prompt = f"Based on interests: {state['interests']}, plan activities in {state['city']} that match"
    response = llm.invoke([HumanMessage(content=prompt)])
    state["messages"].append(response)
    return state

def weather_agent(state: PlannerState) -> PlannerState:
    response = AIMessage(content="Checked weather: Mostly sunny, 25°C")
    state["messages"].append(response)
    return state

def logistics_agent(state: PlannerState) -> PlannerState:
    prompt = f"Organize the activities into a logical 5-day itinerary for {state['city']} in {state['travel_dates']}"
    response = llm.invoke([HumanMessage(content=prompt)])
    state["itinerary"] = response.content
    state["messages"].append(response)
    return state

def budget_agent(state: PlannerState) -> PlannerState:
    prompt = f"""
    Ensure this itinerary fits within a {state['budget']} budget.
    """
    response = llm.invoke([HumanMessage(content=prompt)])
    state["messages"].append(response)
    return state

def event_agent(state: PlannerState) -> PlannerState:
    response = AIMessage(content="Local Event: Tokyo Ramen Festa on Day 3")
    state["messages"].append(response)
    return state
