import streamlit as st
import plotly.express as px
from backend import get_data

#add title, next input, slider,
st.title("Weather for the next days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # get temperature
    try:
        filtered_data = get_data(place, days)


        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt.txt"] for dict in filtered_data]
        # create a temperature
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            st.image()
    except KeyError:
        st.write("That place does not exist")


