# import streamlit as st
# import pandas as pd
# import logging
# from scraper import setup_driver, is_valid_url, scrape_profile, scrape_demo_profile
# from config import load_config
# from io import BytesIO

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# config = load_config()

# st.set_page_config(page_title="Resume Scraper by Divyam", page_icon="🤖")
# st.title("📋 Resume Intelligence Scraper")

# st.markdown("Upload an Excel file with Naukri profile links or use demo mode to test.")

# use_demo = st.checkbox("Use Demo Mode", value=True)
# uploaded_file = st.file_uploader("Upload Excel File (.xlsx)", type=["xlsx"])

# if uploaded_file or use_demo:
#     if use_demo:
#         df = pd.read_excel("demo_profiles.xlsx")
#     else:
#         df = pd.read_excel(uploaded_file)

#     st.write("### Input Data Preview", df.head())

#     if st.button("🔍 Start Scraping"):
#         email_list = []
#         phone_list = []

#         if use_demo:
#             for i in range(len(df)):
#                 email, phone = scrape_demo_profile(i)
#                 email_list.append(email)
#                 phone_list.append(phone)
#         else:
#             driver = setup_driver(
#                 config["driver_path"],
#                 config["user_data_dir"],
#                 config["profile_dir"],
#                 config["headless"],
#             )
#             for i in range(len(df)):
#                 url = df.iloc[i, 2]  # Assume 3rd column = profile link
#                 if is_valid_url(url):
#                     email, phone = scrape_profile(driver, url, config["wait_time"])
#                 else:
#                     email, phone = "Invalid URL", "Invalid URL"
#                 email_list.append(email)
#                 phone_list.append(phone)
#             driver.quit()

#         df["Email"] = email_list
#         df["Phone"] = phone_list

#         st.success("✅ Scraping Completed")
#         st.write("### Scraped Results", df)

#         from io import BytesIO

# # Prepare the Excel output
# output = BytesIO()
# df.to_excel(output, index=False, engine='openpyxl')
# output.seek(0)

# # Show download button
# st.download_button(
#     label="📥 Download Results as Excel",
#     data=output,
#     file_name="scraped_results.xlsx",
#     mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
# )

import streamlit as st
import pandas as pd
import logging
from scraper import setup_driver, is_valid_url, scrape_profile, scrape_demo_profile
from config import load_config
from io import BytesIO

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = load_config()

st.set_page_config(page_title="Resume Scraper by Divyam", page_icon="🤖")
st.title("📋 Resume Intelligence Scraper")

st.markdown("Upload an Excel file with Naukri-style profile links or use demo mode to test.")

use_demo = st.checkbox("✅ Demo Mode (Streamlit Cloud supports only this mode)", value=True)
uploaded_file = st.file_uploader("Upload Excel File (.xlsx)", type=["xlsx"])

if not use_demo:
    st.warning("⚠️ This hosted demo does not support real scraping. Upload is for feature visibility only.")

df = None
if use_demo:
    df = pd.read_excel("demo_profiles.xlsx")
elif uploaded_file:
    df = pd.read_excel(uploaded_file)

if df is not None:
    st.write("### 📄 Input Data Preview", df.head())

    if st.button("🔍 Start Scraping"):
        email_list = []
        phone_list = []

        if use_demo:
            for i in range(len(df)):
                email, phone = scrape_demo_profile(i)
                email_list.append(email)
                phone_list.append(phone)
        else:
            driver = setup_driver(
                config.get("driver_path"),
                config.get("user_data_dir"),
                config.get("profile_dir"),
                config.get("headless", True),
            )
            for i in range(len(df)):
                url = df.iloc[i, 2]  # Assume 3rd column = profile link
                if is_valid_url(url):
                    email, phone = scrape_profile(driver, url, config.get("wait_time", 2))
                else:
                    email, phone = "Invalid URL", "Invalid URL"
                email_list.append(email)
                phone_list.append(phone)
            driver.quit()

        df["Email"] = email_list
        df["Phone"] = phone_list

        st.success("✅ Scraping Completed")
        st.write("### 📊 Scraped Results", df)

        output = BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)

        st.download_button(
            label="📥 Download Results as Excel",
            data=output,
            file_name="scraped_results.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
