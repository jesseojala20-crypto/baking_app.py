import streamlit as st
# Title of the app
st.title("Bakers unit converter")
st.markdown("Easily convert between US and EU measurements")

mode = st.sidebar.radio("Valitse suunta:", ["US to EU", "EU to US"])

if mode == "US to EU":
    option = st.selectbox("Mitä haluat muuntaa?", ["Cup -> dl", "Pint -> dl", "Ounce -> g", "Pound -> g"])
    maara = st.number_input("Syötä määrä:", min_value=0.0, step=0.1)

    if option == "Cup -> dl":
         st.success(f"{maara} cups = **{maara * 2.36:.2f} dl**")
    elif option == "Pint -> dl":
         st.success(f"{maara} pints = **{maara * 4.80:.2f} dl**")
    elif option == "Ounce -> g":
         st.success(f"{maara} ounces = **{maara * 28.35:.2f} g**")
    elif option == "Pound -> g":
         st.success(f"{maara} pounds = **{maara * 451.0:.2f} g**")
else: # EU to US
    option = st.selectbox(
        "Mitä haluat muuntaa?",
        ["dl -> Cup", "dl -> Pint", "g -> Ounce", "g -> Pound"]
    )
    maara = st.number_input("Syötä määrä:", min_value=0.0, step=0.1)

    if option == "dl -> Cup":
        st.success(f"{maara} dl = **{maara / 2.36:.2f} cups**")
    elif option == "dl -> Pint":
        st.success(f"{maara} dl = **{maara / 4.80:.2f} pints**")
    elif option == "g -> Ounce":
        st.success(f"{maara} g = **{maara / 28.35:.2f} oz**")
    elif option == "g -> Pound":
        st.success(f"{maara} g = **{maara / 451.0:.2f} lbs**")

st.info("Tip: You can use this on your phone if you host it on Streamlit Cloud!")
     