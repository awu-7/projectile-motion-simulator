import matplotlib.pyplot as plt
import numpy as np

# set parameters
NUM_THETA = 200     # number of angles to test
NUM_V = 200      # number of velocities to test
MAX_VELOCITY = 100   # highest velocity to test (m/s)

ANGLES = np.linspace(1, 89, NUM_THETA)                # test angles between 1 and 89 deg, since 0 and 90 are edge cases
VELOCITIES = np.linspace(1, MAX_VELOCITY, NUM_V)      # test velocities between 1 m/s and MAX_VELOCITY
ranges = np.zeros((len(VELOCITIES), len(ANGLES)))     # create ranges for plot based on number of entries in each array
angles_grid, velocities_grid = np.meshgrid(ANGLES, VELOCITIES)

GRAVITY = 9.8   # gravity on earth

# convert degrees to radians since NumPy trig functions use radians
angle_rad = np.radians(angles_grid)

# calculate initial velocity components
# note: v0x, v0y used in place of v_x, v_y in explanations to clarify initial vs final velocities
v_x = velocities_grid * np.cos(angle_rad)
v_y = velocities_grid * np.sin(angle_rad)

# calculate total flight time using kinematics
# start with equation: y = v0y*t + 0.5*ay*t^2
# when y = 0: 0 = v0y*t - 0.5*g*t^2
# factor out t: 0 = t(v0y - 0.5*g*t) => 0 = v0y - 0.5*g*t
flight_time = 2 * v_y / GRAVITY

# calculate range using kinematics
# start with equation: x = v0x*t + 0.5*a*t^2
# ax = 0 => x = v0x*t
ranges = v_x * flight_time

# calculate max height using kinematics
# vy^2 = v0y^2 + 2*ay*y
# at max height, final velocity is 0 => 0 = v0y^2 + 2*ay*y
heights = (v_y ** 2) / (2 * GRAVITY)  # max height varies squarely with initial velocity

# Plot
# Range heatmap
plt.figure(figsize=(12, 7))
plt.imshow(ranges, aspect='auto', origin='lower',
           extent=[1, 90, 1, MAX_VELOCITY], cmap='terrain')
plt.colorbar(label='Range (m)')
plt.xlabel('Launch Angle (deg)')
plt.ylabel('Initial Velocity (m/s)')
plt.title('Projectile Range Heatmap')
plt.savefig('projectile_range_heatmap.png', dpi=150)

# max height heatmap
plt.figure(figsize=(12, 7))
plt.imshow(heights, aspect='auto', origin='lower',
           extent=[0, 90, 0, MAX_VELOCITY], cmap='terrain')
plt.colorbar(label='Max Height (m)')
plt.xlabel('Launch Angle (deg)')
plt.ylabel('Initial Velocity (m/s)')
plt.title('Projectile Max Height Heatmap')
plt.savefig('projectile_height_heatmap.png', dpi=150)

# 3D plot for range and max height
fig = plt.figure(figsize=(16, 6))

# Plot 1: Range 3D Surface
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(angles_grid, velocities_grid, ranges,
                         cmap='terrain', edgecolor='none', alpha=0.8)
ax1.set_xlabel('Angle (deg)', fontsize=10, fontweight='bold')
ax1.set_ylabel('Velocity (m/s)', fontsize=10, fontweight='bold')
ax1.set_zlabel('Range (m)', fontsize=10, fontweight='bold')
ax1.set_title('Projectile Range', fontsize=12, fontweight='bold')
ax1.view_init(elev=25, azim=45)
fig.colorbar(surf1, ax=ax1, shrink=0.5)

# Plot 2: Height 3D Surface
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(angles_grid, velocities_grid, heights,
                         cmap='terrain', edgecolor='none', alpha=0.8)
ax2.set_xlabel('Angle (deg)', fontsize=10, fontweight='bold')
ax2.set_ylabel('Velocity (m/s)', fontsize=10, fontweight='bold')
ax2.set_zlabel('Height (m)', fontsize=10, fontweight='bold')
ax2.set_title('Projectile Max Height', fontsize=12, fontweight='bold')
ax2.view_init(elev=25, azim=45)
fig.colorbar(surf2, ax=ax2, shrink=0.5)

plt.suptitle('Range vs Height 3D Comparison', fontsize=14, fontweight='bold', y=1.00)
plt.tight_layout()
plt.savefig('range_vs_height_3d.png', dpi=150, bbox_inches='tight')
plt.show()
