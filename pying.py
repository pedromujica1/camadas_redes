from ping3 import ping
from tqdm import tqdm

maq_all = {}
maq_lig = {}

destino = '192.168.246.'

tout = 0.1

for i in tqdm(range(1, 255)):
    
    destino2 = destino
    destino2 += str(i)

    #print(destino2)

    if ping(destino2, timeout = tout):
        maq_all[destino2] = "On!"
        maq_lig[destino2] = "On!"
    else: maq_all[destino2] = "Off!"

print(maq_all)
for i in maq_all: 
  print(i)
print(maq_lig)
