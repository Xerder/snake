import pygame
import random
import time

class Game():
    def __init__(self,width,height):
        self.width = width //30*30
        self.height = height //30*30
        self.snake = Snake(width,height,self) 
        pygame.init()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.screen.fill("white")          
    def play(self):
        self.food_spawn()
        self.run = True
        while self.run:
            for event in pygame.event.get():
                self.event_handler(event)
            self.snake.move(self.width,self.height)
            self.snake.draw(self.screen)
            self.food_draw()
            if self.check_eat():
                self.food_spawn()
                self.snake.length +=1  
                self.view_score()
            pygame.display.update()
            time.sleep(0.1)

    def view_score(self):
        font = pygame.font.SysFont("timesnewroman",30)
        scr = (font.render(f"{self.snake.length}",True,"black"))     
        self.screen.blit(scr,(880,570)) 
        
    def game_over(self):
        self.run = False

    def event_handler(self,event):
        if event.type == pygame.QUIT:
            pygame.quit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.snake.y_speed = -self.snake.snake_step 
                self.snake.x_speed = 0 
               
            elif event.key == pygame.K_s:
                self.snake.y_speed = self.snake.snake_step 
                self.snake.x_speed = 0 
            elif event.key == pygame.K_a:
                self.snake.x_speed = -self.snake.snake_step 
                self.snake.y_speed = 0 
            elif event.key == pygame.K_d:
                self.snake.x_speed = self.snake.snake_step 
                self.snake.y_speed = 0 
            

    def food_spawn(self):
        self.food_x = random.randint(0,self.width) //30*30
        self.food_y = random.randint(0,self.height) //30*30

    def food_draw(self):
        pygame.draw.rect(self.screen,'red',[self.food_x,self.food_y,self.snake.snake_block,self.snake.snake_block])

    def check_eat(self):
        if self.food_x - self.snake.snake_block <= self.snake.x_pos <= self.food_x + self.snake.snake_block and\
            self.food_y- self.snake.snake_block <= self.snake.y_pos <= self.food_y + self.snake.snake_block:
            return True        
        return False 




class Snake():
    def __init__(self,width,height,obj):
        self.snake_list = []
        self.snake_block = 30
        self.snake_step = 30
        self.x_pos = width/2 //30*30
        self.y_pos = height/2 //30*30
        self.x_speed = 0
        self.y_speed = 0
        self.length = 1
        self.game = obj
  
    def draw(self,screen):
        black = '#000000'
        snake_head = [self.x_pos, self.y_pos]
        self.snake_list.append(snake_head)
        if len(self.snake_list)>self.length:
            pygame.draw.rect(screen,'white',[self.snake_list[0][0], self.snake_list[0][1], self.snake_block, self.snake_block])
            del self.snake_list[0]
        self.check_eat_itself()

        for coords in self.snake_list:
            pygame.draw.rect(screen,black,[coords[0], coords[1], self.snake_block, self.snake_block])
            


        
        


    def move(self,width,height):
        self.x_pos+=self.x_speed
        self.y_pos+=self.y_speed
        if self.x_pos<0:
            self.x_pos = width-30
        elif self.x_pos>width:
            self.x_pos = 0
        elif self.y_pos<0:
            self.y_pos = height-30
        elif self.y_pos>height:
            self.y_pos = 0

    def check_eat_itself(self):
        for i in self.snake_list[:-1]:
            if i == [self.x_pos,self.y_pos]:
                self.game.game_over()





            
        
def main():
    game = Game(900,600)
    game.play()


if __name__ =="__main__":
    main()






