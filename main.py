import os
import sys
import typesense
import streamlit as st

curr_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, os.path.abspath(os.path.join(curr_dir, os.pardir)))


client = typesense.Client({
    'api_key': 'xyz',
    'nodes': [{
        'host': 'typesense',
        'port': '8108',
        'protocol': 'http'
    }],
    'connection_timeout_seconds': 2
})


def search(query):
    res = client.collections['routines'].documents.search({
        'q': query,
        'query_by': 'Dokumentnavn, Søkeord, Dokumentansvarlig, Revisjonsansvarlig',
        "collection": "routines"
    })
    return res


# Streamlit UI
def main():
    st.title("Simple Search App")
    
    # Input for search query
    query = st.text_input("Enter your search query:")
    
    # Perform search when search button is clicked
    if st.button("Search"):
        if query:
            results = search(query)
            st.write("Search Results: " + str(results["found"]))
            if results["found"] > 0:
                for result in results["hits"]:
                    st.header(result["document"]["Dokumentnavn"])
                    st.write(result["document"]["Dokument-ID"])
                    st.write(result["document"]["Godkjenner"])
            else:
                st.write("No results found.")

if __name__ == "__main__":
    main()