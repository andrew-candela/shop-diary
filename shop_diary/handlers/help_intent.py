from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils
from shop_diary import intents

import typing
if typing.TYPE_CHECKING:
    from ask_sdk_model import Response
    from ask_sdk_core.handler_input import HandlerInput


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        if len(intents) > 1:
            first_ints_str = ', '.join(list(intents.keys())[:-1])
            speak_output = f"The intents I support are {first_ints_str} " \
                           f"and {list(intents.keys())[-1]}. "
        else:
            speak_output = f"The intents I support are {intents.keys()}. "
        for intent, use in intents.items():
            new_resp = f"To use {intent} say something like " \
                       f"{' or '.join(use)}. "
            speak_output = speak_output + new_resp
        return (
            handler_input.response_builder
                         .speak(speak_output)
                         .ask(speak_output)
                         .response
        )
