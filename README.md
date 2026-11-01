# Hydropower Generation and Performance Analysis

**Author:** Duran Ali Toklu  
**Field:** Energy Systems Engineering  
**Environment:** Python / Google Colab  
**Libraries:** NumPy, Pandas, Matplotlib

## Project purpose
An educational Python simulation of hydropower generation. The model evaluates the effects of inflow, ecological flow release, turbine flow capacity, penstock friction and minor losses, net head, and annual energy production.

> **Data note:** All flow values and system parameters are illustrative assumptions. They are not measured operating data from Kavşak Bendi HEPP or another real plant.

## Repository structure
- `src/hydropower_analysis.py` — main calculation model
- `notebooks/Hydropower_Generation_Analysis.ipynb` — Google Colab/Jupyter notebook
- `data/` — input data used by the simulation
- `results/` — monthly energy and design-sweep outputs
- `figures/` — generated charts
- `docs/` — technical report
- `README.md` — project overview and run instructions

## Baseline assumptions
- Gross head: 100 m
- Overall efficiency: 85%
- Ecological release: 10% of inflow
- Maximum turbine flow: 20 m³/s
- Penstock: 1,000 m long, 3.0 m diameter
- Darcy friction factor: 0.02
- Minor-loss coefficient: 2.0
- Monthly inflow (Jan–Dec): 12, 14, 18, 25, 30, 28, 22, 16, 12, 10, 9, 11 m³/s

## Baseline results
- Annual energy: **102,055.61 MWh (102.056 GWh)**
- Annual average power: **11.650 MW**
- Time-weighted average head loss: **1.991 m**
- Time-weighted average net head: **98.009 m**

## Design sweep
The tested grid covers penstock diameters of 2.5–4.5 m and maximum turbine flows of 12–24 m³/s. The highest energy output in this limited grid is **110.426 GWh/year**, at 4.5 m and 24 m³/s. This is an energy-only result, not a techno-economic optimum.

## Run locally
```bash
pip install numpy pandas matplotlib
python src/hydropower_analysis.py
```
The notebook can also be opened in Google Colab.

## HydroGenerate status
The HydroGenerate package was installed and its `calculate_hp_potential` interface was inspected during development. A numerical comparison is **pending verification**; no HydroGenerate numerical result is claimed in this project yet.

## Limitations
1. Monthly flows are assumed, not measured.
2. Total efficiency and friction factor are constant.
3. Hydraulic losses use a simplified Darcy–Weisbach model and one minor-loss coefficient.
4. Turbine hill charts, part-load efficiency, water hammer, cavitation, outages, sediment and detailed environmental constraints are not modelled.
5. The design sweep tests only a limited set of discrete combinations.

## References
- Idaho National Laboratory, HydroGenerate documentation: https://idaholabresearch.github.io/HydroGenerate/
- HydroGenerate on PyPI: https://pypi.org/project/HydroGenerate/
