from pypresence import Presence
import time

anime = input("What anime are you Watching? : ")
client_id = "921866924533616760"
RPC = Presence(client_id)

RPC.connect()
RPC.update(state="RPC starting...")
print("RPC starting...")

while True: 
    time.sleep(15) 
    RPC.update(state="Is wachting anime...")
    time.sleep(15)
    RPC.update(state=f"Anime: {anime}")