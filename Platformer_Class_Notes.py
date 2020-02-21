'''
Created on Feb 19, 2020

@author: rdyoung
'''
import pygame
import random

pygame.init() # Pygame constructor

screen_width = 800 # The width of my window
screen_height = 600 #The height of my window

screen = pygame.display.set_mode((screen_width, screen_height)) #This makes a new screen for pygame

backgrounds = [] # A Blank List To Hold Our Backgrounds
for i in range(15):
    backgrounds.append(pygame.image.load("Backgrounds\\BG(" + str(i+1) + ").png")) #Adds all the background pics
    backgrounds[i] = pygame.transform.scale(backgrounds[i], (800,600)) #Sizes the backgrounds for the window

characters = [] # A Blank List To Hold Our Characters
for i in range(10):
    characters.append(pygame.image.load("Character\\Walk (" + str(i+1) + ").png")) #Adds all the character pics
    characters[i] = pygame.transform.scale(characters[i], (50,50)) #Sizes the characters to 50px

clock = pygame.time.Clock() # gives us the ability to have a refresh rate 

def place_Character(c, x,y): #Function that takes current picture number, x position and y position of character
    screen.blit(characters[c], (x,y)) #This places the current character at location (x,y) 

class Reaper:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        self.walk_Count = 0
        self.walk_Images = self.set_Walk_Images()
    
    def set_Walk_Images(self):
        images = []
        for i in range(10):
            if i < 10:
                images.append(pygame.image.load("Character\\1_TROLL\\Troll_01_1_WALK_00" + str(i) + ".png")) #Adds all the character pics
            else:
                images.append(pygame.image.load("Character\\Reaper\\Walking\\0_Reaper_Man_Walking_0" + str(i) + ".png")) 
            images[i] = pygame.transform.scale(images[i], (100,100)) #Sizes the characters to 50px
        return images
    
    def place_Reaper(self):
        screen.blit(self.walk_Images[self.walk_Count], (self.x,self.y))
        self.walk_Count += 1
        if self.walk_Count >= len(self.walk_Images):
            self.walk_Count = 0
    
    def move_Reaper(self, curr_x):
        if self.x > curr_x:
            self.x -= random.randint(0,3)
        elif self.x < curr_x:
            self.x += random.randint(0,3)
        self.place_Reaper()

reapers = [] 
for i in range(0,5):
    reapers.append(Reaper( random.randint(0, 800) ,500))

def game():
    exit_Game = False # We will use this boolean to end pygame
    curr_x = (screen_width * .1) #This will be the starting x of the bee
    x_key_mod = 0 # We will use this to move the bee along the x axis 
    bg_Count = 0 #We will use this for current background
    char_Count = 0 #We will use this for current character
    
    while not exit_Game: #As long as our exit_game boolean is not true keep running
        for event in pygame.event.get(): #For every event that occurs (key presses, mouse moves, key releases ...)
            if event.type == pygame.QUIT: #If the red check is clicked on the pygame window 
                exit_Game = True
            elif event.type == pygame.KEYDOWN: # has a key been pressed
                if event.key == pygame.K_LEFT or event.key == pygame.K_a: #has the left arrow or a key been pressed
                    x_key_mod = -5 # set the x mod variable to moving left on the x axis 
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d: #has the right arrow or d key been pressed
                    x_key_mod = 5 # set the x mod variable to moving left on the x axis 
            elif event.type == pygame.KEYUP: # has a key been released
                if event.key == pygame.K_LEFT or event.key == pygame.K_a: #has the left arrow or a key been pressed
                    x_key_mod = 0 # set the x mod variable to not moving left on the x axis 
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d: #has the right arrow or d key been pressed
                    x_key_mod = 0 # set the x mod variable to not moving left on the x axis  
            
        curr_x += x_key_mod # adds the x movement

        if curr_x > screen_width - 50 or curr_x < 0 : #Has our character image left the screen? 
            if curr_x < 0: #    Has our character gone left off the screen?
                bg_Count -= 1 #Go back to the previous background
                curr_x = 730 #Move the character to the far right of the page
                reapers.append(Reaper( random.randint(0, 800) ,500))
            elif curr_x > 780: # Has our character gone right off the screen?
                bg_Count += 1 #look at the ext background
                curr_x = 20 #Move the character to the far left of the page
                reapers.append(Reaper( random.randint(0, 800) ,500))
            if bg_Count > 14: # Is our background count beyond the len of backgrounds
                bg_Count = 0 #set the background to the min value of all backgrounds
            elif bg_Count < 0: # Is background count below 0
                bg_Count = 14 #Set the background to the top value of all backgrounds
        screen.blit(backgrounds[bg_Count], (0,0)) #paint the background on the screen 
        
        if x_key_mod > 0:#is the character moving forward?
            char_Count += 1 #Choose next character picture
            if char_Count == len(characters): # Have we gone beyond all character pictures?
                char_Count = 0  #Go back to the beginning of the character pictures
        elif x_key_mod < 0: #is the character moving backward? 
            char_Count -= 1 #Choose the previous character picture
            if char_Count < 0: ## Are we below all possible character pictures
                char_Count = len(characters)  - 1   #Go back to the top value of character pictures
        place_Character(char_Count,curr_x,500) # paints the bee
        
        for r in reapers: #Selects all reapers in the array
            r.move_Reaper(curr_x) # moves all reapers to the character 
            
        pygame.display.update() # updates the visual display
        clock.tick(20) # sets the fps 
            
game()