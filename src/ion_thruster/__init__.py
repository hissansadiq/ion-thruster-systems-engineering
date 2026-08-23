"""Ion-Thruster: a small, gridded ion thruster performance and sizing calculator.
Equations follow the paper: Goebel, D. M. and Katz, I., "Fundamentals of
Electric Propulsion: Ion and Hall Thrusters", Wiley, 2008.
"""
from .performance import (
    exhaust_velocity,
    thrust,
    specific_impulse,
    input_power,
    xenon_ion_mass_kg,
)
__all__=[
    exhaust_velocity,
    thrust,
    specific_impulse,
    input_power,
    xenon_ion_mass_kg,
]

__version__="0.1.0"