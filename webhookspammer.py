"""
Credits: Webhook spammer made by andy
Discord: !ANDY!#0001
Github: AndyOnTop
"""
print("""
 _____ _                 _            _    _      _     _   _             _          _____                                           
/  ___(_)               | |          | |  | |    | |   | | | |           | |        /  ___|                                          
\ `--. _ _ __ ___  _ __ | | ___      | |  | | ___| |__ | |_| | ___   ___ | | __     \ `--. _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 `--. \ | '_ ` _ \| '_ \| |/ _ \     | |/\| |/ _ \ '_ \|  _  |/ _ \ / _ \| |/ /      `--. \ '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
/\__/ / | | | | | | |_) | |  __/     \  /\  /  __/ |_) | | | | (_) | (_) |   <      /\__/ / |_) | (_| | | | | | | | | | | |  __/ |   
\____/|_|_| |_| |_| .__/|_|\___|      \/  \/ \___|_.__/\_| |_/\___/ \___/|_|\_\     \____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                  | |                                                                     | |                                        
                  |_|                                                                     |_|                                        
                                                    Made by Andy
                                                  Github: AndyOnTop
""")

#imports
from dhooks import Webhook
import time

#prompts
message = input("What do you want to spam?: ")
webhookurl = Webhook(input("Enter webhook: "))
delay = input("Enter a delay: ")

#webhook spamming time
while True:
    time.sleep(1)
    webhookurl.send(message)
    print("Sent.")