import streamlit as st

from streamlit_option_menu import option_menu
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

sheet_url = st.secrets["yrl2"]
#rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Section="Section A"')

# with st.sidebar:
#     selected = option_menu("Main Menu", ["Section A", "Section B"], menu_icon="house", default_index=0)

# if selected:
    #selected = selected.replace('Block ', '')
rows = run_query(f'SELECT * FROM "{sheet_url}"')

for itrs, row in enumerate(rows):
        
    if row.Mobile_No is not None:
        mobile = int(row.Mobile_No)
        
    if row.Vaccine_Id is not None:
        btn_state = ""
    else:
        btn_state = "disabled"
        
    st.markdown(f"""
        <div class="card">
         <div class="card-header">
          Featured
         </div>

         <div class="card-body">
          <h5 class="card-title">Special title treatment</h5>
          <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
         </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown(f"""
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
