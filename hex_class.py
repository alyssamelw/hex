import turtle, random, math

class Hexagon():
 
    sides = 6
    side_length = 30
    angle = 60
    radius = math.sqrt(side_length ** 2 - (side_length / 2) ** 2)

    def __init__(self, turtle, position): 
        self.a = turtle
        self.start_hex = [position[0], position[1]] #set start point of the hexagon
        self.played = False
        
        self.centre_x = self.start_hex[0] + Hexagon.radius
        self.centre_y = self.start_hex[1] - Hexagon.side_length / 2
        self.centre = self.centre_x, self.centre_y
        
        self.draw_hexagon()

    def draw_hexagon(self): #draw one hexagon
        self.a.goto(self.start_hex)
        self.a.pendown()
        self.a.setheading(270) #begins facing 'south'
        
        for i in range(Hexagon.sides):
            self.a.fd(Hexagon.side_length)
            self.a.lt(Hexagon.angle)
       
        self.a.penup()
   
    def is_selected(self, click):  #checks if clicked within radius
        num1 = (click[0] - self.centre_x) ** 2
        num2 = (click[1] - self.centre_y) ** 2
        distance = math.sqrt(num1 + num2)
        return distance <= Hexagon.radius
    
    def fill_cell(self, moves): #draws filled hexagon, colour determined by turn
        self.a.penup()
        self.a.pensize(1)
        self.a.pencolor("black")
        if moves % 2 == 0:
            self.a.fillcolor("midnight blue")
        else:
            self.a.fillcolor("sky blue")
        self.a.begin_fill()
        self.draw_hexagon()
        self.a.end_fill()
        self.played = True 

class Board():
    
    diameter = Hexagon.radius * 2

    def __init__ (self, turtle, board_size, starting_position, random, screen):
        self.a = turtle
        self.board_size = board_size
        self.start = starting_position
        self.moves = 0
        self.random = random
        self.screen = screen
        self.board = []
        self.draw_board()
    
    def draw_board(self):
        self.screen.tracer(0, 0)
    
        self.a.penup()
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                row.append(Hexagon(self.a, self.start))
                self.start[0] += Board.diameter
            self.start[0] -= Board.diameter * (self.board_size - 1) + Hexagon.radius
            self.start[1] -= Hexagon.side_length + (Hexagon.side_length / 2)
            self.a.goto(self.start)
            self.board.append(row)
        
        self.a.rt(120)
        self.a.fd(Hexagon.side_length / 2)
        self.a.pensize(15)
        self.a.pendown()
        
        for i in range(2):
            self.a.color("sky blue")
            self.a.fd(Hexagon.side_length / 2)
            for i in range(self.board_size - 1):
                self.a.rt(Hexagon.angle)
                self.a.fd(Hexagon.side_length)
                self.a.lt(Hexagon.angle)
                self.a.fd(Hexagon.side_length)
            self.a.rt(Hexagon.angle)
            self.a.fd(Hexagon.side_length)
            
            self.a.color("midnight blue")
            self.a.rt(Hexagon.angle)
            self.a.fd(Hexagon.side_length)
            for i in range(self.board_size - 1):
                self.a.rt(Hexagon.angle)
                self.a.fd(Hexagon.side_length)
                self.a.lt(Hexagon.angle)
                self.a.fd(Hexagon.side_length)  
            self.a.rt(Hexagon.angle)
            self.a.fd(Hexagon.side_length / 2)
       
        self.a.penup()
        
        self.screen.update()

    def select(self, x, y):
        for row in self.board:
            for cell in row:
                if cell.is_selected((x, y)) is True and not cell.played:
                    cell.fill_cell(self.moves)
                    self.moves += 1
                    self.game_over()
                    
                    self.computer_move()
                    
    def computer_move(self):
        if self.moves < self.board_size ** 2:
            cnum1 = random.randint(0, (self.board_size - 1))
            cnum2 = random.randint(0, (self.board_size - 1))
            while self.board[cnum1][cnum2].played == True:
                cnum1 = random.randint(0, (self.board_size - 1))
                cnum2 = random.randint(0, (self.board_size - 1))
            
            cpos = self.board[cnum1][cnum2]
            if cpos.played is not True:
                self.a.goto(cpos.centre)
                cpos.fill_cell(self.moves)
                self.moves += 1
                self.game_over()
    
    def game_over(self):
        if self.moves == self.board_size ** 2:
            self.a.goto(-50, 50)
            self.a.write("Click to close window. ", True, font=("Times New Roman", 20, "normal"))
            self.screen.exitonclick()

def main():   
    screen = turtle.Screen()
    a = turtle.Turtle()

    board_size = int(input("What size would you like your board to be? "))
    starting_position = [0, 0]
    board = Board(a, board_size, starting_position, random, screen)
    
    moves = 0
    
    screen.onclick(board.select) 
    
    turtle.done()

main()