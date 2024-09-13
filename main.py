import pygame
import sys
import os
import yaml
import win32gui
import win32con

pygame.init()

# Load configuration
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

background_color = tuple(config.get("background_color", [255, 165, 0]))
font_color = tuple(config.get("font_color", [255, 255, 255]))
direction = config.get("direction", "left")
ticker_text = config.get("ticker_text", "Default Ticker Text")
position = config.get("position", "bottom")

# Get the screen dimensions
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

# Set ticker height to 1/8th of the screen height
ticker_height = int(screen_height / 8)

# Set up a window with no frame
screen = pygame.display.set_mode((screen_width, ticker_height), pygame.NOFRAME)
pygame.display.set_caption("News Channel Ticker")

# Determine the position of the ticker
y_position = 0 if position == "top" else screen_height - ticker_height
os.environ['SDL_VIDEO_WINDOW_POS'] = f"0,{y_position}"

# Get the window handle and set it to be always on top
hwnd = pygame.display.get_wm_info()['window']
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, y_position, screen_width, ticker_height, 0)

# Set font size to ticker_height - 2
font = pygame.font.Font(None, ticker_height - 2)

def create_ticker(text, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if direction == "left":
        text_rect.left = screen_width
    else:
        text_rect.right = 0
    text_rect.centery = ticker_height // 2  # Center the text vertically
    return text_surface, text_rect

def main():
    ticker_surface, ticker_rect = create_ticker(ticker_text, font_color)
    
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill(background_color)
        
        # Display the scrolling ticker text
        screen.blit(ticker_surface, ticker_rect)
        if direction == "left":
            ticker_rect.move_ip(-2, 0)
            if ticker_rect.right < 0:
                ticker_rect.left = screen_width
        else:
            ticker_rect.move_ip(2, 0)
            if ticker_rect.left > screen_width:
                ticker_rect.right = 0
        
        # Update the display
        pygame.display.flip()
        clock.tick(120)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()