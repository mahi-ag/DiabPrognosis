import streamlit as st
import pandas as pd

def app():
    # Check if forum_posts.csv exists, if not, create it
    try:
        forum_posts = pd.read_csv('forum_posts.csv')
    except FileNotFoundError:
        forum_posts = pd.DataFrame(columns=['Username', 'Post'])

    # Function to add a new post to the forum
    def add_post(username, post):
        nonlocal forum_posts
        forum_posts.loc[len(forum_posts)] = [username, post]
        forum_posts.to_csv('forum_posts.csv', index=False)  # Save the updated DataFrame to CSV

    # Function to display the forum posts
    def display_forum():
        st.subheader('Community Forum')
        if forum_posts.empty:
            st.write('No posts yet. Be the first to start the conversation!')
        else:
            for index, row in forum_posts.iterrows():
                st.write(f'**{row["Username"]}** says: {row["Post"]}')

    # Sidebar for posting new messages
    st.sidebar.title('New Post')
    username = st.sidebar.text_input('Username', 'Anonymous')
    post = st.sidebar.text_area('Write your message')

    if st.sidebar.button('Post'):
        if post:
            add_post(username, post)
            st.sidebar.text('Post added successfully!')
        else:
            st.sidebar.text('Please enter a message.')

    # Display the forum posts
    display_forum()

# If you have other functions or code specific to the community module, you can add it here.
