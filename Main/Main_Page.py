import streamlit as st

from google.oauth2 import service_account
from gsheetsdb import connect

st.markdown(f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
""", unsafe_allow_html=True)

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)

conn = connect(credentials=credentials)

@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url1 = st.secrets["yrl1"]
sheet_url2 = st.secrets["yrl2"]
sheet_url3 = st.secrets["yrl3"]

rows1 = run_query(f'SELECT Last_Name FROM "{sheet_url1}"')
rows2 = run_query(f'SELECT Last_Name FROM "{sheet_url2}"')
rows3 = run_query(f'SELECT Last_Name FROM "{sheet_url3}"')

st.write("1st Yr",len(rows1))
st.write("2nd Yr",len(rows2))
st.write("3rd Yr",len(rows3))
