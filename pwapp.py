import streamlit as st
import random

st.title("PW demo app")


col1, col2 = st.columns(2)

if "inventory" not in st.session_state:
    st.session_state.inventory = []
if "totalPulledCount" not in st.session_state:
    st.session_state.totalPulledCount = 0
if "hard_pity" not in st.session_state:
    st.session_state.hard_pity = 0
if "grassCount" not in st.session_state:
    st.session_state.grassCount = 0
if "daily_hours_off" not in st.session_state:
    st.session_state.daily_hours_off = 0

def clear_inv():
    st.session_state.inventory = []
    st.session_state.totalPulledCount = 0

#col1: data input

# targetScreenTime = col1.text_input("target screen time by the end of 4 weeks")
# pastScreenTime = col1.text_input("actual average screen time from phone for the past week")

# col1.write("your target is: " + str(targetScreenTime) + " hours")
# col1.write("for the last week, your screen time was: " + str(pastScreenTime) + " hours")

# col1.html("<hr>") # draws a line

# todayScreenTime = col1.text_input("screen time by the end of today")
# col1.write("today's screen time: " + str(todayScreenTime))
# col1.write("past screen time: " + str(pastScreenTime))

# if col1.button("tabulate grass"):
#     # if todayScreenTime is lower than pastScreenTime, earn that much grass. otherwise grass remains the same
#     if pastScreenTime and todayScreenTime:
#         todayScreenTime, pastScreenTime = int(todayScreenTime), int(pastScreenTime)
#         if todayScreenTime <= pastScreenTime:
#             col1.write("congrats! your screen time today is under your past screen time.")
#             st.session_state.grassCount += (pastScreenTime - todayScreenTime)
#             col1.write("you now have " + str(st.session_state.grassCount) + " grass!")
#         elif todayScreenTime > pastScreenTime:
#             col1.write("please do better... ")

if col1.button("1 hour has passed with device off", use_container_width=True): 
    st.session_state.grassCount += 1
    st.session_state.daily_hours_off += 1
if col1.button("5 hours have passed with device off", use_container_width=True): 
    st.session_state.grassCount += 5
    st.session_state.daily_hours_off += 5
if col1.button("10 hours have passed with device off", use_container_width=True): 
    st.session_state.grassCount += 10
    st.session_state.daily_hours_off += 10
if col1.button("15 hours have passed with device off", use_container_width=True): 
    st.session_state.grassCount += 15
    st.session_state.daily_hours_off += 15
if col1.button("1 day has passed with device off", use_container_width=True): 
    st.session_state.grassCount += 24
    st.session_state.daily_hours_off += 24

if col1.button("progress to next day", use_container_width=True):
    st.session_state.daily_hours_off = 0

# assuming one full day has passed
if st.session_state.daily_hours_off >= 10 and st.session_state.daily_hours_off <= 24:
    col1.write("congratulations! you spent " + str(st.session_state.daily_hours_off) + " hours off your device today!")
elif st.session_state.daily_hours_off < 10:
    col1.write("you spent " + str(st.session_state.daily_hours_off) + " hours off your device today.")
elif st.session_state.daily_hours_off > 24:
    col1.write("error! max 24 hours in a day! total hours input was " + str(st.session_state.daily_hours_off))



command = col1.chat_input("admin debug command window")
if command: 
    if command == "reset all" or command == "reset":
        st.session_state.grassCount = 0
        st.session_state.daily_hours_off = 0
        clear_inv()
        st.session_state.hard_pity = 0
    elif command == "reset grass":
        st.session_state.grassCount = 0
        st.session_state.daily_hours_off = 0
    elif command.startswith("give grass"):
        grasscommand = command.split()
        final_grass = grasscommand[2] if len(grasscommand) > 2 else None
        st.session_state.grassCount += int(final_grass)
    else:
        col1.write("invalid command")


# col2: the gacha simulator

col2.header("gacha pull simulator")  

gachapool = ["dragonfly","squirrel","ladybug","sparrow","butterfly","rabbit","dog","bee","caterpillar","ant"]
gachaLen = len(gachapool)
limited = "[RARE] gnome"
standard = "[RARE] stickbug"
guaranteed_status = 0
max_pity = 80
grass_per_pull = 1

def gacha_pull():
    if st.session_state.hard_pity < max_pity: # normal pull, not hard pity
        if random.randint(1,100) == 100: # 1% chance of pulling a rare
            gacha_result = random.choice([standard, limited]) # 50/50 between standard and limited
            col2.write("you pulled " + gacha_result + " at " + str(st.session_state.hard_pity) + " pity!") # display congratulatory message
            st.session_state.hard_pity = 0 # resets hard pity
        else: # normal pull, no rare
            gacha_result = gachapool[random.randint(0, gachaLen-1)] # picks between non-rare list
            st.session_state.hard_pity += 1 
    else: # hard pity reached
        gacha_result = random.choice([standard, limited]) # 50/50 between standard and limited
        col2.write("you pulled " + gacha_result + " at max pity, which is " + str(max_pity))
        st.session_state.hard_pity = 0 
    st.session_state.totalPulledCount += 1
    st.session_state.inventory.append(gacha_result)
  



def pull_for_amt(pullAmount):
    for i in range (pullAmount):
        gacha_pull()
    col2.write(f"you pulled {pullAmount} times")

def view_gacha_stats():
    categorisedCount = {}
    for element in st.session_state.inventory:
        if element in categorisedCount:
            categorisedCount[element] += 1
        else:
            categorisedCount[element] = 1
    col2.write("total pull count is " + str(st.session_state.totalPulledCount))
    col2.write("individual count:")
    col2.write(categorisedCount)
    col2.write("pity: " + str(st.session_state.hard_pity))

def check_inv():
    col2.write(st.session_state.inventory)


# display in col2
if st.session_state.grassCount >= grass_per_pull:
    if col2.button("hide dialogue"):
        col2.write()

if st.session_state.grassCount >= grass_per_pull:
    if col2.button("pull 1"):
        gacha_pull()
        col2.write("you pulled 1 time")
        st.session_state.grassCount -= grass_per_pull

if st.session_state.grassCount >= 10*grass_per_pull:
    if col2.button("pull 10"):
        pull_for_amt(10)
        st.session_state.grassCount -= 10*grass_per_pull

if st.session_state.grassCount >= 100*grass_per_pull:
    if col2.button("pull 100"):
        pull_for_amt(100)
        st.session_state.grassCount -= 100*grass_per_pull

if st.session_state.grassCount >= 1000*grass_per_pull:
    if col2.button("pull 1000"):
        pull_for_amt(1000)
        st.session_state.grassCount -= 1000*grass_per_pull

if st.session_state.grassCount >= 10000*grass_per_pull:
    if col2.button("pull 10000"):
        pull_for_amt(10000)
        st.session_state.grassCount -= 10000*grass_per_pull

if st.session_state.grassCount >= 100000*grass_per_pull:
    if col2.button("pull 100000"):
        pull_for_amt(100000)
        st.session_state.grassCount -= 100000*grass_per_pull

if st.session_state.grassCount >= 1000000*grass_per_pull:
    if col2.button("pull 1000000"):
        pull_for_amt(1000000)
        st.session_state.grassCount -= 1000000*grass_per_pull

col2.write("grass count: " + str(st.session_state.grassCount))

view_gacha_stats()

col2.html("<hr>") 

if col2.button("check inventory"):
    check_inv()

if col2.button ("clear inventory"):
    clear_inv()
    col2.write("inventory cleared")
