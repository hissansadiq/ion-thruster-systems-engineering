# Ion Thruster Systems Engineering

A small, honestly-scoped Python calculator for estimating the ideal performance
of a gridded electrostatic ion thruster.

## Why This Project Exists

This project implements standard textbook electric-propulsion relationships
for a simplified gridded ion-thruster model.

The equations are based on:

Goebel, D. M. and Katz, I., *Fundamentals of Electric Propulsion:
Ion and Hall Thrusters*, Wiley, 2008.

The project is intentionally small and verifiable. The goal is to maintain
engineering calculations as readable, tested Python code with a professional
Git workflow.

## Current Scope

The current implementation provides:

- Xenon ion mass calculation
- Ideal ion exhaust velocity
- Ideal beam thrust
- Specific impulse
- Electrical input power

The current thrust model assumes a fully ionized, single-species,
zero-divergence ion beam. Real-world thrust correction factors are not modeled
in this first version and are documented as a known limitation.

## Project Structure

```text
ion-thruster-systems-engineering/
├── src/
│   └── ion_thruster/
│       ├── __init__.py
│       └── performance.py
├── tests/
│   └── test_performance.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt