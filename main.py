import os
import anthropic
from tree_of_thought import *

# Set the API key for Anthropic 
CLAUDE_API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key

# Get the permission from the owner of the API key to use it.
llm1 = anthropic.Anthropic(api_key=CLAUDE_API_KEY) 

# Define the prompt for the first model ( as a root of tree of thought)
query = "What is the potential impact of Chinese price war on Thailand economy?"

# Define the model and max token for the models
slm_model = "claude-3-5-sonnet-20240620"
# Define the model and max token for the models
slm_max_token = 1000



# Branching the query into sub-branches
response_domestic_market_competition = domestic_market_competition(query, llm1, slm_model, slm_max_token)
# Sub-branches of domestic market competition
response_price_undercutting = price_undercutting(response_domestic_market_competition, llm1, slm_model, slm_max_token)
response_market_share_losses = market_share_losses(response_domestic_market_competition, llm1, slm_model, slm_max_token)
response_response_domestic_market_competition = innovation_and_quality_improvement(response_domestic_market_competition, llm1, slm_model, slm_max_token)

# Branching the query into sub-branches
response_consumer_behavior = consumer_behavior(query, llm1, slm_model, slm_max_token)
# Sub-branches of consumer behavior
response_demand_for_cheaper_goods = demand_for_cheaper_goods(response_consumer_behavior, llm1, slm_model, slm_max_token)
response_disposable_income_and_spending_patterns = disposable_income_and_spending_patterns(response_consumer_behavior, llm1, slm_model, slm_max_token)
response_brand_layalty_and_perception = brand_layalty_and_perception(response_consumer_behavior, llm1, slm_model, slm_max_token)


# If the Developer consider any of the Sub-branches answer not good enough, they decide to manually remove the Sub-branches.
final_query = response_price_undercutting + \
              response_market_share_losses + \
              response_response_domestic_market_competition + \
              response_demand_for_cheaper_goods + \
              response_disposable_income_and_spending_patterns + \
              response_brand_layalty_and_perception

# Make the final conclusion based on the sub-branches
final_response = make_conclusion(final_query, llm1, slm_model, slm_max_token)

# Print the final response
print(final_response)