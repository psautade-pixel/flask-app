from flask import Flask
app = Flask(__name__)
@app.route(&quot;/&quot;)
def home():
return &quot;Hello World from Cloud ��&quot;
if __name__ == &quot;__main__&quot;:
app.run()