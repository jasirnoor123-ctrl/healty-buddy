from pyngrok import ngrok
url=ngrok.connect(8501)
print("public url:")
print(url)