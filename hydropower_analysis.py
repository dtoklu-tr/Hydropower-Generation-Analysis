"""
Hydropower Generation and Performance Analysis
Educational simulation using assumed monthly flow data.
All input values are illustrative, not measured data from a real hydropower plant.
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
FLOW_M3S = np.array([12, 14, 18, 25, 30, 28, 22, 16, 12, 10, 9, 11], dtype=float)
DAYS = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

RHO = 1000.0
G = 9.81
EFFICIENCY = 0.85
GROSS_HEAD_M = 100.0
ECOLOGICAL_FLOW_RATIO = 0.10
TURBINE_CAPACITY_M3S = 20.0
PENSTOCK_LENGTH_M = 1000.0
PENSTOCK_DIAMETER_M = 3.0
DARCY_FRICTION_FACTOR = 0.02
MINOR_LOSS_COEFFICIENT = 2.0


def run_monthly_model(diameter_m=PENSTOCK_DIAMETER_M,
                      turbine_capacity_m3s=TURBINE_CAPACITY_M3S):
    """Return monthly hydraulic and energy results for the assumed flow profile."""
    available_flow = FLOW_M3S * (1 - ECOLOGICAL_FLOW_RATIO)
    turbine_flow = np.minimum(available_flow, turbine_capacity_m3s)

    area = math.pi * diameter_m**2 / 4
    velocity = turbine_flow / area

    friction_loss = (
        DARCY_FRICTION_FACTOR
        * (PENSTOCK_LENGTH_M / diameter_m)
        * (velocity**2 / (2 * G))
    )
    minor_loss = MINOR_LOSS_COEFFICIENT * (velocity**2 / (2 * G))
    total_loss = friction_loss + minor_loss
    net_head = GROSS_HEAD_M - total_loss

    power_kw = EFFICIENCY * RHO * G * turbine_flow * net_head / 1000
    energy_mwh = power_kw * 24 * DAYS / 1000

    result = pd.DataFrame({
        "Month": MONTHS,
        "Incoming flow (m3/s)": FLOW_M3S,
        "Turbine flow (m3/s)": turbine_flow,
        "Velocity (m/s)": velocity,
        "Friction loss (m)": friction_loss,
        "Minor loss (m)": minor_loss,
        "Total head loss (m)": total_loss,
        "Net head (m)": net_head,
        "Power (kW)": power_kw,
        "Energy (MWh)": energy_mwh,
    })
    return result


def run_design_sweep():
    """Compare the specified penstock diameters and turbine capacities."""
    diameters = [2.5, 3.0, 3.5, 4.0, 4.5]
    capacities = [12, 16, 20, 24]
    rows = []
    for diameter in diameters:
        for capacity in capacities:
            monthly = run_monthly_model(diameter, capacity)
            annual_mwh = monthly["Energy (MWh)"].sum()
            rows.append({
                "Penstock diameter (m)": diameter,
                "Maximum turbine flow (m3/s)": capacity,
                "Annual energy (MWh)": annual_mwh,
                "Annual energy (GWh)": annual_mwh / 1000,
            })
    return pd.DataFrame(rows)


if __name__ == "__main__":
    monthly = run_monthly_model()
    print("MONTHLY RESULTS")
    print(monthly.round(2).to_string(index=False))

    annual_mwh = monthly["Energy (MWh)"].sum()
    print(f"\\nAnnual energy: {annual_mwh:,.2f} MWh ({annual_mwh/1000:.3f} GWh)")
    print(f"Average power: {annual_mwh*1000/8760:,.2f} kW")

    monthly.plot(x="Month", y="Energy (MWh)", kind="bar", legend=False)
    plt.title("Monthly Hydropower Energy Production")
    plt.ylabel("Energy (MWh)")
    plt.tight_layout()
    plt.show()

    design_results = run_design_sweep()
    print("\\nDESIGN SWEEP")
    print(design_results.round(2).to_string(index=False))
    design_results.to_csv("optimization_results.csv", index=False)
