# Projectile Motion Simulator
This project is a physics simulator intended to help students gain a better understanding of projectile motion and kinematics. It demonstrates how launch angles and velocities affect projectile range and maximum height. The program can simulate millions of parameter combinations and generates multiple plots with Matplotlib, including heatmaps and interactive 3D plots that can be used to analyze optimal launch conditions. 

## Key Takeaways
- Max range is achieved at 45 degrees, regardless of initial velocity
- Max height increases with launch angle, from 0 to 90 degrees
- There is a clear trade-off between range and height

## Setup
**Requirements**
- Python 3.7+
- NumPy
- Matplotlib

**Installation**
```bash
git clone https://github.com/awu-7/projectile-motion/  
cd projectile-motion
pip install numpy matplotlib
python projectile_motion.py
```

## Calculations
This simulator assumes projectile motion with no air resistance.

**Kinematics**  
$\Delta x = v_0t + \frac{1}{2}at^2$  
$v^2 = v_0^2 +2a\Delta x$  

**Range**  
$x = v_x t$
Note: this is also equal to $\frac{v_0^2 \sin(2\theta)}{g}$. Try to derive it yourself!  

**Height**  
$y = \frac{v_y^2}{2g}$ 

**Velocity components**  
$v_0x = v_0 \cos(\theta)$  
$v_0y = v_0 \sin(\theta)$  

See ```projectile_motion.py``` for more detailed explanations and derivations.

## Output
Running the script generates three plots that are saved as images:
- **projectile_range_heatmap.png**: range across all parameter combinations
- **projectile_height_heatmap.png**: maximum height across all parameter combinations
- **range_vs_height_3d.png**: side-by-side view of 3D surface plots for range and height
