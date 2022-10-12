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

sheet_url = st.secrets["yrl1"]

rows = run_query(f'SELECT * FROM "{sheet_url}"')

for itrs, row in enumerate(rows, 1):
        
    if row.Mobile_No is not None:
        mobile = int(row.Mobile_No)
        
    if row.Vaccine_Id is not None:
        btn_state = ""
    else:
        btn_state = "disabled"
        
    st.markdown(f"""
        <div class="form-floating">
            <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea"></textarea>
            <label for="floatingTextarea">Comments</label>
        </div>
        <!--<div class="card" style="margin-bottom: 2rem; color: #777;">
         <div class="card-header">
          Year Level 1
         </div>
         <div class="card-body">
         <h5 class="card-title" style="color: #777"><strong style="color: #db0121">{itrs}</strong>|&nbsp;<u><i>{row.Last_Name}</i>, {row.First_Name} {row.Middle_Initial}</u></h5>
                <em><p class="card-text"><strong>Permanent Address:</strong> {row.Permanent_Address}</br>
                <strong>Current Address:</strong> {row.Local_Address}</br>
                <strong>Staying with Relatives?:</strong> {row.is_Staying_with_Family}</br>
                <strong>Staying with other SOM Students?:</strong> {row.is_Staying_with_SOM_Students}</br>
                <strong>Staying with:</strong> {row.is_Staying_With_Name}</br>
                <strong>Father's Name and No.:</strong> {row.Father_No}</br>
                <strong>Mother's Name and No.:</strong> {row.Mother_No}</br>
                <strong>Emergency Contact Person:</strong> {row.Emergency_Contact_Person}</br>
                <strong>Other Email Add:</strong> {row.Other_EmailAdd}</br>
                <strong>Mobile No.:</strong> {mobile}</br>
                <strong>PhilHealth?:</strong> {row.has_PhilHealth}</br>
                <strong>PhilHealth Category:</strong> {row.Philhealth_Category}</br>
                <strong>Other Medical Insurance?:</strong> {row.has_Other_Medical_Insurance}</br>
                <strong>Medical Insurances:</strong> {row.List_of_Other_Medical_Insurance}</br>
                <strong>Covid19 Vaccine?:</strong> {row.has_Covid19_Vaccine}</br>
                <strong>Covid19 Booster?:</strong> {row.has_Covid19_Booster}</br>
                </p></em>
                <a href="{row.Vaccine_Id}" class="btn btn-outline-dark {btn_state}">Vaccination ID/Certificate</a>
         </div>
        </div>-->
        """, unsafe_allow_html=True)

st.markdown(f"""
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
