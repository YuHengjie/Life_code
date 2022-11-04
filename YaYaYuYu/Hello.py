# %%
from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt
import datetime,requests
from plotly import graph_objects as go
import base64

# %%
plt.style.use('default')

st.set_page_config(
    page_title = 'Hello',
    page_icon = '💫',
    layout = 'wide'
)

# %%
st.sidebar.success("Select a module above.")

# %%
st.write("# Welcome to Yaya&Yuyu's website! 👋")
st.write("")
st.write("")

# %%
placeholder1 = st.empty()
with placeholder1.container():
    f1,f2 = st.columns([1,1])
    with f1:
        file_ = open("YaYaYuYu/image/yayacartoon.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" >',
        unsafe_allow_html=True,
        )
    with f2:
        file_ = open("YaYaYuYu/image/fishresize.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" >',
        unsafe_allow_html=True,
        )


# %%
st.write('')
st.write('')
st.write('')

# %%
st.write('# My girl, how are you feeling today 😊')

col1, col2 = st.columns(2)

with col1:
    emo = st.selectbox('',['（づ￣3￣）づ╭❤～','Happy','Not bad','Sad'])
    if emo == 'Happy':
        file_ = open("YaYaYuYu/image/happy.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" >',
        unsafe_allow_html=True,
        )
    if emo == 'Not bad':
        file_ = open("YaYaYuYu/image/notbad.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" >',
        unsafe_allow_html=True,
        )
    if emo == 'Sad':
        file_ = open("YaYaYuYu/image/sad.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" >',
        unsafe_allow_html=True,
        )
with col2:
    st.write('')
    st.write('')
    st.markdown("<h3 style='text-align: center; color: black;'>See Yuyu\'s action </h3>", unsafe_allow_html=True)

    if emo == 'Happy':
        file_ = open("YaYaYuYu/image/happytwo.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" >',
        unsafe_allow_html=True,
        )
    if emo == 'Not bad':
        file_ = open("YaYaYuYu/image/notbadtwo.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" >',
        unsafe_allow_html=True,
        )
    if emo == 'Sad':
        file_ = open("YaYaYuYu/image/sadtwo.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" >',
        unsafe_allow_html=True,
        )

# %%
st.write('')
st.write('')
st.write('')

# %%
st.write('# Weather forecast, Take care 🌧️🌥️')

# %%

city = 'Shenzhen'
api="9b833c0ea6426b70902aa7a4b1da285c"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
response=requests.get(url)
x=response.json()

lon=x["coord"]["lon"]
lat=x["coord"]["lat"]
ex="current,minutely,hourly"
url2=f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={ex}&appid={api}'
res=requests.get(url2)
y=res.json()

# %%
maxtemp=[]
mintemp=[]
pres=[]
humd=[]
wspeed=[]
desc=[]
cloud=[]
rain=[]
dates=[]
sunrise=[]
sunset=[]
cel=273.15

for item in y["daily"]:

    maxtemp.append(round(item["temp"]["max"]-cel,2))
    mintemp.append(round(item["temp"]["min"]-cel,2))

    wind_unit="m/s"
    wspeed.append(str(round(item["wind_speed"],1))+wind_unit)

    pres.append(item["pressure"])
    humd.append(str(item["humidity"])+' %')
    
    cloud.append(str(item["clouds"])+' %')
    rain.append(str(int(item["pop"]*100))+'%')

    desc.append(item["weather"][0]["description"].title())

    d1=datetime.date.fromtimestamp(item["dt"])
    dates.append(d1.strftime('%d %b'))
    
    sunrise.append( datetime.datetime.utcfromtimestamp(item["sunrise"]).strftime('%H:%M'))
    sunset.append( datetime.datetime.utcfromtimestamp(item["sunset"]).strftime('%H:%M'))

icon=x["weather"][0]["icon"]
current_weather=x["weather"][0]["description"].title()
unit="Celsius"
temp=str(round(x["main"]["temp"]-cel,2))

col1, col2 = st.columns(2)
with col1:
    st.write("## Current Temperature ")
with col2:
    st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png",width=70)

col1, col2= st.columns(2)
temp_unit = " °C"
col1.metric("TEMPERATURE",temp+temp_unit)
col2.metric("WEATHER",current_weather)

# %%
st.write("## Today's Weather ")
col1, col2, col3, col4= st.columns(4)
temp_unit = " °C"
humidity_unit = ' %'
windspeed_unit = ' m/s'
min_temp = round(y['daily'][0]['temp']['min']-cel,2)
max_temp  = round(y['daily'][0]['temp']['max']-cel,2)
col1.metric("TEMPERATURE",f'{min_temp}~{max_temp} {temp_unit}')
col2.metric("WEATHER",y['daily'][0]['weather'][0]['description'].title())
humidity = y['daily'][0]['humidity']
col3.metric("HUMIDITY", f'{humidity}'+ humidity_unit)
windspeed = y['daily'][0]['wind_speed']
col4.metric("WINDSPEED", f'{windspeed}'+ windspeed_unit)

# %%
st.write("## Tomorrow's Weather ")
col1, col2, col3, col4= st.columns(4)
temp_unit = " °C"
humidity_unit = ' %'
windspeed_unit = ' m/s'
min_temp = round(y['daily'][1]['temp']['min']-cel,2)
max_temp  = round(y['daily'][1]['temp']['max']-cel,2)
col1.metric("TEMPERATURE",f'{min_temp}~{max_temp} {temp_unit}')
col2.metric("WEATHER",y['daily'][1]['weather'][0]['description'].title())
humidity = y['daily'][1]['humidity']
col3.metric("HUMIDITY", f'{humidity}'+ humidity_unit)
windspeed = y['daily'][1]['wind_speed']
col4.metric("WINDSPEED", f'{windspeed}'+ windspeed_unit)

# %%
st.write('')
st.write('')
st.write('')

# %%
st.write('# Today\'s agenda 📰')
agenda = st.selectbox('',['︿(￣︶￣)︿','Study','Exercise','Relax','Miss you'])
if agenda=='Study':
    file_ = open("YaYaYuYu/image/wa.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" >',
    unsafe_allow_html=True,
    ) 
if agenda=='Exercise':
    file_ = open("YaYaYuYu/image/catmouse.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" >',
    unsafe_allow_html=True,
    ) 
if agenda=='Relax':
    file_ = open("YaYaYuYu/image/touchfish.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" >',
    unsafe_allow_html=True,
    ) 
if agenda=='Miss you':
    file_ = open("YaYaYuYu/image/cutedog.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" >',
    unsafe_allow_html=True,
    ) 

# %%
st.write('')
st.write('')
st.write('')

# %%
st.write('# Acknowledgements and notes ❤️')
st.markdown(
    """
    - This is a 100-day anniversary gift from Yuyu to Yaya (a very cute, pretty, kind, brave girl, Yuyu's girl).
    - Yuyu says, he is very grateful for the appearance of Yaya.
    - Yuyu also says, he is so lucky to have a girlfriend who can make him himself.
    - The website is constantly being updated, looking forward to the days when Yaya and Yuyu can be together every day.
"""
)
