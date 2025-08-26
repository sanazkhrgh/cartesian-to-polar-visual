import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
#Cartesian point
x = 3
y = 4

#Convert to Polar coordinates
r = np.hypot(x, y)
theta = np.arctan2(y, x)
print(f"Cartesian: x = {x}, y = {y}")
print(f"Polar: r = {r:.2f}, θ = {theta:.2f} rad, θ = {np.degrees(theta):.2f}°")

# Differential area element
dr = 0.5
dtheta = np.pi/12
theta_vals = np.linspace(theta, theta + dtheta, 200)
x_inner = r * np.cos(theta_vals)
y_inner = r * np.sin(theta_vals)
x_outer = (r + dr) * np.cos(theta_vals)
y_outer = (r + dr) * np.sin(theta_vals)

# Custom gradient for differential area
colors = ["#ff7f50", "#ff1493"] # orange to deep pink
cmap = LinearSegmentedColormap.from_list("my_cmap", colors)

# Prepare figure
fig, ax = plt.subplots(figsize=(8,8))
ax.set_aspect('equal')
ax.set_facecolor('#ffffff')

# Grid and axes
ax.grid(True, linestyle='--', color='mediumpurple', alpha=0.5)
ax.axhline(0, color='purple', linewidth=1)
ax.axvline(0, color='purple', linewidth=1)

# Plot Cartesian point
ax.plot(x, y, 'ro', markersize=10, label=f"Point ({x},{y})")

# Draw radius line
ax.plot([0, x], [0, y], color='#1e90ff', linewidth=2, label=f"r = {r:.2f}")

# Draw angle arc
arc = np.linspace(0, theta, 100)
ax.plot(r*0.3*np.cos(arc), r*0.3*np.sin(arc), color='#9400d3', linewidth=2, label=r"$\theta$")

# Draw differential area with gradient-like effect
for i in range(len(theta_vals)-1):
  ax.fill_between([x_inner[i], x_outer[i]], [y_inner[i], y_outer[i]], [y_inner[i], y_outer[i]],
  color=cmap(i/len(theta_vals)), alpha=0.7)

# Boundary arcs
ax.plot(x_inner, y_inner, color='#8a2be2', linewidth=2)
ax.plot(x_outer, y_outer, color='#8a2be2', linewidth=2)

# Radial lines for differential area
ax.plot([r*np.cos(theta), (r+dr)*np.cos(theta)],
[r*np.sin(theta),(r+dr)*np.sin(theta)], color='#8a2be2', linestyle='--', linewidth=1.5)
ax.plot([r*np.cos(theta+dtheta),(r+dr)*np.cos(theta+dtheta)],
[r*np.sin(theta+dtheta),(r+dr)*np.sin(theta+dtheta)], color='#8a2be2', linestyle='--', linewidth=1.5)

# Mark origin
ax.plot(0, 0, 'ko', markersize=10, markeredgewidth=2)

# Labels (black)
ax.text(x/2, y/2 , f"r={r:.2f}" , color='black',fontsize=12)
ax.text(0.15, 0.05, f"θ={np.degrees(theta):.1f}°", color='black', fontsize=12)

# Title and legend
ax.set_title("Cartesian to Polar with Differential Area Element", fontsize=14 , color='black')
ax.legend(fontsize=12)

# Set limits
ax.set_xlim(-1, max(x+r+dr, y+r+dr)+1)
ax.set_ylim(-1, max(x+r+dr, y+r+dr)+1)
plt.show()

