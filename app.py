from flask import Flask
from datetime import datetime
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>DevOps Dashboard</title>

<style>

body {{
    margin:0;
    background:#111827;
    font-family:Segoe UI;
    color:white;
}}

.header {{
    background:#2563eb;
    padding:25px;
    text-align:center;
}}

.header h1 {{
    margin:0;
    font-size:42px;
}}

.container {{
    width:90%;
    margin:40px auto;
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
    gap:25px;
}}

.card {{
    background:#1f2937;
    border-radius:15px;
    padding:25px;
    text-align:center;
    box-shadow:0 0 15px rgba(0,0,0,.3);
}}

.card h2 {{
    color:#60a5fa;
}}

.success {{
    color:#22c55e;
    font-size:22px;
}}

.footer {{
    text-align:center;
    margin-top:40px;
    padding:20px;
    color:#94a3b8;
}}

</style>

</head>

<body>

<div class="header">
<h1>☁ AWS DevOps Dashboard</h1>
<p>Docker • GitHub • AWS EC2 • Flask</p>
</div>

<div class="container">

<div class="card">
<h2>Deployment Status</h2>
<p class="success">✅ SUCCESS</p>
</div>

<div class="card">
<h2>Cloud Platform</h2>
<p>Amazon EC2</p>
</div>

<div class="card">
<h2>Container</h2>
<p>🐳 Docker Running</p>
</div>

<div class="card">
<h2>Source Code</h2>
<p>GitHub Repository</p>
</div>

<div class="card">
<h2>Server Name</h2>
<p>{hostname}</p>
</div>

<div class="card">
<h2>Deployment Time</h2>
<p>{current_time}</p>
</div>

</div>

<div class="footer">
Created by <b>Rashmi Gujari</b> 🚀
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
