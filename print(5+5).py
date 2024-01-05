import pygame
import random

# 初始化Pygame
pygame.init()

# 設置遊戲視窗
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fruit Catcher")

# 定義顏色
white = (255, 255, 255)
red = (255, 0, 0)

# 定義遊戲元素
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size

fruit_size = 30
fruit_speed = 5

# 初始化玩家的垂直位置
player_y = height - 2 * player_size

# 創建水果
def create_fruit():
    fruit_x = random.randint(0, width - fruit_size)
    fruit_y = 0
    return fruit_x, fruit_y

# 遊戲主循環
clock = pygame.time.Clock()
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += 5
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= 5
    if keys[pygame.K_DOWN] and player_y < height - player_size:
        player_y += 5

    screen.fill(white)

    # 移動水果
    fruit_y += fruit_speed
    if fruit_y > height:
        fruit_x, fruit_y = create_fruit()
        score -= 1  # 減分

    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))

    pygame.draw.ellipse(screen, red, (fruit_x, fruit_y, fruit_size, fruit_size))

    # 檢查是否接到水果
    if (
        player_x < fruit_x < player_x + player_size
        and player_y < fruit_y < player_y + player_size
    ):
        fruit_x, fruit_y = create_fruit()
        score += 1  # 加分

    # 顯示分數
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, red)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

# 退出遊戲
pygame.quit()
