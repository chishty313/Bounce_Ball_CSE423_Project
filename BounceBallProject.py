from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Ball properties
ball_radius = 20
ball_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]  # Initial position

# Midpoint Circle Algorithm

def draw_circle_midpoint(x_center, y_center, radius):
    x = 0
    y = radius
    d = 1 - radius

    # Plot initial points based on 8-way symmetry
    plot_circle_points(x_center, y_center, x, y)

    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        plot_circle_points(x_center, y_center, x, y)


def plot_circle_points(x_center, y_center, x, y):
    # 8-way symmetry points using GL_POINTS
    glBegin(GL_POINTS)
    glVertex2i(x_center + x, y_center + y)
    glVertex2i(x_center - x, y_center + y)
    glVertex2i(x_center + x, y_center - y)
    glVertex2i(x_center - x, y_center - y)
    glVertex2i(x_center + y, y_center + x)
    glVertex2i(x_center - y, y_center + x)
    glVertex2i(x_center + y, y_center - x)
    glVertex2i(x_center - y, y_center - x)
    glEnd()

# Display Function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_circle_midpoint(ball_position[0], ball_position[1], ball_radius)
    glFlush()

# Main Function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bounce Ball - Midpoint Circle Algorithm")

    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    glutDisplayFunc(display)
    glutMainLoop()

main()
