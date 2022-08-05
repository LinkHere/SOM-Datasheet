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

sheet_url = st.secrets["private_gsheets_url"]
#rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Section="Section A"')

with st.sidebar:
    selected = option_menu("Main Menu", ["Section A", "Section B"], menu_icon="house", default_index=0)

if selected:
    #selected = selected.replace('Block ', '')
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Section="{selected}"')

    for itrs, row in enumerate(rows):
        
        if row.Mobile_no is not None:
            mobile = int(row.Mobile_no)
        
        if row.Vaccine_id is not None:
            btn_state = ""
        else:
            btn_state = "disabled"
        
        st.markdown(f"""
            <div class="card" style="margin-bottom: 2rem; color: #777;">
              <div class="card-header">
              Year Level 3 - {row.Section}
              </div>
              <div class="card-body">
                <h5 class="card-title" style="color: #777"><u><i>{row.Last_Name}</i>, {row.First_Name} {row.Middle_Initial}</u></h5>
                <em><p class="card-text"><strong>Permanent Address:</strong> {row.Permanent_Address}</br>
                <strong>Current Address:</strong> {row.Current_Address}</br>
                <strong>Staying with Relatives?:</strong> {row.Staying_with_relatives}</br>
                <strong>Staying with other SOM Students?:</strong> {row.Staying_with_other_SOM_Students}</br>
                <strong>Staying with:</strong> {row.Staying_with}</br>
                <strong>Father's Name and No.:</strong> {row.Father_and_No}</br>
                <strong>Mother' Name and No.:</strong> {row.Mother_and_No}</br>
                <strong>Emergency Contact Person:</strong> {row.Emergency_contact}</br>
                <strong>CEU Mail:</strong> {row.CEU_mail}</br>
                <strong>Mobile No.:</strong> {mobile}</br>
                <strong>PhilHealth?:</strong> {row.PhilHealth}</br>
                <strong>PhilHealth Category:</strong> {row.PhilHealth_category}</br>
                <strong>Other Medical Insurance?:</strong> {row.Other_Medical_Insurance}</br>
                <strong>Medical Insurances:</strong> {row.Medical_Insurances}</br>
                <strong>Covid19 Vaccine?</strong> {row.Covid19_vaccine}</br>
                </p></em>
                <a href="{row.Vaccine_id}" class="btn btn-outline-dark {btn_state}">Vaccination ID/Certificate</a>
              </div>
            </div> 
        """, unsafe_allow_html=True)

st.markdown(f"""
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
