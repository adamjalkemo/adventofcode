import numpy as np

#x_range = np.array([20, 30])
#y_range = np.array([-10, -5])
x_range = np.array([153, 199])
y_range = np.array([-114, -75])

y_max_global = 0
good_positions = set()
for vx in range(300, 0, -1):
    for vy in range(300, -300, -1):
#for vx in range(30, 0, -1):
#   for vy in range(30, -30, -1):
        #print(vx, vy)
        initial_velocity = np.array([vx, vy])
        velocity = np.array(initial_velocity)
        pos = np.array([0, 0])
        y_max = 0
        while True:
            pos += velocity
            y_max = max(y_max, pos[1])
            #if initial_velocity[0] == 7:
            #    print(initial_velocity, pos)

            if pos[0] > x_range[1] or pos[1] < y_range[0]:
                break

            if pos[0] >= x_range[0] and pos[0] <= x_range[1] and pos[1] >= y_range[0] and pos[1] <= y_range[1]:
                print(vx, vy)
                #print(initial_velocity, pos, y_max)
                y_max_global = max(y_max_global, y_max)
                good_positions.add((vx, vy))

            velocity[0] += np.sign(velocity[0]) * -1
            velocity[1] -= 1
print(y_max_global)
print(len(good_positions))
