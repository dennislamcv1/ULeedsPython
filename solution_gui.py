import sys
from src.direction import Direction
from src import utils
from src.gui_environments import gui_environments


def move_robot_on_path(robot, path):
    for cell in path:
        current_cell = robot.position
        if current_cell.row - 1 == cell.row and current_cell.column == cell.column:
            robot.move(Direction.Up)
        elif current_cell.row + 1 == cell.row and current_cell.column == cell.column:
            robot.move(Direction.Down)
        elif current_cell.row == cell.row and current_cell.column - 1 == cell.column:
            robot.move(Direction.Left)
        elif current_cell.row == cell.row and current_cell.column + 1 == cell.column:
            robot.move(Direction.Right)

    if robot.position == robot.goal_cell:
        print('Hooray the robot is at the goal position!!!')
        print(f'Number of steps: {robot.num_motions}')
    else:
        print('The robot failed to reach the goal :(')


utils.check_input()
robot = gui_environments[sys.argv[1]]
path = utils.path_finding(robot)

if path: # This checks if there was a path
    move_robot_on_path(robot, path)

while True:
    robot.draw()
