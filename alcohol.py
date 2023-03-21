@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, sep=";", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(1400)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Alcohol')
hist_values = np.histogram(data['alcohol'], bins=15, range=(0,24))[0]
st.bar_chart(hist_values)

