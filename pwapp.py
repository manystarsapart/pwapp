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

#col1: data input

# targetScreenTime = float(col1.text_input("target screen time by the end of 4 weeks"))
# pastScreenTime = float(col1.text_input("actual average screen time from phone for the past week"))

# col1.write("your target is: " + str(targetScreenTime) + " hours")
# col1.write("for the last week, your screen time was: " + str(pastScreenTime) + " hours")

# col1.html("<hr>", unsafe_allow_html=True) # draws a line

# todayScreenTime = float(col1.text_input("screen time by the end of today"))
# col1.write("today's screen time: " + str(todayScreenTime))
# col1.write("past screen time: " + str(pastScreenTime))
# if todayScreenTime <= pastScreenTime:
#     col1.write("congrats! your screen time today is under your past screen time.")
    

#col2: the gacha simulator

col2.header("gacha pull simulator")  

gachapool = ["cat","dog","sheep","bird","hamster","guinea pig","snake","gecko","chinchilla","rabbit","fish","turtle"]
gachaLen = len(gachapool)
limited = "qi"
standard = "not_qi"
guaranteed_status = 0
max_pity = 80









def gacha_pull():
    if st.session_state.hard_pity < max_pity: # normal pull, not hard pity
        if random.randint(1,100) == 100: # 1% chance of pulling a rare
            gacha_result = random.choice(standard, limited) # 50/50 between standard and limited
            col2.write("you pulled " + gacha_result + " at " + str(st.session_state.hard_pity) + " pity!") # display congratulatory message
            st.session_state.hard_pity = 0 # resets hard pity
        else: # normal pull, no rare
            gacha_result = gachapool[random.randint(0, gachaLen-1)] # picks between non-rare list
            st.session_state.hard_pity += 1 
    else: # hard pity reached
        gacha_result = random.choice(standard, limited) # 50/50 between standard and limited
        col2.write("you pulled " + gacha_result + " at max pity, which is " + str(max_pity))
        st.session_state.hard_pity = 0 
    st.session_state.totalPulledCount += 1
    st.session_state.inventory.append(gacha_result)
        
        








def clear_inv():
    st.session_state.inventory = []
    st.session_state.totalPulledCount = 0

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

 



if col2.button("hide dialogue"):
    #balls
    col2.write()

if col2.button ("pull 1"):
    gacha_pull()
    col2.write("you pulled 1 time")

if col2.button("pull 10"):
    pull_for_amt(10)

if col2.button("pull 100"):
    pull_for_amt(100)

if col2.button("pull 1000"):
    pull_for_amt(1000)

if col2.button("check inventory"):
    check_inv()

if col2.button ("clear inventory"):
    clear_inv()
    col2.write("inventory cleared")

view_gacha_stats()
