import PlannerState from state

# User Input
print("Welcome to Wish Travel: Your AI Travel Planner")
city = input("Enter your destination city:")
country = input("Enter the country:")
interests = input("List your interests (comma-separated):").split(",")
travel_dates = input("Enter your travel dates (e.g., July 2025):")
budget = input("Enter your budget level (low, medium, high):")

example_input: PlannerState = {
    "messages": [],
    "city": city.strip(),
    "country": country.strip(),
    "interests": [i.strip() for i in interests],
    "travel_dates": travel_dates.strip(),
    "budget": budget.strip(),
    "itinerary": ""
}


# Run
result = app.invoke(example_input)

# Print Output
print("\n Final Itinerary\n")
print(result['itinerary'])

print("\n Conversation Log \n")
for msg in result['messages']:
    print(msg.type.upper() + ":", msg.content)
