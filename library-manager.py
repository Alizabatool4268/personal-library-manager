import streamlit as st


st.set_page_config(layout="wide",page_icon="📔",page_title="Library-manager")
st.title("LIBRARY MANAGER 📔")   

library:list=[
    {"title":"To Kill a Mockingbird","author":"	Harper Lee","genera":"Fiction / Classic","publication_year":"1960","isread":True},
    {"title":"1984","author":"	George Orwell","genera":"Dystopian / Political","publication_year":"1949","isread":True},
    {"title":"Harry Potter and the Sorcerer's Stone","author":"	J.K. Rowling","genera":"Fantasy / Young Adult","publication_year":"1997","isread":False},
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
                <p>publication year: {book["publication_year"]}</p>
            </div>
       </div>
       
       """,unsafe_allow_html=True
    )
st.sidebar.title("EDIT YOUR LIBRARY✏️")    
st.sidebar.title("Scroll to see results of your selected options")    
choices = st.sidebar.selectbox( "SELECT FROM THE FOLLOWING OPTIONS 📝 ", [
        "Add a book",
        "Remove a book",
        "Display all books",
        "Search for a book",
        "Display statistics",])

if choices == "Add a book":
    
    title = st.text_input("Enter books title")
    author= st.text_input("Enter author name")
    Genera = st.text_input("Enter Genera")
    year = st.number_input("Enter books publication year")
    isread = st.selectbox("Have you read this book",[True,False])
    
    
    if st.button("add book"):
       new_book = {
                "title":title,
                "author":author,
                "genera":Genera,
                "publication_year":year,
                "isread":isread
            }
       library.append(new_book)
       st.success(f"{title}✔️ written by {author}✏️ is added in to the library ✨✨")
else:
    print("You can not add a book")
    
if choices == "Remove a book":
    st.title("REMOVE BOOKS")    
    remove_by_title = st.text_input("Enter book title")
    if st.button("Remove book"):
        print("")