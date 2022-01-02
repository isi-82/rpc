from pypresence import Presence
import time

rpc_text = input("Your RPC Text : ")
client_id = "[Your Client ID]"
RPC = Presence(client_id)

RPC.connect()
RPC.update(state="RPC starting...")
print("RPC starting...")

while True: 
    time.sleep(15) 
    RPC.update(state=rpc_text)
