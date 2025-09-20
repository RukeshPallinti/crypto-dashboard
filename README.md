📊 Cryptocurrency Dashboard (INR)

This is a crypto dashboard I built in PyCharm using Streamlit.  
The main idea was to track the top 5 cryptocurrencies in INR and visualize them in an interactive way.  
I kept it lightweight so it’s easy to run locally and can be extended later.

# ✨ What it does

\- Shows live data for the top 5 coins (prices in INR).  
\- Interactive charts to check price trends.  
\- Uses Streamlit for the dashboard and Plotly/Seaborn for visuals.  
\- Simple and clean UI – focused on functionality.

# 🛠️ Tech I used

\- Python 3.9+  
\- Streamlit (for the dashboard)  
\- Pandas & NumPy (for data handling)  
\- Plotly & Seaborn (for charts)  
\- PyCharm (where I developed this project)

# 📂 Project structure

crypto-dashboard/  
│-- dashboard.py -> Main Streamlit app  
│-- requirements.txt -> All dependencies  
│-- data/ -> (Optional, if I want to cache or save data)  
│-- README.docx -> This file

# ⚙️ How to run it

1\. Clone the repo:  
git clone https://github.com/RukeshPallinti/crypto-dashboard.git 
cd crypto-dashboard   
<br/>2\. (Optional) Create a virtual environment:  
python -m venv venv  
source venv/bin/activate # On Windows: venv\\Scripts\\activate  
<br/>3\. Install dependencies:  
pip install -r requirements.txt  
<br/>4\. Run the app:  
streamlit run dashboard.py  
<br/>The dashboard will open in your browser at: 👉 <http://localhost:8501>


# 🔮 Things I want to add later

\- Support for more coins + multiple fiat currencies (USD, EUR, etc.)  
\- Add analytics like moving averages or volatility.  
\- Deploy to Streamlit Cloud or Heroku so it’s accessible online.  
\- Add a dark mode option.
