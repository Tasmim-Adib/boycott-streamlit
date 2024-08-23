import streamlit as st
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()

def extract_english(text):
    match = re.match(r"([a-zA-Z\s]+)", text)
    return match.group(1).strip().lower() if match else ""


# MongoDB connection details
MONGODB_URL = os.getenv("MONGODB_URL")
client = MongoClient(MONGODB_URL)
database = client['boycott']
collection = database['products']

# Streamlit app
# st.markdown("<h2 style = 'color : tomato; text-align : center'>আপনার নিজের সামর্থ্য দিয়ে সর্বোচ্চ চেষ্টা করুন <br/> মানবতার বিজয় হবেই ইনশাআল্লাহ</h2>", unsafe_allow_html=True)
# st.title("Boycott Israeli Products")
st.markdown("<h2 style = 'color : tomato; text-align : center'>Boycott Indian Products</h2>", unsafe_allow_html=True)
# st.title("Boycott Indian Products")
# Sidebar for user input
# st.sidebar.header("Add Product")

# # Input fields for adding a new product
# category = st.sidebar.text_input("Category")
# local_list = st.sidebar.text_area("Local List (comma-separated)")
# india_list = st.sidebar.text_area("India List (comma-separated)")
# israel_list = st.sidebar.text_area("Israel List (comma-separated)")

data = ["Select Category", "Rice (চাল)","Oil (তেল)", "Soap (সাবান)", "Shampoo (শ্যাম্পু)", "Face Wash (ফেস ওয়াস)", "Toothpaste (টুথপেস্ট)", "Detergent (ডিটারজেন্ট)","Perfume and Body Spray (পারফিউম ও বডি স্প্রে)",
"lotion (লোশন)","shower gel (শাওয়ার জেল)","Tea (চা)","Coffee (কফি)","Water (পানি)"
  ,"Cold and Soft Drink (কোল্ড ও সফট ড্রিংক্স)","Toilet Cleaner (টয়লেট ক্লিনার)","Dish Cleaner (ডিস ক্লিনার)","Juice (জুস)","Chocolate (চকলেট)","Sanitary Napkin and Pad (স্যানিটারি ন্যাপকিন ও প্যাড)","Powder Drink (পাউডার ড্রিংক)",
   "Condom and Pill (কনডম ও পিল)"]
 

# Convert the comma-separated input to list
# local_list = local_list.split(",") if local_list else []
# india_list = india_list.split(",") if india_list else []
# israel_list = israel_list.split(",") if israel_list else []

# if st.sidebar.button("Add Product"):
#     product = {
#         "c": category,
#         "l": local_list,
#         "ia": india_list,
#         "ir": israel_list
#     }
#     collection.insert_one(product)
#     st.sidebar.success("Product added successfully!")

# Input field for fetching a product by category

fetch_category = st.selectbox(" ", options=data)

if st.button("Search"):
    fetch_category = extract_english(fetch_category)
    product = collection.find_one({"c": fetch_category})
    if product:
        st.markdown(f"## Category: {product['c'].capitalize()}")


        st.markdown("<h3 style='color: red;'>Indian Product (ভারতীয় পণ্য):</h3>", unsafe_allow_html=True)
        st.markdown("<ul>" + "".join([f"<li>{item}</li>" for item in product['ia']]) + "</ul>", unsafe_allow_html=True)


        st.markdown("<h3 style='color: green;'>Local Products (দেশীয় পণ্য):</h3>", unsafe_allow_html=True)
        st.markdown("<ul>" + "".join([f"<li>{item}</li>" for item in product['l']]) + "</ul>", unsafe_allow_html=True)

        st.markdown("<h3 style='color: red;'>Related to Israel (ইসরাইলের সাথে সম্পর্কিত):</h3>", unsafe_allow_html=True)
        st.markdown("<ul>" + "".join([f"<li>{item}</li>" for item in product['ir']]) + "</ul>", unsafe_allow_html=True)
        
        st.markdown("<a href='https://boycott.thewitness.news/browse/1'>Visit this site to get details</a>", unsafe_allow_html=True)

        
        
    else:
        st.error("Product not found.")

    st.markdown("<p style='color : #621f00; '>সকল পন্যের নাম রাখা সম্ভব হয়নি। এই তালিকা উন্নতি করতে আপনাদের সহযোগিতা একান্ত কাম্য</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center'>&copy Copyright : Tasmim Rahman Adib</p>", unsafe_allow_html=True)

# # Input field for updating a product
# st.header("Update Product")
# update_category = st.text_input("Enter Category to Update Product")
# new_local_list = st.text_area("New Local List (comma-separated)")
# new_india_list = st.text_area("New India List (comma-separated)")
# new_israel_list = st.text_area("New Israel List (comma-separated)")

# # Convert the comma-separated input to list
# new_local_list = new_local_list.split(",") if new_local_list else []
# new_india_list = new_india_list.split(",") if new_india_list else []
# new_israel_list = new_israel_list.split(",") if new_israel_list else []

# if st.button("Update Product"):
#     update_data = {
#         "l": new_local_list,
#         "ia": new_india_list,
#         "ir": new_israel_list
#     }
#     result = collection.update_one({"c": update_category}, {"set": update_data})
#     if result.matched_count > 0:
#         st.success("Product updated successfully!")
#     else:
#         st.error("Product not found.")

# # Input field for deleting a product
# st.header("Delete Product")
# delete_category = st.text_input("Enter Category to Delete Product")

# if st.button("Delete Product"):
#     result = collection.delete_one({"c": delete_category})
#     if result.deleted_count > 0:
#         st.success("Product deleted successfully!")
#     else:
#         st.error("Product not found.")
