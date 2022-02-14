#Calculates at what time an experiment ended based on the start time and time[3] elapsed since the start


hour, minutes, seconds=[int(x) for x in input("When did the experiment start? Insert in the format hh:mm:ss ").split(':')]
elapsedTime=int(input("How many seconds did the experiment take? "))
day=0
time=[day, hour, minutes, seconds, elapsedTime]

def main(time):
    if time[4]>=3600:
        FixTimeForMoreThan3600(time)
    if time[4] >= 60:
        FixTimeForMoreThan60(time)
    if time[4] < 60:
        FixTimeForLessThan60(time)
    ShowTime(time)

def FixTimeForMoreThan3600(time):
    time[1]+=(time[4]//3600)
    time[2]+=(time[4]%3600)//60
    time[3]+=((time[4]%3600)%60)%60
    while time[2]>60 or time[3]>60:
        if time[2]>60:
            time[1]+=time[2]//60
            time[2]-=(time[2]//60)*60
        if time[3]>60:
            time[2]+=time[3]//60
            time[3]-=(time[3]//60)*60
    if time[1]>=24:
        time[0]+=time[1]//24
        time[1]-=time[0]*24

def FixTimeForMoreThan60(time):
    time[2]+=(time[4]%3600)//60
    time[3]+=(time[4]%3600%60)//60
    while time[2]>60 or time[3]>60:
        if time[2]>60:
            time[1]+=time[2]//60
            time[2]-=(time[2]//60)*60
        if time[3]>60:
            time[2]+=time[3]//60
            time[3]-=(time[3]//60)*60
    if time[1]>=24:
        time[0]+=time[1]//24
        time[1]-=time[0]*24

def FixTimeForLessThan60(time):
    time[3]+=time[4]
    while time[2]>60 or time[3]>60:
        if time[2]>60:
            time[1]+=time[2]//60
            time[2]-=(time[2]//60)*60
        if time[3]>60:
            time[2]+=time[3]//60
            time[3]-=(time[3]//60)*60
    if time[1]>=24:
        time[0]+=time[1]//24
        time[1]-=time[0]*24

def ShowTime(time):   
    print(f"The experiment ended at {time[1]}:{time[2]}:{time[3]} (plus {time[0]} days from the start)")   

if __name__ == '__main__':
    main(time)