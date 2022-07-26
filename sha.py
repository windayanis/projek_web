import streamlit as st
import hashlib

def sha():
    input_text = st.text_area("Masukan text")
    choice = st.selectbox("SHA :", ["SHA256","SHA384","SHA224","SHA512","SHA1"])
    col1,col2 = st.columns([14,1])
    with col2:
        if st.button("Hash"):
            if len(input_text) == 0:
                with col1:
                    st.error("Masukan Text!")
            else:
                if choice == "SHA256":
                    result = hashlib.sha256(input_text.encode())
                    with col1:
                        st.info(result.hexdigest())
                if choice == "SHA384":
                    result = hashlib.sha384(input_text.encode())
                    with col1:
                            st.info(result.hexdigest()) 
                if choice == "SHA224":
                    result = hashlib.sha224(input_text.encode())
                    with col1:
                        st.info(result.hexdigest())
                if choice == "SHA512":
                    result = hashlib.sha512(input_text.encode())
                    with col1:  
                        st.info(result.hexdigest())
                if choice == "SHA1":
                    result = hashlib.sha1(input_text.encode())
                    with col1:
                        st.info(result.hexdigest())
