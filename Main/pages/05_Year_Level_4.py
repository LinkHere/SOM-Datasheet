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

sheet_url = st.secrets["yrl4"]

def show_details(rows, idx):
    for itrs, row in enumerate(rows, idx):
        mobile = row.Mobile_No
        mobile = int(mobile)

        if mobile is not None:
            mobile = mobile

        if row.Vaccine_Id is not None:
            btn_state = ""

        else:
            btn_state = "disabled"
        
        st.markdown(f"""
            {row.Last_Name}
        """)
        
def choose_block(sheet_url, block):
    results = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="{block}"')
    return results

def err_msg():
    return "Error"
            
blck1a, blck1b, blck2a, blck2b, blck3a, blck3b, blck4a, blck4b, blck5a, blck5b = st.tabs(["Block1-A", "Block1-B", "Block2-A", "Block2-B", "Block3-A", "Block3-B", "Block4-A", "Block4-B", "Block5-A", "Block5-B"])
idx = 1

with blck1a:
    try:
        b1a = choose_block(sheet_url,"1-A")
        show_details(b1a, idx)
    except:
        err_msg()
    
with blck1b:
    try:
        b1b = choose_block(sheet_url,"1B")
        show_details(b1b, idx)
    except:
        err_msg()
            
st.markdown(f"""
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
