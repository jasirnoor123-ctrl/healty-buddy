from pypdf import PdfReader

import ollama

# PDF files

pdf_files = [

    "diabete_guide.pdf",

    "cancer_guide.pdf",

    "ulcer_guide.pdf"

]

# Load all PDF text

all_text = ""

for pdf in pdf_files:

    reader = PdfReader(pdf)

    for page in reader.pages:

        text = page.extract_text()

        if text:

            all_text += text + "\n"

print("✅ PDFs Loaded Successfully")

# Chat Loop

while True:

    question = input("\nAsk your question: ")

    if question.lower() == "exit":

        break

    prompt = f"""

You are Healthy Buddy.

Answer only from the medical information below.

DOCUMENT:

{all_text[:20000]}

QUESTION:

{question}

ANSWER:

"""

    response = ollama.chat(

        model="llama3",

        messages=[

            {

                "role": "user",

                "content": prompt

            }

        ]

    )

    print("\n🤖 Answer:")

    print(response["message"]["content"])