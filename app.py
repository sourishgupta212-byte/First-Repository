import streamlit as st

# 1. SET UP THE WEB PAGE WINDOW
st.set_page_config(page_title="The Unfinished Game", page_icon="🎮")
st.title("The Narrator's Room")

# 2. INITIALIZE GAME STATE (This remembers what the player has done)
if "step" not in st.session_state:
    st.session_state.step = "start"
if "searched" not in st.session_state:
    st.session_state.searched = []

# 3. HELPER FUNCTION TO CHANGE SCENES
def go_to(next_step):
    st.session_state.step = next_step
    st.rerun()

# ----------------- GAME SCENES -----------------

# SCENE: START
if st.session_state.step == "start":
    st.write("---")
    st.subheader("Anonymous: Psst.. Over here. Take this.")
    st.caption("✨ Item Acquired: Key")
    st.write("Anonymous: There is a door behind you. The narrator cannot be trusted...")
    st.write("*Noises*... He is here! I must hide!")
    
    if st.button("Continue"):
        go_to("narrator_arrives")

# SCENE: NARRATOR
elif st.session_state.step == "narrator_arrives":
    st.write("---")
    st.write("Narrator: Hey! I am back. Did anyone happen to give you a key?")
    st.write("You: No?")
    st.write("Narrator: Good. No one here can be trusted except me. *Leaves*")
    st.write("Anonymous: He is hiding his true identity! Search the room for anything useful.")
    
    if st.button("Look around the room"):
        go_to("search_room")

# SCENE: SEARCH ROOM (Uses your list logic!)
elif st.session_state.step == "search_room":
    st.write("---")
    st.write("What do you want to search?")
    
    # Check if they found everything
    if len(st.session_state.searched) == 2:
        st.success("You found a metal device from the desk and a weird math book on the bookshelf!")
        if st.button("Unlock the Door"):
            go_to("door_hallway")
    else:
        # Button 1: Desk
        if "Desk" not in st.session_state.searched:
            if st.button("Search Desk"):
                st.session_state.searched.append("Desk")
                st.rerun()
        else:
            st.write("*(You already searched the desk)*")
            
        # Button 2: Bookshelf
        if "Bookshelf" not in st.session_state.searched:
            if st.button("Search Bookshelf"):
                st.session_state.searched.append("Bookshelf")
                st.rerun()
        else:
            st.write("*(You already searched the bookshelf)*")

# SCENE: THE DOOR
elif st.session_state.step == "door_hallway":
    st.write("---")
    st.write("Door: *Opens dramatically*")
    st.write("You: What is this place?")
    st.write("Door: Suddenly, the wall fell down revealing a metal hallway with two doors!")
    
    # Choices layout using web buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("A - Go Right"):
            go_to("go_right")
    with col2:
        if st.button("B - Go Left"):
            go_to("go_left")
    with col3:
        if st.button("C - Ask the Door"):
            go_to("ask_door")

# SCENE: GO RIGHT
elif st.session_state.step == "go_right":
    st.write("---")
    st.write("Door: You choose to go right...")
    st.write("You see a room lined with dozens of computers running scripts...")
    st.write("Computer: Searching files... Updating files... Game import failed.")
    st.write("Meanwhile, back at the original room...")
    st.error("Narrator: Where is the player? Eren... I am going to find you, Eren.")
    
    if st.button("Restart Game"):
        st.session_state.clear()
        st.rerun()

# SCENE: GO LEFT
elif st.session_state.step == "go_left":
    st.write("---")
    st.write("You went left! But you haven't coded this part yet!")
    if st.button("Go Back"):
        go_to("door_hallway")

# SCENE: ASK DOOR
elif st.session_state.step == "ask_door":
    st.write("---")
    st.write("You: Mr. Door, what is this?")
    st.write("Door: You were rude to me earlier. Why should I tell you? :(")
    
    if st.button("Apologize"):
        st.write("Door: Well, since you apologized... it's a hallway leading two ways.")
        if st.button("Continue"):
            go_to("door_hallway")
