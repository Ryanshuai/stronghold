from pynput import keyboard, mouse
import time
import threading

import pynput.mouse

m_control = mouse.Controller()
k_control = keyboard.Controller()


class PressThread(threading.Thread):
    def __init__(self, threadID, name, delay, key):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.key = key
        self.res = False

    def run(self):
        self.res = on_press_(self.key)


def on_press_(key):
    if hasattr(key, 'char') and key.char == 'w':
        print("w")
        pos = m_control.position
        m_control.position = (903, 1376)
        m_control.press(mouse.Button.left)
        time.sleep(0.01)
        m_control.release(mouse.Button.left)
        time.sleep(0.01)
        m_control.position = pos
        return False

    elif hasattr(key, 'char') and key.char == 'f':
        print("f")
        pos = m_control.position
        m_control.position = (986, 1417)
        m_control.press(mouse.Button.left)
        time.sleep(0.01)
        m_control.release(mouse.Button.left)
        time.sleep(0.01)
        m_control.position = pos
        return False

    elif key == keyboard.Key.space:
        print("space")
        m_control.press(mouse.Button.left)
        time.sleep(0.05)
        m_control.release(mouse.Button.left)
        return True

    elif key == keyboard.Key.esc:
        k_control.press(keyboard.Key.esc)
        time.sleep(0.02)
        k_control.release(keyboard.Key.esc)
        return False

    elif key == keyboard.Key.tab:
        k_control.press(keyboard.Key.tab)
        time.sleep(0.02)
        k_control.release(keyboard.Key.tab)
        return False


def on_press(key):
    pt = PressThread(1, "PressThread", 0.0001, key)
    pt.start()
    return False


while True:
    with keyboard.Listener(
            suppress=True,
            on_press=on_press,
    ) as listener:
        listener.join()
