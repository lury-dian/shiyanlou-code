#! /usr/bin/env python3
sticks = 21
print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("whoever will take the last stick will loose")

while True:
    print("Sticks left: ", sticks)
    sticks_taken = int(input("Take sticks(1-4): "))
    if sticks == 1:
        print("You took the last stick, you lose!")
        break
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong chioce")
        continue
    print("Computer took: ",(5-sticks_taken))
    sticks -=5
