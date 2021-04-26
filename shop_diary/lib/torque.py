"""
This is a hackey way of giving a range of bolt torque specs.
"""

from typing import Union


exact_result = "Generally you can tighten an M-{size} bolt to {spec} " \
               "Newton Meters."
approx_result = "I'm guessing this would be between an M-{low} and M-{high} " \
                "sized bolt. Which would put it between {low_torque} " \
                "and {high_torque} Newton Meters."
way_too_high_result = "What kind of bolt is this? Are you messing with me?"
too_low_result = "This is a pretty small bolt. Be careful with this one. " \
                 "Certainly don't tighten more than {spec} Newton Meters."


def get_torque_by_bolt_diameter(bolt_diameter: Union[int, str]) -> str:
    bolt_diameter = int(bolt_diameter)
    if bolt_diameter < 5:
        return too_low_result.format(spec=7)
    if bolt_diameter == 5:
        return exact_result.format(size=5, spec=7)
    if bolt_diameter == 6:
        return exact_result.format(size=6, spec=12)
    if bolt_diameter < 8:
        return approx_result.format(low=6, high=8, low_torque=12,
                                    high_torque=30)
    if bolt_diameter == 8:
        return exact_result.format(size=8, spec=30)
    if bolt_diameter < 10:
        return approx_result.format(low=8, high=10, low_torque=30,
                                    high_torque=55)
    if bolt_diameter == 10:
        return exact_result.format(size=10, spec=55)
    if bolt_diameter < 12:
        return approx_result.format(low=10, high=12, low_torque=55,
                                    high_torque=100)
    if bolt_diameter == 12:
        return exact_result.format(size=12, spec=100)
    if bolt_diameter < 14:
        return approx_result.format(low=12, high=14, low_torque=55,
                                    high_torque=160)
    if bolt_diameter == 14:
        return exact_result.format(size=14, spec=160)
    if bolt_diameter < 16:
        return approx_result.format(low=14, high=16, low_torque=160,
                                    high_torque=245)
    if bolt_diameter == 16:
        return exact_result.format(size=16, spec=245)
    if bolt_diameter < 20:
        return approx_result.format(low=16, high=20, low_torque=245,
                                    high_torque=480)
    if bolt_diameter == 20:
        return exact_result.format(size=20, spec=480)
    else:
        return way_too_high_result
