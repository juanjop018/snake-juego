from turtle import Turtle #importa la librertia Turtle.
import random #importa la  libreria de random para la aparicion de un objeto de manera aleatorio. 

class Food(Turtle): 

    def __init__(self): 
        super().__init__() 
        self.shape("circle") # Define la forma del objeto
        self.penup() #Para que no deje los rastros de la linea del objetivo.
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) 
        self.color("blue") #Le da el color al objeto
        self.speed("fastest") #Le da la velocidad de reaparecer a la comida.
        self.refresh() #Hacce que la comida vuelva a reaparecer.

    def refresh(self): 
        random_x = random.randint(-280, 280) #Sirve para ubicar el objeto dentro de la ventana de forma aleatorio en el eje x.
        random_y = random.randint(-280, 280) #Sirve para ubicar el objeto dentro de la ventana de forma aleatorio en el eje y.
        self.goto(random_x, random_y) #le da una direccion al objeto.