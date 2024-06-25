import streamlit as st
import random

col1, col2 = st.columns(2)

if "inventory" not in st.session_state:
    col2.session_state.inventory = []
if "totalPulledCount" not in st.session_state:
    col2.session_state.totalPulledCount = 0

gachapool = ["cat","dog","sheep","bird","hamster","guinea pig","snake","gecko","chinchilla","rabbit","fish","turtle"]
gachaLen = len(gachapool)
limited = "qi"

def gacha_pull():
    if random.randint(1,100) == 100:
        gacha_result = limited
        col2.write("you pulled a " + limited + "!")
    else:
        gacha_result = gachapool[random.randint(0, gachaLen-1)]
    col2.session_state.totalPulledCount += 1
    col2.session_state.inventory.append(gacha_result)

def clear_inv():
    col2.session_state.inventory = []
    col2.session_state.totalPulledCount = 0

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

def check_inv():
    col2.write(st.session_state.inventory)

#interface
st.title("PW demo app")
st.header("gacha pull simulator")   

# targetScreenTime = st.text_input("target screen time by the end of 4 weeks")
# pastScreenTime = st.text_input("actual average screen time from phone for the past week")

# st.write("your target is: " + targetScreenTime + " hours")
# st.write("for the last week, your screen time was: " + pastScreenTime + " hours")

col1.write("\n")
col1.write("\n")
col1.write("\n")

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
