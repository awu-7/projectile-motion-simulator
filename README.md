# Projectile Motion Simulator
A physics simulator and visualizer that demonstrates how launch angles and velocities affect a projectile's trajectory. It can simulate millions of parameter combinations to visualize the optimal conditions for max distance and trade-offs between range and height. 

## Requirements
- Python 3.7+
- NumPy
- Matplotlib

## Setup
```bash
git clone https://github.com/awu-7/projectile-motion/  
cd projectile-motion
pip install numpy matplotlib
python projectile_motion.py
```

## Calculations
Only kinematics formulas are used. Further comments in ```projectile_motion.py```

## Outputs

<img width="600" height="350" alt="image" src="https://github.com/user-attachments/assets/92d8b84f-8119-48b9-a178-a75801e27438" /> <br>
```projectile_range_heatmap.png```  Confirms 45 degrees as optimal launch angle for range <br>
<img width="600" height="350" alt="image" src="https://github.com/user-attachments/assets/43255f6a-d462-44e4-bed1-ad759d0690e0" /> <br>
```projectile_height_heatmap.png``` Shows 90 degrees achieves max height <br>
<img width="2139" height="907" alt="image" src="https://github.com/user-attachments/assets/dc2954e6-1156-4f1c-adec-87fb7b956eca" />  
```projectile_range_heatmap.png``` 3D side-by-side comparison




