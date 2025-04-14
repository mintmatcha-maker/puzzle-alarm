import streamlit as st
import numpy as np

def sliding_puzzle():
    st.title("Sliding Puzzle Alarm")
    st.write("Solve this puzzle to wake up!")

    puzzle = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    empty_pos = [2, 2]

    def render_puzzle():
        for i in range(3):
            cols = st.columns(3)
            for j in range(3):
                value = puzzle[i][j]
                label = " " if value == 0 else str(value)
                if cols[j].button(label, key=f"{i}-{j}"):
                    move_tile(i, j)

    def move_tile(i, j):
        if (abs(empty_pos[0] - i) + abs(empty_pos[1] - j)) == 1:
            puzzle[empty_pos[0]][empty_pos[1]] = puzzle[i][j]
            puzzle[i][j] = 0
            empty_pos[0], empty_pos[1] = i, j

    render_puzzle()

    if np.array_equal(puzzle, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])):
        st.success("You solved it! Good morning 🌞")

def main():
    st.set_page_config(page_title="Smart Puzzle Alarm", page_icon="⏰")
    st.title("Smart Puzzle Alarm System")
    choice = st.radio("Choose Puzzle", ["Sliding Puzzle", "Coming Soon"])
    
    if choice == "Sliding Puzzle":
        sliding_puzzle()
    else:
        st.info("More puzzles will be added soon!")

if __name__ == "__main__":
    main()
