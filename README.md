# 🌟 Positivity Reframer

A Streamlit chatbot that takes any **negative thought** and rewrites it into something **positive** — powered by **LLaMA 3.3 70B** via the Groq API.

## ✨ What It Does

Type a negative sentence → get a 2-line positive reframe back instantly.

**Example:**
> *"I failed my exam."*
> → *"Every failure teaches you something new. You now know exactly what to work on."*

## 🛠 Tech Stack
- Python + Streamlit
- Groq API (LLaMA 3.3 70B via Cloudflare Gateway)
- python-dotenv

## 📦 Setup

```bash
# 1. Clone the repo
git clone https://github.com/Akashhh739/Chatbot.git
cd Chatbot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your API key
cp example.env .env
# Then edit .env and add your GROQ_API_KEY

# 4. Run
streamlit run main.py
```

## 🔑 Environment Variables

Create a `.env` file based on `example.env`:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your Groq API key at [console.groq.com](https://console.groq.com)
