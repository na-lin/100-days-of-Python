from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # self.ball_speed = STARTING_SPEED
        # self.speed(self.ball_speed)
        # print(self.ball_speed)

    def create_ball(self):
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(x=0, y=0)

    def reset_ball(self):
        """already bounce_y,need to bounce_x"""
        """reverse the direction to the opposite """
        self.bounce_paddel()
        self.create_ball()
        self.move_speed = 0.1
        # self.ball_speed_up()'

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        """reverse_y"""
        self.y_move *= -1

    def bounce_paddel(self):
        """reverse_x"""
        self.x_move *= -1
        self.move_speed *= 0.9


    # def ball_speed_up(self):
    #     self.ball_speed += 1
    #     self.speed(self.ball_speed)
    #     print(self.speed())

    # rebound_x = self.xcor() + 5
    # rebound_y = self.ycor() - 15
    # self.goto(rebound_x,rebound_y)
    # insteady of my solution
    # is_at_edge = 1
    # if ball.ycor() > 280 or ball.ycor() < -280:
    #     is_at_edge *= -1
    # if is_at_edge == -1 :
    #     ball.rebound()
    # elif is_at_edge == 1:
    #     ball.move()
