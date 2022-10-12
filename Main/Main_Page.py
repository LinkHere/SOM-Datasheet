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

st.markdown(f"""
<!--    <div class="card" style="width: 18rem; color: #777;">
#        <div class="card-header">
#            Students
#        </div>
#        <ul class="list-group list-group-flush" style="color: #777;">
#            <li class="list-group-item">
#                <h6>1st Year <span class="badge bg-secondary">{len(rows1)}</span></h6>
#            </li>
#            <li class="list-group-item">
#                <h6>2nd Year <span class="badge bg-secondary">{len(rows2)}</span></h6>
#            </li>
#            <li class="list-group-item">
#                <h6>3rd Year <span class="badge bg-secondary">{len(rows3)}</span></h6>
#            </li>
#        </ul>
#    </div>-->

<div class="row" style="margin-bottom: 15px; color: #777;">
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title" style="color: #777;">1st Year Students</h5>
        <p class="card-text" style="color: #777;"><h6>Found: <span class="badge bg-danger">{len(rows1)}</span></h6></p>
        <p class="card-text">👈 <em>Click on the sidebar</em></p>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title" style="color: #777;">Special title treatment</h5>
        <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
</div>

<div class="row" style="color: #777;">
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title" style="color: #777;">Special title treatment</h5>
        <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title" style="color: #777;">Special title treatment</h5>
        <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
