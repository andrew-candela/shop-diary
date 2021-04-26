from ask_sdk_core.skill_builder import SkillBuilder

from shop_diary import handlers

# The SkillBuilder object acts as the entry point for your skill,
# routing all request and response payloads to the handlers above.
# Make sure any new handlers or interceptors you've defined are included below.
# The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(handlers.LaunchRequestHandler())
sb.add_request_handler(handlers.WhatsInMyGarageIntentHandler())
sb.add_request_handler(handlers.InProgressLogEntryHandler())
sb.add_request_handler(handlers.LogEntryHandler())
sb.add_request_handler(handlers.TorqueSpecsHandler())
sb.add_request_handler(handlers.HelpIntentHandler())
sb.add_request_handler(handlers.CancelOrStopIntentHandler())
sb.add_request_handler(handlers.SessionEndedRequestHandler())
# make sure IntentReflectorHandler is last so it doesn't override your
# custom intent handlers
sb.add_request_handler(handlers.IntentReflectorHandler())
sb.add_exception_handler(handlers.CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
