"""Gridded ion thruster performance equations. Standard textbook relations for a gridded (electrostatic) ion
thruster, following:

Goebel, D. M. and Katz, I., "Fundamentals of Electric Propulsion:
Ion and Hall Thrusters", JPL Space Science and Technology Series,
Wiley, 2008. See Chapter 2 for the ideal beam exhaust velocity,
thrust, specific impulse, and input power relations used here.
All functions use SI units unless a function's docstring says
otherwise (specific impulse is returned in seconds, by convention).

"""

import math

ELEMENTARY_CHARGE_C=1.602176634e-19
AVOGADRO_NUMBER=6.02214076e23
STANDARD_GRAVITY_M_S2=9.80665

XENON_RELATIVE_ATOMIC_MASS=131.293

def xenon_ion_mass_kg():
    """Return the mass of a single xenon ion/atom in kilograms.
    float
    Mass of one xenon ion, in kilograms (~2.1801e-25 kg).
    """
    mass_g_per_mol=XENON_RELATIVE_ATOMIC_MASS
    mass_kg_per_mol=mass_g_per_mol * 1e-3
    return mass_kg_per_mol / AVOGADRO_NUMBER


def exhaust_velocity(beam_voltage_V,ion_mass_kg,charge_C=ELEMENTARY_CHARGE_C):
    """Ideal ion exhaust (beam) velocity from electrostatic acceleration.
    Derived from equating the kinetic energy gained by a singly
    charged ion falling through the beam voltage to its final kinetic
    energy: q * V_b = (1/2) * m * v_e^2, solved for v_e.
    """
    return math.sqrt(2.0 *charge_C*beam_voltage_V / ion_mass_kg)

def thrust(mass_flow_kg_s,exhaust_velocity_m_s):
    """Thrust from momentum flux of the ion beam.
    T = m_dot * v_e
    """
    return mass_flow_kg_s * exhaust_velocity_m_s

def specific_impulse(exhaust_velocity_m_s, g0=STANDARD_GRAVITY_M_S2):
    """Specific impulse from exhaust velocity: Isp = v_e / g0."""
    return exhaust_velocity_m_s  / g0

def input_power(thrust_N,exhaust_velocity_m_s,total_efficiency):
    
    """Electrical input power required to produce a given thrust.
    Derived from total efficiency defined as the ratio of directed
    beam kinetic power to electrical input power:
    eta_T = (T * v_e / 2) / P_in => P_in = T * v_e / (2 * eta_T)
    """
    if not (0.0 < total_efficiency <= 1.0):
        raise ValueError ("total_efficiency must be 0 or less than or equal to 1")
    return thrust_N*exhaust_velocity_m_s/(2.0 * total_efficiency)