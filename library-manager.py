import streamlit as st
import pandas as pd


st.set_page_config(layout="wide",page_icon="📔",page_title="Library-manager")
st.title("LIBRARY MANAGER 📔")   

library:list=[
    {"title":"To Kill a Mockingbird","author":"	Harper Lee","genera":"Fiction / Classic","publication_year":"1960","isread":True},
    {"title":"1984","author":"	George Orwell","genera":"Dystopian / Political","publication_year":"1949","isread":True},
    {"title":"Harry Potter and the Sorcerer's Stone","author":"	J.K. Rowling","genera":"Fantasy / Young Adult","publication_year":"1997","isread":False},
]
# coppying the array so that when the script reloads the changes remain intact
if "library" not in st.session_state:
    st.session_state.library = library.copy()

library = st.session_state.library

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

st.sidebar.title("EDIT YOUR LIBRARY✏️")    
st.sidebar.title("Scroll to see results of your selected options") 
  
# On the side bar the choices are provided for editing an managing library 
choices = st.sidebar.selectbox( "SELECT FROM THE FOLLOWING OPTIONS 📝 ", [
        "Display all books",
        "Add a book",
        "Remove a book",
        "Search for a book",
        "Display statistics"])


if choices == "Add a book":
    st.title("ADD BOOKS")
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
       #print(library)
    else:
        print("This book can not be added")   
       
else:
    print("The choice is not approparate ")  
    
# Removing books    
if choices == "Remove a book":
    st.title("REMOVE BOOKS")    
    remove_by_title = st.text_input("Enter book title")
    
    if st.button("Remove book"):
       selected_book = next((book for book in library if book["title"]==remove_by_title),None)
       if selected_book :
           library.remove(selected_book)
           st.success("your book has been removed")
           #print(library)
       else:
           st.error ("this book is not avalible")   
else:
    print("The choice is not approparate ")          

# Displaying all the books
if choices == "Display all books":
    st.title("AVALABLE BOOKS")
    st.markdown(book_cards, unsafe_allow_html=True)
    for book in library:
     st.markdown(
        f"""
        <div class="cardHolderDiv">
             <div class="card">
                 <h5>Title: {book["title"]}</h5>
                 <p>Author: {book["author"]}</p>
                 <p>Genera: {book["genera"]}</p>
                 <p>publication year: {book["publication_year"]}</p>
                 <p>Read: {"yes" if book["isread"] else "No"}</p>
             </div>
        </div>
       
        """,unsafe_allow_html=True
     )
else:
    print("The choice is not approparate ")  


# search for a book
if choices == "Search for a book":
    search_input = st.text_input("Enter your book title")
    
    if st.button("search book"):
       searched_book = next((book for book in library if book["title"]==search_input),None)
       #print(searched_book)
       if searched_book:
           st.success("Book found ✅")
           st.markdown(f"""
            **Title:** {searched_book['title']}  
            **Author:** {searched_book['author']}  
            **Genera:** {searched_book['genera']}  
            **Publication Year:** {searched_book['publication_year']}  
            **Read:** {"Yes" if searched_book["isread"] else "No"}
            """)
       else:
           st.error("Book not found")
else:
    print("The choice is not approparate ")
    
    
 # Displaying statisctics   
if choices ==  "Display statistics":
    st.title("LIBRARY STATISTICS",)
    
    total_books = len(library)
    st.write(f"TOTAL BOOKS: {total_books}")
  
    read_book = sum(1 for book in library if book["isread"])
    st.write(f"READ BOOKS: {read_book}")
    
    unread_books = total_books- read_book
    st.write(f"UNREAD BOOKS: {unread_books}")

    average = (read_book/total_books)*100 
    st.write(f"PERCENTAGE: {average}%")
    
    represent_graph= pd.DataFrame({
        "status":["read","unread"],
        "count":[read_book,unread_books]
    })
    st.bar_chart(represent_graph.set_index("status"))

else:
    print("The choice is not approparate ")
           