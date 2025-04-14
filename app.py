import streamlit as st
import mysql.connector

# Connect to MySQL Database
conn = mysql.connector.connect(
    host="sql12.freesqldatabase.com",   # Your host
    user="sql12773137",                 # Your username
    passwd="Vk2lyMxvTn",              # Your password
    database="sql12773137",             # Your database name
    port=3306                           # Default port
)
c = conn.cursor()

# UI Title
st.title("🛒 Grocery Shop Management System")

menu = ["Login", "Exit"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "bhuvanesh" and password == "bhuvi":
            st.success("✅ Login Successful!")

            options = [
                "See All Customers",
                "See All Products",
                "See All Workers",
                "Add Product",
                "Add Customer",
                "Add Worker",
                "Search Customer by Name",
                "Search Product by Name",
                "Search Worker by Name"
            ]
            task = st.selectbox("Select Operation", options)

            if task == "See All Customers":
                c.execute("SELECT * FROM costumers")
                data = c.fetchall()
                st.subheader("🧾 Customer Details")
                for row in data:
                    st.write(row)

            elif task == "See All Products":
                c.execute("SELECT * FROM products")
                data = c.fetchall()
                st.subheader("📦 Product Details")
                for row in data:
                    st.write(row)

            elif task == "See All Workers":
                c.execute("SELECT * FROM employees")
                data = c.fetchall()
                st.subheader("👨‍🔧 Worker Details")
                for row in data:
                    st.write(row)

            elif task == "Add Product":
                pname = st.text_input("Product Name")
                pcost = st.number_input("Product Cost", format="%.2f")
                if st.button("Add Product"):
                    query = f"INSERT INTO products VALUES ('{pname}', {pcost})"
                    c.execute(query)
                    conn.commit()
                    st.success("✅ Product added successfully!")

            elif task == "Add Customer":
                cname = st.text_input("Customer Name")
                phone = st.text_input("Phone Number")
                cost = st.number_input("Total Purchase", format="%.2f")
                if st.button("Add Customer"):
                    query = f"INSERT INTO costumers VALUES ('{cname}', {phone}, {cost})"
                    c.execute(query)
                    conn.commit()
                    st.success("✅ Customer added successfully!")

            elif task == "Add Worker":
                wname = st.text_input("Worker Name")
                work = st.text_input("Work")
                age = st.number_input("Age", min_value=0, step=1)
                salary = st.number_input("Salary", format="%.2f")
                phone = st.text_input("Phone Number")
                if st.button("Add Worker"):
                    query = f"INSERT INTO employees VALUES ('{wname}', '{work}', {age}, {salary}, {phone})"
                    c.execute(query)
                    conn.commit()
                    st.success("✅ Worker added successfully!")

            elif task == "Search Customer by Name":
                name = st.text_input("Enter customer name to search")
                if st.button("Search Customer"):
                    c.execute(f"SELECT * FROM costumers WHERE name = '{name}'")
                    result = c.fetchall()
                    if result:
                        for row in result:
                            st.write(row)
                    else:
                        st.warning("No customer found with that name.")

            elif task == "Search Product by Name":
                pname = st.text_input("Enter product name to search")
                if st.button("Search Product"):
                    c.execute(f"SELECT * FROM products WHERE product = '{pname}'")
                    result = c.fetchall()
                    if result:
                        for row in result:
                            st.write(row)
                    else:
                        st.warning("No product found with that name.")

            elif task == "Search Worker by Name":
                wname = st.text_input("Enter worker name to search")
                if st.button("Search Worker"):
                    c.execute(f"SELECT * FROM employees WHERE name = '{wname}'")
                    result = c.fetchall()
                    if result:
                        for row in result:
                            st.write(row)
                    else:
                        st.warning("No worker found with that name.")
        else:
            st.error("🚫 Incorrect username or password!")

elif choice == "Exit":
    st.warning("Goodbye! 👋")
