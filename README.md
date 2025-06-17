🕌 **Zakat Buddy (Beta) – AI-Powered Zakat & Quranic Ayah Guide**


Zakat Buddy is a basic AI prototype that helps calculate your approximate zakat and fetches a Quranic verse about charity. It's currently a light version, not a full Islamic zakat calculator, but will be upgraded soon with more accurate logic and proper Urdu support, in sha Allah.



📌 Current Status:

⚠️ Note: This is not a complete or fully shariah-compliant zakat system.

It simply provides a quick overview using fixed gold/silver prices and does not cover all zakat rules.

Urdu language support is under development and may not display properly for now.




✨ **What It Does (So Far)**:

🧮 Estimates zakat payable from your basic asset info

📖 Fetches a random relevant Quranic verse about zakat or charity

🗣️ Supports English, and soon Urdu

🤖 Uses OpenRouter models via LiteLLM

🧱 Built with clean, modular Python code using OOP


🛠️ **Stack**:

- Area	Tools Used

- AI Models	OpenRouter ( Mistral, deepseek)

- Logic	Python, OOP
- Interfaces Chainlit (chat UI)
- Project Mgmt	uv / venv

🚀 **How to Use**

# Clone repo and install
git clone https://github.com/yourusername/zakat-buddy-app.git
cd zakat-buddy-app
uv venv
uv pip install -r requirements.txt


# Add your .env file:

OPENROUTER_API_KEY=your_key_here


# Then run:
chainlit run main.py



**📂Project Structure**:
# zakat-buddy-app/
├── agents/
├── prompts/
├── zakat_utils.py
├── config.py
├── app_streamlit.py
├── app_chainlit.py
└── .env


**📅 Planned Features**:


✅ More accurate zakat calculator (proper nisab, categories, lunar year tracking)

🧾 Multiple types of zakatable assets

🌐 Full Urdu translation and formatting

📊 Nisab calculator from real-time gold/silver prices

📚 Hadith-based explanations

🔒 Data privacy options (local-only mode)




❤️ **A Note From the Maker**:

- This is a faith-driven side project by a student developer exploring AI and Islamic tech.

- It's still work-in-progress — please use respectfully and provide feedback.

- I'm building this to help myself and others learn. More coming soon, In shaa Allah. 🌙

- Educational & personal use only. Not intended for fatwa or official zakat assessment.


build by Khadija 








