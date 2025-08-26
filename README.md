# Cartesian to Polar Conversion with Differential Area Element

This project demonstrates the conversion from **Cartesian coordinates (x, y)** to **Polar coordinates (r, θ)** and visualizes a **differential area element** in polar coordinates:

- `r = sqrt(x^2 + y^2)`
- `θ = arctan2(y, x)`
- Differential area element: `dA = r dr dθ` (a small wedge of a ring)

## Features

- Cartesian point plotted (red dot)
- Radius line (blue) and angle arc (purple)
- Differential area element visualized with gradient (orange → pink)
- Grid, axes, and black labels for clarity
- Educational for understanding polar integration and coordinate transformation

## Usage

```bash
python cartesian_to_polar_pro_visual.py