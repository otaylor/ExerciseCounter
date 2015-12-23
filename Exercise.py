import time
import winsound

#Sound to make 
def RepComplete (BeepTime):    
    winsound.Beep(1000, BeepTime)

#Run per repetition
def Repetition (Duration):
    print "Rep in progress"
    RepComplete(300)
    time.sleep(Duration)

#Convert input to float
def ConvertToFloat (Convert):
    Int = int(Convert)
    Float = float(Int)
    return Float


print "This program allows you to run a series of repetitions"
Reps = raw_input("Please enter the number of repetitions: ")
Duration = raw_input("Please enter the duration of the repetitions in seconds: ")

Reps = ConvertToFloat(Reps)
Duration = ConvertToFloat(Duration)

#Give the user time to get into position
print "Please get into position"
time.sleep(5)

#Loop for number of repetitions
RepetitionsCompleted = int(1)
while RepetitionsCompleted <= Reps:
    print 'Rep number: ', RepetitionsCompleted
    Repetition (Duration)
    RepetitionsCompleted = RepetitionsCompleted + 1

print "Specificed repetitions completed."
RepComplete(800)


