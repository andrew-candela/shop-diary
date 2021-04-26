"""There is no way this is being called.
I'll have to figure out what this is and why/how it's used later.
"""


from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils
from ask_sdk_model import DialogState
import logging
import six

import typing
if typing.TYPE_CHECKING:
    from ask_sdk_model import Response
    from ask_sdk_core.handler_input import HandlerInput


logger = logging.getLogger(__name__)


class InProgressLogEntryHandler(AbstractRequestHandler):
    """Handler for LogEntry Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (
            ask_utils.is_intent_name("log_entry")(handler_input)
            and
            handler_input.request_envelope.request.dialog_state !=
            DialogState.COMPLETED
        )

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.debug("In InProgressLogEntryHandler")
        for slot_name, current_slot in six.iteritems(current_intent.slots):
            if slot_name not in ["article", "at_the", "I_Want"]:
                if current_slot.resolutions.resolutions_per_authority[0].status.code == StatusCode.ER_SUCCESS_NO_MATCH:
                    if current_slot.name in required_slots:
                        prompt = "I'm in progress trying to find the slot value for {}".format(current_slot.name)

                        return handler_input.response_builder.speak(
                            prompt).ask(prompt).add_directive(
                                ElicitSlotDirective(
                                    slot_to_elicit=current_slot.name
                                )).response
                        # return handler_input.response_builder.add_directive(
                        #         ElicitSlotDirective(
                        #             slot_to_elicit=current_slot.name
                        #         )).response
                        

        return handler_input.response_builder.add_directive(
            DelegateDirective(
                updated_intent=current_intent
            )).response