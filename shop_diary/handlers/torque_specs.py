from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils
from shop_diary.lib.torque import get_torque_by_bolt_diameter
import logging

import typing
if typing.TYPE_CHECKING:
    from ask_sdk_model import Response
    from ask_sdk_core.handler_input import HandlerInput


logger = logging.getLogger(__name__)


class TorqueSpecsHandler(AbstractRequestHandler):
    """Handler for TorqueSpecs Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (
            ask_utils.is_intent_name("torque_specs")(handler_input)
        )

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        bolt_diameter = slots['bolt_size'].value
        speak_output = get_torque_by_bolt_diameter(bolt_diameter)

        return (
            handler_input.response_builder.speak(speak_output).response
        )
