"""Unit tests for ion_thruster.performance.
Reference case (used throughout): a xenon gridded ion thruster with
beam voltage 1500 V, mass flow rate 5 mg/s (5e-6 kg/s), and total
efficiency 0.65.
"""
import math
import pytest
from ion_thruster.performance import (
    exhaust_velocity,
    thrust,
    specific_impulse,
    input_power,
    xenon_ion_mass_kg,
    ELEMENTARY_CHARGE_C,
    STANDARD_GRAVITY_M_S2,
)
def test_xenon_ion_mass_kg():
    m = xenon_ion_mass_kg()
    assert m == pytest.approx(2.1801e-25, rel=1e-3)

def test_exhaust_velocity_reference_case():
    m = xenon_ion_mass_kg()
    v_e = exhaust_velocity(1500.0, m)
    expected = math.sqrt(2 * ELEMENTARY_CHARGE_C * 1500.0 / m)
    assert v_e == pytest.approx(expected, rel=1e-9)
    assert 10_000.0 < v_e < 100_000.0 # tens of km/s

def test_exhaust_velocity_scales_with_sqrt_voltage():
    m = xenon_ion_mass_kg()
    v_1500 = exhaust_velocity(1500.0, m)
    v_6000 = exhaust_velocity(6000.0, m)
    assert v_6000 == pytest.approx(2.0 * v_1500, rel=1e-9)

def test_thrust_reference_case():
    m = xenon_ion_mass_kg()
    v_e = exhaust_velocity(1500.0, m)
    T = thrust(5e-6, v_e)
    assert T == pytest.approx(5e-6 * v_e, rel=1e-9)
    assert 0.005 < T < 0.5 # tens to hundreds of mN

def test_specific_impulse_reference_case():
    m = xenon_ion_mass_kg()
    v_e = exhaust_velocity(1500.0, m)
    isp = specific_impulse(v_e)
    assert isp == pytest.approx(v_e / STANDARD_GRAVITY_M_S2, rel=1e-9)
    assert 2000.0 < isp < 5000.0

def test_input_power_reference_case():
    m = xenon_ion_mass_kg()
    v_e = exhaust_velocity(1500.0, m)
    T = thrust(5e-6, v_e)
    P = input_power(T, v_e, 0.65)
    assert P == pytest.approx(T * v_e / (2 * 0.65), rel=1e-9)
    assert 1000.0 < P < 20000.0

def test_input_power_rejects_invalid_efficiency():
    with pytest.raises(ValueError):
        input_power(0.05, 30000.0, 0.0)
    with pytest.raises(ValueError):
        input_power(0.05, 30000.0, 1.5)

def test_input_power_lower_efficiency_needs_more_power():
    m = xenon_ion_mass_kg()
    v_e = exhaust_velocity(1500.0, m)
    T = thrust(5e-6, v_e)
    p_high_eff = input_power(T, v_e, 0.80)
    p_low_eff = input_power(T, v_e, 0.40)
    assert p_low_eff > p_high_eff