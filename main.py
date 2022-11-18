from turtle import Screen #importa la librertia Turtle.
from snake import Snake #Llama al archivo snake y le importa la clase Snake.
from food import Food # Llama al archivo food y le importa la clase Food.
from scoreboard import Scoreboard #Llama al archivo scoreboard y le importa la clase Scoreboard.
import time #Este permite contar el tiempo de la ejecucion y controla su flujo.

#creacion de la ventana
screen = Screen() # Importamos la ventana 
screen.setup(width=600, height=600) # Este controla las dimensiones.
screen.bgcolor("black") # Este le da el color.
screen.title("Snake Game") # Este da el titulo que llevara.
screen.tracer(0) #Reconoce la animacion de la libreria Turtle.

snake = Snake() #Importa la clase Snake. 
food = Food() #Importa la clase Food.
scoreboard = Scoreboard() #Importa la clase Scoreboard.


screen.listen() #Da el numero de conexiones no aceptadas en el sistema antes de rechazar nuevas conexiones.
screen.onkey(snake.up, "Up") #Vincula la liberacion de la tecla superior.
screen.onkey(snake.down, "Down") #Vincula la liberacion de la tecla inferior.
screen.onkey(snake.left, "Left") #Vincula la liberacion de la tecla  izquierda.
screen.onkey(snake.right, "Right") #Vincula la liberacion de la tecla Derecho.

game_is_on = True #Se crea el segmento que es verdadero.
while game_is_on: #Se crea un ciclo para elo movimiento.
    screen.update() #Se inserta elementos especificos de una libreria.
    time.sleep(0.1) #Cotrola la velocidad de movimiento.
    snake.move() #Detecta el movimiento.

    #detect collision with food
    if snake.head.distance(food) <15: 
        food.refresh() #Vuelve a regenerar la comida.
        snake.extend() #Consume la comida.
        scoreboard.increase_score() #Al consumir la comida da el puntaje.

    #dectect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor() > 280 or snake.head.ycor()< -280: 
        game_is_on=False 
        scoreboard.game_over() #Detecta la colision con un borde del muro, para al instante acabar el juego.

    #detect collision with tail.
    for segment in snake.segments: 
        if segment == snake.head: 
            pass 
        elif snake.head.distance(segment)<10: 
            game_is_on = False 
            scoreboard.game_over() #Detecta la colision con el mismo cuerpo, para al instante acabar el juego. 

screen.exitonclick() 


