import streamlit as st

def extract_emails(txt):
    wtxt = txt.split()
    emails = ''
    l = []
    for i in wtxt:
        if len(i) > 6 and '@' in i:
            l.append(i)

    for i in l:
        if i != l[-1]:
            emails += f'{i} ; '
        else:
            emails += f'{i}'
    
    return emails

def main():
    st.title("Email Extractor")
    st.write("Enter the text below to extract emails.")
    
    while True:
        txt = st.text_area('Paste the text here:')
        if st.button('Extract Emails'):
            extracted_emails = extract_emails(txt)
            st.write(f"Extracted emails: {extracted_emails}")
        cont = st.text_input('Do you want to continue? Type "n" to exit:')
        if cont.lower() == 'n':
            break

if __name__ == '__main__':
    main()
