import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Load snake and food images
snake_img = pygame.image.load("snake.png")
food_img = pygame.image.load("food.png")

# Snake initial position and speed
snake = [(5, 5)]
snake_direction = (1, 0)
snake_speed = 10

# Food initial position
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Snake movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_direction = (0, -1)
    if keys[pygame.K_DOWN]:
        snake_direction = (0, 1)
    if keys[pygame.K_LEFT]:
        snake_direction = (-1, 0)
    if keys[pygame.K_RIGHT]:
        snake_direction = (1, 0)

    # Update snake position
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # Check for collisions with the food
    if snake[0] == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Check for collisions with the wall
    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= GRID_HEIGHT
    ):
        running = False

    # Draw everything
    window.fill(WHITE)
    for segment in snake:
        window.blit(snake_img, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE))
    window.blit(food_img, (food[0] * GRID_SIZE, food[1] * GRID_SIZE))
    pygame.display.update()

    # Control game speed
    pygame.time.delay(1000 // snake_speed)

# Quit Pygame
pygame.quit()

