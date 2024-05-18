import json
import requests
from datetime import datetime
from typing import List, Dict

class FinancialLiteracy:
    """A class to handle financial literacy topics and customer interactions."""

    def __init__(self, topics: List[str]):
        """
        Initializes the FinancialLiteracy class.

        Args:
            topics (List[str]): A list of financial topics.
        """
        self.topics = topics

    def get_topic_info(self, topic: str) -> str:
        """
        Fetches detailed information about a financial topic.

        Args:
            topic (str): The financial topic to fetch information about.

        Returns:
            str: Information about the topic.
        """
        # Simulating an API request to fetch topic information
        response = requests.get(f"https://api.example.com/financial_topics/{topic}")
        if response.status_code == 200:
            return response.json().get('info', 'No information available.')
        else:
            return "Error fetching topic information."

class CustomerInteraction:
    """A class to manage customer interactions."""

    def __init__(self, customer_id: str):
        """
        Initializes the CustomerInteraction class.

        Args:
            customer_id (str): The ID of the customer.
        """
        self.customer_id = customer_id
        self.timestamp = datetime.now()
        self.interactions = []

    def log_interaction(self, interaction: str):
        """
        Logs a customer interaction.

        Args:
            interaction (str): The interaction details.
        """
        self.interactions.append({
            "timestamp": self.timestamp.isoformat(),
            "interaction": interaction
        })

    def get_interaction_history(self) -> List[Dict[str, str]]:
        """
        Retrieves the interaction history.

        Returns:
            List[Dict[str, str]]: A list of past interactions.
        """
        return self.interactions

class PesaFlowAssistant:
    """A complex assistant class to manage financial literacy and customer interactions."""

    def __init__(self, customer_id: str):
        """
        Initializes the PesaFlowAssistant class.

        Args:
            customer_id (str): The ID of the customer.
        """
        self.customer = CustomerInteraction(customer_id)
        self.financial_literacy = FinancialLiteracy([
            "bonds",
            "bills",
            "money market funds",
            "index funds"
        ])

    def interact(self):
        """Handles the interaction with the customer."""
        print("Hello, my name is James, I’m an assistant from Pesa Flow. I wanted to check in with you about financial literacy.")
        customer_response = input("Would you be interested in learning about our financial literacy solutions? (yes/no): ").strip().lower()

        if customer_response == 'yes':
            print("Great! Here are the topics we can discuss:")
            for i, topic in enumerate(self.financial_literacy.topics, start=1):
                print(f"{i}. {topic.title()}")

            choice = int(input("Please enter the number of the topic you're interested in: "))
            if 1 <= choice <= len(self.financial_literacy.topics):
                chosen_topic = self.financial_literacy.topics[choice - 1]
                info = self.financial_literacy.get_topic_info(chosen_topic)
                print(f"Here is some information about {chosen_topic.title()}: {info}")
                self.customer.log_interaction(f"Discussed {chosen_topic.title()}")
            else:
                print("Invalid choice. Interaction terminated.")
        else:
            print("No problem. Have a great day!")
            self.customer.log_interaction("Customer declined financial literacy discussion")

    def save_interactions(self, filepath: str):
        """
        Saves the interaction history to a JSON file.

        Args:
            filepath (str): The path to the file where interactions will be saved.
        """
        with open(filepath, 'w') as file:
            json.dump(self.customer.get_interaction_history(), file, indent=4)

if __name__ == "__main__":
    # Initialize the assistant with a sample customer ID
    assistant = PesaFlowAssistant(customer_id="123456")

    # Run the interaction process
    assistant.interact()

    # Save the interactions to a file
    assistant.save_interactions("interaction_history.json")
