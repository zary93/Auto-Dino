import math
import keyboard
import pyautogui as gui
import time


def get_pixel(image, x, y):
    # Function to get the pixel color at a specific (x, y) coordinate in the image
    px = image.load()
    return px[x, y]


def start():
    # Initial setup and waiting for 3 seconds before starting
    x, y, width, height = 200, 700, 610, 380
    jumping_time = 0
    last_jumping_time = 0
    current_jumping_time = 0
    last_interval_time = 0
    y_search1, y_search2, x_start, x_end = 220, 230, 380, 400
    y_search_for_bird = 175
    time.sleep(3)

    while True:
        if keyboard.is_pressed('q'):
            # Break the loop if 'q' is pressed
            break

        # Capture the screenshot of the dinosaur game area
        dino_img = gui.screenshot(region=(x, y, width, height))
        dino_img.save('dino.jpg')

        # Get the background color (assumed to be at (10, 370))
        bg_color = get_pixel(dino_img, 10, 370)

        # Check for obstacles and bird and perform actions accordingly
        for z in reversed(range(x_start, x_end)):
            if get_pixel(dino_img, z, y_search1) != bg_color or get_pixel(dino_img, z, y_search2) != bg_color:
                # Jump if an obstacle is detected
                keyboard.press("up")
                jumping_time = time.time()
                current_jumping_time = jumping_time
                break
            if get_pixel(dino_img, z, y_search_for_bird) != bg_color:
                # Duck if a bird is detected
                keyboard.press("down")
                time.sleep(0.4)
                keyboard.release("down")
                break

        # Adjust the search area dynamically based on the time intervals between jumps
        interval_time = current_jumping_time - last_jumping_time
        if last_interval_time != 0 and math.floor(interval_time) != math.floor(last_interval_time):
            x_end += 7
            if x_end >= width:
                x_end = width

        last_jumping_time = jumping_time
        last_interval_time = interval_time


start()

