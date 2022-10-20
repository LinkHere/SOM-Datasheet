import streamlit as st

from streamlit_option_menu import option_menu
from google.oauth2 import service_account
from gsheetsdb import connect

st.markdown(f"""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
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

sheet_url = st.secrets["yrl3"]
rows_tab1 = run_query(f'SELECT * FROM "{sheet_url}" WHERE Section="Section A"')
rows_tab2 = run_query(f'SELECT * FROM "{sheet_url}" WHERE Section="Section B"')

def show_details(rows, 1):
    for itrs, row in enumerate(rows, 1):
        if row.Mobile_no is not None:
            mobile = int(row.Mobile_no)

        if row.Vaccine_id is not None:
            btn_state = ""
        else:
            btn_state = "disabled"
        st.markdown(f"""
            {row.Last_Name}
        """, unsafe_allow_html=True)

#with st.sidebar:
#    selected = option_menu("Main Menu", ["Section A", "Section B"], menu_icon="house", default_index=0)

#if selected:
    #selected = selected.replace('Block ', '')
#    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Section="{selected}"')
tab1, tab2 = st.tabs(["Section A","Section B"])

with tab1:
    show_details(rows_tab1, 1)
        

st.markdown(f"""
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
