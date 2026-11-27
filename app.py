import streamlit as st
import whisper
from groq import Groq
from streamlit_mic_recorder import mic_recorder
with open("style.css") as f:
    css=f.read()


    st.markdown(


        f"<style>{css}</style>",


        unsafe_allow_html=True


    )
model =whisper.load_model("base")
client = Groq (
    api_key=st.secrets["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"]
)

st.markdown(


    '<h1 class="main-title">🩺 Healthy Buddy</h1>',


    unsafe_allow_html=True


)


 
st.set_page_config(


    page_title="Healthy Buddy",


    page_icon="💪",


    layout="wide"


)


st.title("💪 Healthy Buddy")
col1, col2 = st.columns([5,1])


with col2:


    audio = mic_recorder(


        start_prompt="🎤",


        stop_prompt="⏹️",


        key="voice"


    )


if audio:


   


    with open("voice.wav", "wb") as f:


        f.write(audio["bytes"])


    result = model.transcribe("voice.wav")


    user_prompt = result["text"]


    st.write("🎤 You said:", user_prompt)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":user_prompt}]
    )


    answer = response["message"]["content"]


    st.write(answer)




if "messages" not in st.session_state:


    st.session_state.messages = []


with st.sidebar:


    st.header("📜 History")


    for message in st.session_state.messages:


        if message["role"] == "user":


            st.write("👤", message["content"][:30])


for message in st.session_state.messages:


    with st.chat_message(message["role"]):


        st.markdown(message["content"])


prompt = st.chat_input("Ask health related questions...")


if prompt:


    st.session_state.messages.append(


        {


            "role": "user",


            "content": prompt


        }


    )


    with st.chat_message("user"):


        st.markdown(prompt)
        st.write("thinking......")
        


    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[


            {


                "role": "system",


                "content": """


You are Healthy Buddy.


Understand:
- English

- Tanglish (Tamil written in English)

always reply in english 




Answer only health related questions.


Give diet recommendations.


Give fitness recommendations.


Give hydration guidance.


Be friendly.


"""


            },


            {


                "role": "user",


                "content": prompt


            }


        ]


    )


    answer = response["message"]["content"]


    with st.chat_message("assistant"):


        st.markdown(answer)


    st.session_state.messages.append(


        {


            "role": "assistant",


            "content": answer


        }


    )