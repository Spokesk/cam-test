led = False

# 1. Using the led variable above create a function called "led_state" that writes
#   to the console whether the LED is "ON" or "OFF" in a human readable way.

def led_state():
    if led == False:
        return "OFF"
    else:
        return "ON"


# 2. Using the led variable above write a function named "toggle_led" that toggles the led.
#       If the state is OFF turn it ON and if the state is ON it turns OFF.

def toggle_led():
    global led
    if led == False:
        led = True
    else:
        led = False



# 3. Using the two functions you created, "led_state" and "toggle_led",
#   print the initial led state and
#   with a while loop do the following 5 times:
#       - toggle the led
#       - print the new led state

# ( HINT: The led status should only be printed 6 times in total.
#           It starts OFF and ends being ON. )

# LED: OFF
# LED: ON
# LED: OFF
# LED: ON
# LED: OFF
# LED: ON

def blink_led():
    global led
    led_state()
    loop = 5
    while loop != 0:
        loop = loop - 1
        print("LED: " + str(led_state()))
        toggle_led()
        
blink_led()



                                        