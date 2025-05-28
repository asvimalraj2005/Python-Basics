# Pattern matching sequence. 
# Match/case usage 
# Below is an simple match case function handling sequences. Imagine you are designing a robot that accepts 
# commands sent as sequence of words and numbers like Deeper 440 3, After splitting into parts and parsing the number 
# you have a message like ['Deeper',440,3]. How could use a method like this to handle such messages 
# 
# Method from an imaginary robot class 
def handle_command(self, message):
    match message:
        case ['Deeper', frequency, times]:
            self.beep(times, frequency)
        case ['Neck', angle]:
            self.rotate_neck(angle)
        case ['LED', ident, intensity]:
            self.leds[ident].set_brightness(intensity)
        case ['LED', ident, red, green, blue]:
            self.leds[ident].set_color(red, green, blue)
        case _:
            raise InvalidCommand(message)
robot=MyRobot()
robot.handle_command(['Deeper',440,3])
robot.handle_command(['LED','eye',255,0,0])
robot.handel_command(['Neck',45])
robot.handle_command(['Unknown',123])
        