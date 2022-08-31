import utils
import streamlit as st

DUNE_KEY=st.secrets['dune_key']

st.title('Dune downloader')

query_id=st.number_input('Insert query ID',step=1,format='%d')

if st.button('Get info'):
    dune_data=utils.get_dune_data(query_id,DUNE_KEY)
    dune_data_csv = dune_data.to_csv(index=False).encode('utf-8')

    st.dataframe(dune_data)
    st.download_button(label='Download info',
                       data=dune_data_csv,
                       file_name=f'Query {query_id}.csv',
                       mime='text/csv')


