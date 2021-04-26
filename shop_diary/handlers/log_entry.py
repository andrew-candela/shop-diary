from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils
from shop_diary.lib.ddb_utils import ShopDiaryDB

import typing
if typing.TYPE_CHECKING:
    from ask_sdk_model import Response
    from ask_sdk_core.handler_input import HandlerInput


class LogEntryHandler(AbstractRequestHandler):
    """Handler for LogEntry Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (
            ask_utils.is_intent_name("log_entry")(handler_input)
        )

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        shop_object = slots['shop_object'].value
        entry_value = slots['entry'].value
        milage = slots['milage'].value
        ddb_payload = {"milage": milage, "entry": entry_value}
        ddb = ShopDiaryDB()
        ddb.make_entry(shop_object, ddb_payload)
        speak_output = f"I've logged your entry for the {shop_object}"

        return (
            handler_input.response_builder
                         .speak(speak_output)
                         .response
        )
