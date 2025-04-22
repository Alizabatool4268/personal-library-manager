import streamlit as st


st.set_page_config(layout="wide",page_icon="📔",page_title="Library-manager")
st.title("LIBRARY MANAGER 📔")   

library:list=[
    {"title":"To Kill a Mockingbird","author":"	Harper Lee","genera":"Fiction / Classic","publication year":"1960"},
    {"title":"1984","author":"	George Orwell","genera":"Dystopian / Political","publication year":"1949"},
    {"title":"Harry Potter and the Sorcerer's Stone","author":"	J.K. Rowling","genera":"Fantasy / Young Adult","publication year":"1997"},
]

book_cards= """
 <style>
 .cardHolderDiv {
     width:100%;
     display:flex;
     justify-content:center;
     align-items:center;
 }
 .card {
     background-color:#f9b9f9;
     border:2px solid black;
     padding:2px;
     border-radius:10px;
     box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
     color:black;
     width:20rem;
     text-align:center;
 }
 </style>
"""

st.markdown(book_cards, unsafe_allow_html=True)
st.title("AVALABLE BOOKS")
for book in library:
    st.markdown(
       f"""
       <div class="cardHolderDiv">
            <div class="card">
                <h5>Title: {book["title"]}</h5>
                <p>Author: {book["author"]}</p>
                <p>Genera: {book["genera"]}</p>
                <p>publication year: {book["publication year"]}</p>
            </div>
       </div>
       
       """,unsafe_allow_html=True
    )