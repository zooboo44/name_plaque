import os
import board
import neopixel
from dotenv import load_dotenv

ORDER = os.getenv("led_order")

presence_color_matrix = {
    "Available" : "GREEN",
    "Busy" : "RED",
    "DoNotDisturb" : "RED",
    "Away" : "YELLOW",
    "BeRightBack" : "YELLOW",
    "Offline" : "OFF",
    "OutOfOffice" : "PURPLE",
}

COLOR = {
    "RED" : (255,0,0),
    "GREEN" : (0,255,0),
    "YELLOW" : (255,255,0),
    "PURPLE" : (125,69,119),
    "OFF" : (0,0,0)
}

class LedControl():
    def __init__(self, env_file=".env"):
        load_dotenv(env_file)

        self.led_length = int(os.getenv("LED_LENGTH"))
        self.led_pin = int(os.getenv("LED_PIN"))
        self.led_brightness = float(os.getenv("LED_BRIGHTNESS"))

        self.strip = (neopixel.NeoPixel(
            board.D18,
            self.led_length,
            self.led_brightness,
            auto_write=True,
            pixel_order=neopixel.GRBW
        ))

    def set_color(self, color):
        led_color = presence_color_matrix[color]
        print(led_color)
        print(COLOR[led_color])
        self.strip.fill(COLOR[led_color])