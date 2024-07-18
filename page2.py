import streamlit as st
from PIL import Image


def main():
    st.title("Business Card History")

    st.write("Here you can see the history of uploaded business cards.")

    # Placeholder for loading history data
    history = [
        {"name": "John Doe", "job_title": "Software Engineer", "company": "Tech Corp",
            "phone": "123-456-7890", "email": "john.doe@example.com", "website": "www.techcorp.com"},
        {"name": "Jane Smith", "job_title": "Project Manager", "company": "Business Solutions",
            "phone": "098-765-4321", "email": "jane.smith@bizsolutions.com", "website": "www.bizsolutions.com"}
    ]

    for entry in history:
        st.subheader(entry["name"])
        st.write(f"**Job Title:** {entry['job_title']}")
        st.write(f"**Company:** {entry['company']}")
        st.write(f"**Phone:** {entry['phone']}")
        st.write(f"**Email:** {entry['email']}")
        st.write(f"**Website:** {entry['website']}")


if __name__ == "__main__":
    main()
