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
        
        col1, col2, col3 = st.columns([0.3,3,2])
    
        with col1:
            st.markdown(f"""<span class="badge text-bg-danger">{itrs}</span>""", unsafe_allow_html=True)
    
        with col2:
            st.markdown(f"""<p>{row.Last_Name}, {row.First_Name} {row.Middle_Initial}</p>""", unsafe_allow_html=True)
        
        with col3:
            student = st.checkbox('View Details', key={row.Vaccine_Id}, value=False)
        
        if student:
            st.markdown(f"""<div class="card" style="margin-top: -13px; margin-bottom: 2rem; color: #777;">
              <div class="card-body">
                <em><p class="card-text"><strong>Permanent Address:</strong> {row.Permanent_Address}</br>
                <strong>Current Address:</strong> {row.Current_Address}</br>
                <strong>Staying with?:</strong>{row.Leaving_With}</br>
                <strong>Father's Name and No.:</strong> {row.Father_and_Mobile}</br>
                <strong>Mother' Name and No.:</strong> {row.Mother_and_Mobile}</br>
                <strong>Emergency Contact Person:</strong> {row.Emergency_Contact_Person}</br>
                <strong>CEU Mail:</strong> {row.CEU_Mail}</br>
                <strong>Mobile No.:</strong> {mobile}</br>
                <strong>PhilHealth?:</strong> {row.PhilHealth}</br>
                <strong>PhilHealth Category:</strong> {row.PhilHealth_Category}</br>
                <strong>Medical Insurance?:</strong> {row.Medical_Insurance}</br>
                <strong>List of Medical Insurances:</strong> {row.List_of_Medical_Insurances}</br>
                <strong>Covid19 Vaccine?</strong> {row.Covid19_Vaccine}</br>
                </p></em>
                <a href="{row.Vaccine_Id}" class="btn btn-outline-dark {btn_state}">Vaccination ID/Certificate</a>
              </div>
            </div>""", unsafe_allow_html=True)
        
def choose_block(sheet_url, block):
    results = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="{block}"')
    return results
            
blck1a, blck1b, blck2a, blck2b, blck3a, blck3b, blck4a, blck4b, blck5a, blck5b = st.tabs(["Block1-A", "Block1-B", "Block2-A", "Block2-B", "Block3-A", "Block3-B", "Block4-A", "Block4-B", "Block5-A", "Block5-B"])
idx = 1

with blck1a:
    b1a = choose_block(sheet_url,"1-A")
    show_details(b1a, idx)
    
with blck1b:
    b1b = choose_block(sheet_url,"1-B")
    show_details(b1b, idx)
    
with blck2a:
    b2a = choose_block(sheet_url,"2-A")
    show_details(b2a, idx)

with blck2b:
    b2b = choose_block(sheet_url,"2-B")
    show_details(b2b, idx)
    
with blck3a:
    b3a= choose_block(sheet_url,"3-A")
    show_details(b3a, idx)

with blck3b:
    b3b = choose_block(sheet_url,"3-B")
    show_details(b3b, idx)
    
with blck4a:
    b4a = choose_block(sheet_url,"4-A")
    show_details(b4a, idx)

with blck4b:
    b4b = choose_block(sheet_url,"4-B")
    show_details(b4b, idx)
    
with blck5a:
    b5a = choose_block(sheet_url,"5-A")
    show_details(b5a, idx)
    
with blck5b:
    b5b = choose_block(sheet_url,"5-B")
    show_details(b5b, idx)
            
st.markdown(f"""
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
