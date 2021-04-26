from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils
import random
import typing
if typing.TYPE_CHECKING:
    from ask_sdk_model import Response
    from ask_sdk_core.handler_input import HandlerInput


class WhatsInMyGarageIntentHandler(AbstractRequestHandler):
    """Handler for WhatsInMyGarage Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("whats_in_my_garage")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        things = {
            'bicycles': ["Novara Big Buzz", "Schwynn hybrid named Suzette"],
            'motorcycles': ["2011 GSXR 750", "2007 Ducati Monster 695"]
        }
        slots = handler_input.request_envelope.request.intent.slots
        if not slots['thing_type'].value:
            thing_type = 'motorcycles'
        else:
            thing_type = slots['thing_type'].value
        if len(things[thing_type]) == 1:
            speak_output = things[thing_type][0]
        else:
            thing_string = "a ".join(things[thing_type][:-1]) + \
                           " and a " + things[thing_type][-1]
            speak_output = f"You have a {thing_string} in the garage."

        if "monster" in speak_output.lower() and random.uniform(0, 1) > .7:
            speak_output = speak_output + " The monster is kind of a piece " \
                         "of junk. But you did your best I guess."

        return (
            # .ask("add a reprompt if you want
            # to keep the session open for the user to respond")
            handler_input.response_builder
                         .speak(speak_output)
                         .response
        )
