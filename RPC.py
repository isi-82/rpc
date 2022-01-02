# Import's
from pypresence import Presence
import time

# Variabeln
rpc_text = input("RPC Text: ")
client_id = "client_id"
RPC = Presence(client_id)

# Start
RPC.connect()
RPC.update(state="RPC startet...")
print("RPC startet!")

# Loop
while True:
  time.sleep(15)
  RPC.update(state=rpc_text)
