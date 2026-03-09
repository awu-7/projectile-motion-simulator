import matplotlib.pyplot as plt
import numpy as np

MAX_VELOCITY = 100
ANGLES = np.linspace(0, 90, 100)        # set a range of angles between 0 and 90 deg
VELOCITIES = np.linspace(1, 100, 100)   # set a range of reasonable velocities in m/s
ranges = np.zeros((len(VELOCITIES), len(ANGLES)))       # create ranges for plot based on entries in each dimension
angles_grid, velocities_grid = np.meshgrid(ANGLES, VELOCITIES)

GRAVITY = 9.8   # gravity on earth

def projectile_motion(initial_velocity, angle_deg, gravity = GRAVITY):
    # convert degrees to radians since NumPy trig functions use radians
    angle_rad = np.radians(angle_deg)

    # calculate initial velocity components
    v_x = velocities_grid * np.cos(angle_rad)
    v_y = velocities_grid * np.sin(angle_rad)

    # calculate total flight time using kinematics
    # y = v0*t + 0.5*a*t^2
    # since y = 0, we can rearrange to get the following equation:
    flight_time = 2 * v_y / GRAVITY

    # calculate range using kinematics
    # x = v0*t + 0.5*a*t^2
    # after plugging in a = 0, we get the following equation:
    range_value = v_x * flight_time
    height_value = (v_y ** 2) / (2 * gravity)
    return range_value, height_value

ranges, heights = projectile_motion(VELOCITIES,ANGLES,GRAVITY)

# Heat map formatting
# range heatmap
plt.figure(figsize=(12, 7))
plt.imshow(ranges, aspect='auto', origin='lower',
           extent=[0, 90, 0, MAX_VELOCITY], cmap='terrain')
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
