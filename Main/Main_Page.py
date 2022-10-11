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
    <div class="card" style="width: 18rem;">
        <div class="card-header">
            Featured
        </div>
        <ul class="list-group list-group-flush">
            <li class="list-group-item">
                <button type="button" class="btn btn-primary">
                    1st Year <span class="badge text-bg-secondary">{len(rows1)}</span>
                </button>
            </li>
            <li class="list-group-item">A second item</li>
            <li class="list-group-item">A third item</li>
        </ul>
    </div>
""", unsafe_allow_html=True)
st.write("1st Yr",len(rows1))
st.write("2nd Yr",len(rows2))
st.write("3rd Yr",len(rows3))

st.markdown(f"""
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
