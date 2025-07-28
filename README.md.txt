# 📋 Resume Intelligence Extractor (Demo Mode)

This is a demo-mode Streamlit web app that simulates intelligent contact information extraction from online resumes or job portal profiles.

🧠 Originally built as an automation tool using Selenium and Excel, this app was redesigned to be:
- GUI-based
- Demo-safe (no real scraping, just emulated data)
- Resume/portfolio-ready

---

## 💡 What It Does

- Takes an Excel file with fake Naukri-style profile links
- Simulates scraping contact data (email & phone)
- Displays results in the browser
- Allows downloading updated Excel with new columns

---

## 🎯 Tech Used

- Python
- Streamlit (for GUI)
- Pandas / OpenPyXL
- YAML for config
- Regex logic for URL validation
- (Optional) Selenium for real scraping in backend version

---

## 🚀 Try It Live

You can try the hosted demo version here:  
👉 [https://automated-scraper-divyam.streamlit.app/] 

---

## 🧪 Demo-Only Mode (Why?)

Since Naukri.com profiles are private, this version only simulates the scraping logic.  
It uses fake but realistic contact info so that recruiters and viewers can see the scraping flow without requiring login or actual browser automation.

---

## 📁 File Structure

- `gui.py` → Main Streamlit app
- `scraper.py` → Contains simulated scraping logic
- `demo_profiles.xlsx` → Input file for demo
- `requirements.txt` → Streamlit, pandas, etc.

---

## 🙋 About This Project

This was built by [Divyam] as part of learning applied data automation — originally created to help a friend extract recruiter data, and later converted into a GUI-based demo for showcasing web scraping, pipeline thinking, and tool-building capability.

If you're a recruiter or engineer evaluating this, feel free to clone and test it. All logic is modular and real scraping can be re-enabled if needed.

---
