from state import PlannerState

# 4. Build Graph
graph = StateGraph(PlannerState)

# add nodes
graph.add_node("Memory", RunnableLambda(memory_agent))
graph.add_node("LocalExpert", RunnableLambda(local_expert_agent))
graph.add_node("ExperienceCurator", RunnableLambda(experience_curator_agent))
graph.add_node("Weather", RunnableLambda(weather_agent))
graph.add_node("Logistics", RunnableLambda(logistics_agent))
graph.add_node("Budget", RunnableLambda(budget_agent))
graph.add_node("Event", RunnableLambda(event_agent))

#define edges
graph.set_entry_point("Memory")
graph.add_edge("Memory", "LocalExpert")
graph.add_edge("LocalExpert", "ExperienceCurator")
graph.add_edge("ExperienceCurator", "Weather")
graph.add_edge("Weather", "Logistics")
graph.add_edge("Logistics", "Budget")
graph.add_edge("Budget", "Event")
graph.add_edge("Event", END)

app = graph.compile()