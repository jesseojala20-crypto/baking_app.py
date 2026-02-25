import streamlit as st

# Title of the app
st.title("Bakers Unit Converter")
st.markdown("Easily convert between US and EU measurements")

mode = st.sidebar.radio("Valitse suunta:", ["US to EU", "EU to US"])

if mode == "US to EU":
    option = st.selectbox("Mitä haluat muuntaa?", ["Cup -> dl", "Pint -> dl", "Ounce -> g", "Pound -> g", "F -> C"])
    maara = st.number_input("Syötä määrä:", min_value=0.0, step=0.1)

    if option == "Cup -> dl":
         st.success(f"{maara} cups = **{maara * 2.365:.2f} dl**")
    elif option == "Pint -> dl":
         st.success(f"{maara} pints = **{maara * 4.73:.2f} dl**")
    elif option == "Ounce -> g":
         st.success(f"{maara} ounces = **{maara * 28.35:.2f} g**")
    elif option == "Pound -> g":
         st.success(f"{maara} pounds = **{maara * 453.59:.2f} g**")
    elif option == "F -> C":
        celsius = (maara - 32) / 1.8
        st.success(f"{maara}°F = **{celsius:.2f}°C**")
    
else:
    option = st.selectbox(
        "Mitä haluat muuntaa?",
        ["dl -> Cup", "dl -> Pint", "g -> Ounce", "g -> Pound", "C -> F"]
    )
    maara = st.number_input("Syötä määrä:", min_value=0.0, step=0.1)

    if option == "dl -> Cup":
        st.success(f"{maara} dl = **{maara / 2.365:.2f} cups**")
    elif option == "dl -> Pint":
        st.success(f"{maara} dl = **{maara / 4.73:.2f} pints**")
    elif option == "g -> Ounce":
        st.success(f"{maara} g = **{maara / 28.35:.2f} oz**")
    elif option == "g -> Pound":
        st.success(f"{maara} g = **{maara / 453.59:.2f} lbs**")
    elif option == "C -> F":
        fahrenheit = (maara * 1.8) + 32
        st.success(f"{maara}°C = **{fahrenheit:.2f}°F**")