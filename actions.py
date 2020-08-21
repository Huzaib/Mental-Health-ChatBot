# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
import requests
import random

from db_sqlite import insert_data

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("LINK: ", tracker.get_slot('LINK'))
        print(tracker.latest_message)

        dispatcher.utter_message(text="Hello World!")

        return []


class MoodCount(FormAction):
    def name(self):
        return "mood_score"

    def required_slots(self, tracker) -> List[Text]:
        return ["name", "age", "history", "feeling", "addiction", "knowledge", "Stars", "sharing"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "name": [
                self.from_text(),
            ],
            "age": [
                self.from_text(),
            ],

            "history": [
                self.from_text(),
            ],
            "feeling": [
                self.from_text(),
            ],
            "addiction": [
                self.from_text(),
            ],
            "knowledge": [
                self.from_text(),
            ],
            "Stars": [
                self.from_text(),
            ],
            "sharing": [
                self.from_text(),
            ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Your answers have been stored. ")
        insert_data(tracker.get_slot("name"), tracker.get_slot("age"), tracker.get_slot("history"),
                    tracker.get_slot("feeling"), tracker.get_slot("addiction"), tracker.get_slot("knowledge"),
                    tracker.get_slot("Stars"), tracker.get_slot("sharing"))
        return []
