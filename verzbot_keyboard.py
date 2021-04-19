from verzbot import thugger
import keyboard
import clipboard


#recorded = keyboard.record(until='esc')
# Then replay back at three times the speed.

#print(recorded)
keyboard.add_hotkey('pause', lambda: clipboard.copy(thugger()))
