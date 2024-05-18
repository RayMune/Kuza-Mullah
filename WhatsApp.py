import json
import requests
from datetime import datetime
from typing import List, Dict
from twilio.rest import Client

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

