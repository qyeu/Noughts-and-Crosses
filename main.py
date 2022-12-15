import pygame, os, sys


class Game:
    def __init__(self):
        
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Naughts & Crosses")
        self.icon = pygame.image.load("icon.png")
        pygame.display.set_icon(self.icon)

        self.clock = pygame.time.Clock()

        self.game_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

        self.board_img = pygame.image.load("board.png")
        self.x = pygame.image.load("x.png")
        self.o = pygame.image.load("o.png")

        self.turn = 'x'

        self.winner = None
        self.draw = None

        self.main_menu()

    def user_click(self, mouse_click):
        mouseX, mouseY = pygame.mouse.get_pos()
        row = None
        col = None
        #decides which box the user clicked
        if mouseX < 213 and mouseY < 160:
            row = 0
            col = 0

        if mouseX > 213 and mouseY < 160:
            row = 0
            col = 1
        if mouseX > (213 * 2):
            row = 0
            col = 2

        if mouseX < 213 and mouseY > 160:
            row = 1
            col = 0

        if mouseX > 213 and mouseY > 160:
            row = 1
            col = 1
        
        if mouseX > (213 * 2) and mouseY > 160:
            row = 1
            col = 2

        if mouseX < 213 and mouseY > (160 * 2):
            row = 2
            col = 0
        
        if mouseX > 213 and mouseY > (160 * 2):
            row = 2
            col = 1
        
        if mouseX > (213 * 2) and mouseY > (160 * 2):
            row = 2
            col = 2

        try:
            #if nothing is there then set character else nothing happens
            if self.game_board[row][col] == None: 
                if row != None and col != None:
                    if mouse_click[0] == True:
                        self.game_board[row][col] = self.turn
                        if self.turn == 'x': self.turn = 'o'
                        elif self.turn == 'o': self.turn = 'x'
        except TypeError:
            #nothing has been placed so nothing should happen
            return



    def drawGameBoard(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.board_img, (0, 0))


        '''
            * 640 / 3 = 213.333
            * 480 / 3 = 160
        '''
        
        for row in range(len(self.game_board)):
            for col in range(len(self.game_board[row])):
                if self.game_board[row][col] != None:
                    
                    #determine whether to draw X or O
                    if self.game_board[row][col] == 'x':
                        draw = self.x
                    if self.game_board[row][col] == 'o':
                        draw = self.o

                    #determine where mouse clicked
                    if row == 0:
                        pady = 40
                    if row == 1:
                        pady = 40 + 160
                    if row == 2:
                        pady = 40 + (160 * 2)
                    if col == 0:
                        padx = 60
                    if col == 1:
                        padx = 60 + 213
                    if col == 2:
                        padx = 60 + (213 * 2)

                
                    self.screen.blit(draw, (padx, pady))

        pygame.display.flip()
        
    def check_win(self) -> bool:
        #checking for winner along rows
        for row in range(0, 3):
            if self.game_board[row][0] == self.game_board[row][1] == self.game_board[row][2] and self.game_board[row][0] is not None:
                self.winner = self.game_board[row][0]
                break
        #checking for winner down columns
        for col in range(0, 3):
            if self.game_board[0][col] == self.game_board[1][col] == self.game_board[2][col] and self.game_board[0][col] is not None:
                self.winner = self.game_board[0][col]
                break
        #diagonal left -> right
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2]:
            self.winner = self.game_board[0][0]
        #diagonal right -> left
        if self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0]:
            self.winner = self.game_board[0][2]

        nNone = 0 # if winner is none and amount of None in board is 0 then no player has won the game
        if self.winner == None:
            for row in range(len(self.game_board)):
                for col in range(len(self.game_board[row])):
                    if self.game_board[row][col] == None:
                        nNone += 1
            if nNone == 0:
                self.draw = True

    def win(self):
        #pauses the game until enter key is pressed
        finished = False
        while not finished:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    finished = True
                if keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill((255, 255, 255))
            font = pygame.font.SysFont("Ariel", 50, True)
            if self.draw:
                text = 'It\'s a draw!'
            elif self.win:
                text = str(self.winner) + ' wins!!! :)'
            text2 = "Press enter to play again!!"
            text_surface = font.render(text, True, (0, 0, 0))
            text2_surface = font.render(text2, True, (0, 0, 0))

            self.screen.blit(text_surface, (195, 100))
            self.screen.blit(text2_surface, (70, 147))
            
            pygame.display.flip() #update display

        self.clear()

        return
    
    def clear(self):
        self.game_board = [
            [None, None, None], 
            [None, None, None], 
            [None, None, None]
        ]

        self.winner = None
        self.draw = None

        return


    def main_menu(self):
        font = pygame.font.SysFont("Ariel", 50, True)
        title = "Noughts & Crosses"
        option1 = "Start"
        option2 = "Exit"
        #surfaces
        title_surface = font.render(title, True, (0, 0, 0))
        option1_surface = font.render(option1, True, (0, 0, 0))
        option2_surface = font.render(option2, True, (0, 0, 0))
        #rect determine what's clicked
        option1_rect = option1_surface.get_rect(topleft=(268, 175))
        option2_rect = option2_surface.get_rect(topleft=(268, 222))

        self.screen.fill((255, 255, 255))
        #pygame.draw.rect(self.screen, (0, 255, 255), option1_rect)
        self.screen.blit(title_surface, (140, 128))
        self.screen.blit(option1_surface, (268, 175))
        #pygame.draw.rect(self.screen, (0, 255, 255), option2_rect)
        self.screen.blit(option2_surface, (268, 222))
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.clock.tick(60)

            mouseX, mouseY = pygame.mouse.get_pos()
            mouse_keys = pygame.mouse.get_pressed()
            if mouse_keys[0]: #left click
                if option1_rect.collidepoint((mouseX, mouseY)):
                    #without calling pause, an X is place on the position of the mouse after clicking "Start"
                    # ^ upon further inspection this still happens sometimes 
                    self.pause() 
                    self.main_loop()
                if option2_rect.collidepoint((mouseX, mouseY)):
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()

    def pause(self):
        #pauses the program for a short time
        i = 1
        while True:
            for event in pygame.event.get():
                i += 1
                if i >= 2:
                    return
                    

    def main_loop(self):
        while True:
            self.clock.tick(60) #sets framerate to 60fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
            self.drawGameBoard()
            mouse_keys = pygame.mouse.get_pressed()
            if mouse_keys[0] == True: #right or left click
                self.user_click(mouse_keys)
            
                winner = self.check_win()
                if self.winner != None or self.draw != None:
                    self.win()


if __name__ == '__main__':
    game = Game()
