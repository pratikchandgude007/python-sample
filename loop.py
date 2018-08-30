from omxplayer import OMXPlayer
from time import sleep


args=['--no-osd' ]
files = ['2.m4v', '3.m4v', '4.m4v', '5.m4v']

durations = []
players = []

print('Initialising')
for f in files:
        #OMXPlayer per file
        players.append(OMXPlayer(f, args=args))

        #get duration of each file
        durations.append(players[len(players)-1].duration())

#just in case
sleep(2)
print('Playing')

#loop 5 times
for cnt in range(0,5):
    #play each file
    for i in range(0,len(players)):
        players[i].set_position(0.0)
        players[i].play()
        
        # raspberry pi 2
        #sleep(durations[i] - 0.5)
        
        # raspberry pi 1
        sleep(durations[i] - 1.5)
        
        players[i].pause()


print('Quiting')
for p in players:
    p.quit()