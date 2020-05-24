# Obtained from https://www.edureka.co/blog/snake-game-with-pygame/

import pygame, sys,time,random
pygame.init()
size = width, height =600,400

black = (0,0,0)
yellow= (255,255,102)
white = (255,255,255)
blue  = (50,153,213)
red   = (213,50,80)
green = (0,255,0)

screen = pygame.display.set_mode(size)
pygame.display.update()
pygame.display.set_caption('Snake game by Sonia')
	
clock = pygame.time.Clock()

snake_speed = 7
snake_block = 20

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(screen, black, [x[0],x[1],snake_block,snake_block])

def message(txt, color):
	textsurface = font_style.render(txt, True, color)
	screen.blit(textsurface, (width/3, height/3))
def your_score(score):

	value = score_font.render("Your score: "+str(score),True,yellow)
	screen.blit(value,[0,0])
def gameloop():
	game_over=False
	game_close =False
	
	x1= width/2
	y1 = height/2

	x1_change = 0
	y1_change = 0

	snake_list=[]
	length_of_snake = 1

	foodx = round(random.randrange(0,width - snake_block)/float(snake_block))*float(snake_block)
	foody = round(random.randrange(0,height - snake_block)/float(snake_block))*float(snake_block)
	print(foodx,foody)
	
	movr, movl, movd, movu = False, False, False, False

	delaytime=0
	keydown_flag = True

	while not game_over:
		while game_close == True:
			screen.fill(blue)
			message("You lost!\n Press Q_Quit or C-Play again",red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					if event.key == pygame.K_c:
						gameloop()
					

		for event in pygame.event.get():
			print("entered keydown: "+str(keydown_flag))
			if event.type == pygame.QUIT:
				game_over=True
			if event.type == pygame.KEYDOWN and keydown_flag == True:
				starttime = pygame.time.get_ticks()
				keydown_flag = False
				if event.key == pygame.K_LEFT:
					if movr == False:						
						x1_change= -snake_block
						y1_change = 0
						movl = True
						movr, movd, movu = False, False, False
						pygame.time.wait(delaytime)
				elif event.key == pygame.K_RIGHT:
					if movl == False:
						x1_change = snake_block
						y1_change = 0
						movr = True
						movl, movu, movd = False, False, False
						pygame.time.wait(delaytime)
				elif event.key == pygame.K_UP:
					if movd == False:
						x1_change = 0
						y1_change = -snake_block
						movu = True
						movd, movr, movl = False, False, False
						pygame.time.wait(delaytime)
				elif event.key == pygame.K_DOWN:
					if movu == False:
						x1_change = 0
						y1_change = snake_block
						movd = True
						movu, movr, movl = False, False, False
						pygame.time.wait(delaytime)
			if keydown_flag == False and pygame.time.get_ticks()-starttime >=10:
				keydown_flag = True
		if x1<0 or y1<0 or x1>=width or y1>=height:
			print("out of boundries")
			game_close=True
							
		x1 += x1_change
		y1 += y1_change
		
		screen.fill(blue)
		pygame.draw.rect(screen, green,[foodx,foody,snake_block,snake_block])
		snake_head = []
		snake_head.append(x1)
		snake_head.append(y1)
		snake_list.append(snake_head)
		if len(snake_list) > length_of_snake:
			del snake_list[0]

		for x in snake_list[:-1]:
			if x==snake_head:
				game_close = True
		our_snake(snake_block, snake_list)
		your_score(length_of_snake-1)

		pygame.display.update()

		if x1== foodx and y1==foody:
			foodx = round(random.randrange(0,width - snake_block)/float(snake_block))*float(snake_block)
			foody = round(random.randrange(0,height - snake_block)/float(snake_block))*float(snake_block)
			length_of_snake +=1
			print("Yummy!!")
		clock.tick(snake_speed)

	pygame.quit()
	quit()

gameloop()
