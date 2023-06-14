# Python-Turtle-Graphics


This project is a simple turtle graphics program written in Python. It uses the turtle module, which provides a way to create graphics and animations using a turtle metaphor.

The program defines three functions: square(), circle(), and triangle(). Each function is responsible for drawing a specific shape using the turtle module's methods.

The square() function draws a red square with a side length of 100 units. It uses a loop to repeat the forward() and right() turtle commands four times to create the four sides of the square.

The circle() function draws an orange circle with a radius of 50 units. It uses the circle() method provided by the turtle module to draw the circle.

The triangle() function draws a green equilateral triangle with side length 100 units. It uses a loop to repeat the forward() and left() turtle commands three times to create the three sides of the triangle.

The main() function is the entry point of the program. It sets up the turtle environment by setting the speed and initial position of the turtle. Then it calls the square(), circle(), and triangle() functions in succession, with each shape drawn and the turtle moved forward by 150 units after each shape. Finally, the turtle.done() function is called to indicate that the drawing is complete.

When running this program, it will open a turtle graphics window and display the shapes drawn by the turtle. The square will be positioned on the left, followed by the circle in the middle, and the triangle on the right.
