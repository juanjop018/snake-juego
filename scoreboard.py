from turtle import Turtle # Importa la librertia Turtle.
ALIGNMENT = "center" #Centra la barra de puntajes.
FONT = ("Courier", 24, "normal") #Le da una fuente a la barra de puntajes.

class Scoreboard(Turtle): #Le da una clase a la barra de puntajes.

    def __init__(self): #Se comienza la funcion
        super().__init__() #Se empieza con la funcion super.
        self.score = 0 #Se le asigna un puntaje.
        self.color("white") #Se le da el color al puntaje.
        self.penup() #Evitamos que se creen las lineas.
        self.goto(0, 270) #Se le asigna una puntacion al puntaje.
        self.hideturtle() #Oculta el contenido de la barra solo dejando el texto.
        self.update_scoreboard() #Para actualizar la barra.

    def update_scoreboard(self): #Le da color y forma a la fuente.
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT) 

    def game_over(self): #Se actualiza la informacion de la barra de puntaje y enseña el game over.
        self.goto(0, 0) 
        self.write("GAME OVER",align=ALIGNMENT, font=FONT) 

    def increase_score(self): #Incrementa el puntaje conforme avanza el juego.
        self.score += 1 
        self.clear() 
        self.update_scoreboard() 