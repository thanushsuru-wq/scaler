import os

base_template = """<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Adaptive Clinical Trial Environment</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
        <link href="{{ url_for('static', filename='css/bootstrap.min.css') }}" rel="stylesheet">
        <link href="{{ url_for('static', filename='css/bootstrap-icons.css') }}" rel="stylesheet">
        <link href="{{ url_for('static', filename='css/owl.carousel.min.css') }}" rel="stylesheet">
        <link href="{{ url_for('static', filename='css/owl.theme.default.min.css') }}" rel="stylesheet">
        <link href="{{ url_for('static', filename='css/templatemo-medic-care.css') }}" rel="stylesheet">
        <style>
            .json-output { background: #f8f9fa; padding: 15px; border: 1px solid #ddd; border-radius: 5px; font-family: monospace; white-space: pre-wrap; }
            .nav-link { font-weight: 600; }
            .chatbot-btn { position: fixed; bottom: 20px; right: 20px; z-index: 9999; border-radius: 50px; padding: 15px 25px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); }
        </style>
    </head>
    <body id="top">
        <main>
            <nav class="navbar navbar-expand-lg bg-light fixed-top shadow-lg">
                <div class="container">
                    <a class="navbar-brand mx-auto d-lg-none" href="{{ url_for('home') }}">Trial AI <strong class="d-block">Recruitment Specialist</strong></a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav mx-auto">
                            <li class="nav-item"><a class="nav-link" href="{{ url_for('home') }}">Home</a></li>
                            <li class="nav-item"><a class="nav-link" href="{{ url_for('trials') }}">Active Trials</a></li>
                            <li class="nav-item"><a class="nav-link" href="{{ url_for('prescription') }}">OpenCV Prescription Scan</a></li>
                            
                            <a class="navbar-brand d-none d-lg-block" href="{{ url_for('home') }}">Trial AI <strong class="d-block">Recruitment Specialist</strong></a>
                            
                            <li class="nav-item"><a class="nav-link" href="{{ url_for('assign') }}">Evaluate Dashboard</a></li>
                            {% if session.get('user_id') %}
                                <li class="nav-item"><a class="nav-link shadow-sm bg-primary text-white rounded px-3 ms-2" href="{{ url_for('logout') }}">Logout ({{ session.get('username') }})</a></li>
                            {% else %}
                                <li class="nav-item"><a class="nav-link shadow-sm bg-primary text-white rounded px-3 ms-2" href="{{ url_for('login') }}">Login</a></li>
                            {% endif %}
                        </ul>
                    </div>
                </div>
            </nav>
            
            {% with messages = get_flashed_messages() %}
              {% if messages %}
                <div class="container mt-5 pt-5">
                    {% for message in messages %}
                        <div class="alert alert-info">{{ message }}</div>
                    {% endfor %}
                </div>
              {% endif %}
            {% endwith %}

            {% block content %}{% endblock %}
        </main>

        <a href="{{ url_for('chat_ui') }}" class="btn btn-primary chatbot-btn"><i class="bi-chat-dots-fill"></i> AI Chatbot</a>

        <footer class="site-footer section-padding" id="contact">
            <div class="container">
                <div class="row">
                    <div class="col-lg-5 me-auto col-12">
                        <h5 class="mb-lg-4 mb-3">AI Cluster Status</h5>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item d-flex">Environment: Active Flask Server</li>
                            <li class="list-group-item d-flex">Algorithms: OpenCV Morphological Thresholding</li>
                            <li class="list-group-item d-flex">Database: SQLite Ready</li>
                        </ul>
                    </div>
                    <div class="col-lg-2 col-md-6 col-12 my-4 my-lg-0">
                        <h5 class="mb-lg-4 mb-3">System Access</h5>
                        <p><a href="mailto:admin@clinicaltrials.ai">admin@clinicaltrials.ai</a></p>
                    </div>
                    <div class="col-lg-3 col-md-6 col-12 ms-auto">
                        <p class="copyright-text">Copyright © Trial AI 2026</p>
                    </div>
                </div>
            </div>
        </footer>
        <script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
        <script src="{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>
        <script src="{{ url_for('static', filename='js/owl.carousel.min.js') }}"></script>
        <script src="{{ url_for('static', filename='js/scrollspy.min.js') }}"></script>
        <script src="{{ url_for('static', filename='js/custom.js') }}"></script>
    </body>
</html>
"""

templates = {
    "base.html": base_template,
    "index.html": """{% extends "base.html" %}
{% block content %}
<section class="hero" id="hero">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <div id="myCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel">
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="{{ url_for('static', filename='images/slider/portrait-successful-mid-adult-doctor-with-crossed-arms.jpg') }}" class="img-fluid" alt="">
                        </div>
                    </div>
                </div>
                <div class="heroText d-flex flex-column justify-content-center">
                    <h1 class="mt-auto mb-2">
                        Adaptive <div class="animated-info"><span class="animated-item">precision</span></div>
                    </h1>
                    <p class="mb-4">Welcome to the advanced Clinic portal. Now powered by OpenCV and ML models to extract Doctor's Prescription data reliably, alongside an internal AI Chatbot for communication.</p>
                    <div class="heroLinks d-flex flex-wrap align-items-center">
                        <a class="custom-link me-4" href="{{ url_for('prescription') }}" data-hover="Upload Prescription">Upload Prescription</a>
                        <p class="contact-phone mb-0"><i class="bi-diagram-3"></i> Authenticated Environment</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock %}
""",
    "login.html": """{% extends "base.html" %}
{% block content %}
<section class="section-padding" style="margin-top: 80px;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-6 col-12">
                <h2 class="text-center mb-4">Portal Login</h2>
                <div class="booking-form">
                    <form method="POST" action="{{ url_for('login') }}">
                        <input type="text" name="username" class="form-control mb-3" placeholder="Username" required>
                        <input type="password" name="password" class="form-control mb-3" placeholder="Database Password" required>
                        <button type="submit" class="btn btn-primary w-100 mb-3">Authenticate</button>
                        <p class="text-center"><a href="{{ url_for('register') }}">Don't have an account? Register Here.</a></p>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock %}
""",
    "register.html": """{% extends "base.html" %}
{% block content %}
<section class="section-padding" style="margin-top: 80px;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-6 col-12">
                <h2 class="text-center mb-4">Register Account</h2>
                <div class="booking-form">
                    <form method="POST" action="{{ url_for('register') }}">
                        <input type="text" name="username" class="form-control mb-3" placeholder="Create Username" required>
                        <input type="password" name="password" class="form-control mb-3" placeholder="Create Password" required>
                        <button type="submit" class="btn btn-primary w-100 mb-3">Save to SQLite DB</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock %}
""",
    "prescription.html": """{% extends "base.html" %}
{% block content %}
<section class="section-padding" style="margin-top: 80px;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8 col-12">
                <h2 class="text-center mb-4">Doctor's Prescription Scan</h2>
                <p class="text-center text-muted">Upload a medical image. OpenCV will threshold & process the image, then pass it to the ML Recommendation Engine.</p>
                <div class="booking-form">
                    <form method="POST" action="{{ url_for('prescription') }}" enctype="multipart/form-data">
                        <input type="file" name="file" class="form-control mb-3" accept="image/*" required>
                        <button type="submit" class="btn btn-primary w-100 mb-3">Run OpenCV Pipeline</button>
                    </form>
                </div>
                
                {% if recommendation %}
                <div class="card mt-5 shadow-sm border-primary">
                    <div class="card-header bg-primary text-white">
                        <strong>AI/ML Extraction Results</strong>
                    </div>
                    <div class="card-body">
                        <p class="card-text">{{ recommendation }}</p>
                    </div>
                </div>
                {% endif %}
            </div>
        </div>
    </div>
</section>
{% endblock %}
""",
    "chat.html": """{% extends "base.html" %}
{% block content %}
<section class="section-padding" style="margin-top: 80px;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8 col-12">
                <h2 class="text-center mb-4">AI Specialist Chatbot</h2>
                <div class="card shadow-lg border-0">
                    <div class="card-body" id="chat-box" style="height: 400px; overflow-y: auto; background: #fdfdfd;">
                        <div class="mb-3">
                            <strong class="text-primary">Chatbot AI:</strong> Hi there! I am the environment's communication agent. How can I assist?
                        </div>
                    </div>
                    <div class="card-footer bg-white border-0">
                        <form id="chat-form">
                            <div class="input-group">
                                <input type="text" id="user_input" class="form-control" placeholder="Ask me about algorithms or trials...">
                                <button type="submit" class="btn btn-primary">Send Message</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<script>
    document.getElementById('chat-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const userInput = document.getElementById('user_input').value;
        if (!userInput) return;
        
        const chatBox = document.getElementById('chat-box');
        chatBox.innerHTML += `<div class="mb-3 text-end"><strong class="text-secondary">You:</strong> ${userInput}</div>`;
        document.getElementById('user_input').value = '';
        
        fetch('{{ url_for("api_chat") }}', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userInput })
        })
        .then(res => res.json())
        .then(data => {
            chatBox.innerHTML += `<div class="mb-3"><strong class="text-primary">Chatbot AI:</strong> ${data.reply}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        });
    });
</script>
{% endblock %}
""",
    "trials.html": """{% extends "base.html" %}
{% block content %}
<section class="section-padding pb-0" id="timeline" style="margin-top: 80px;">
    <div class="container">
        <div class="row">
            <h2 class="text-center mb-lg-5 mb-4">Active Database Trials</h2>
            <div class="timeline">
                <div class="row g-0 justify-content-end justify-content-md-around align-items-start timeline-nodes">
                    <div class="col-9 col-md-5 me-md-4 me-lg-0 order-3 order-md-1 timeline-content bg-white shadow-lg">
                        <h3 class="text-light">TRIAL-A01: CardioX</h3>
                        <p>Our Neural Network identified high demand here.</p>
                    </div>
                    <div class="col-3 col-sm-1 order-2 timeline-icons text-md-center"><i class="bi-heart-pulse timeline-icon"></i></div>
                    <div class="col-9 col-md-5 ps-md-3 ps-lg-0 order-1 order-md-3 py-4 timeline-date"><time>Phase 3</time></div>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock %}
""",
    "assign.html": """{% extends "base.html" %}
{% block content %}
<section class="section-padding" id="booking" style="margin-top: 80px;">
    <div class="container">
        <h2 class="text-center mb-4">Evaluate & Assign via Python Kernel</h2>
        <div class="booking-form">
            <form role="form" id="agent-form">
                <div class="row">
                    <div class="col-lg-6 col-12"><input type="text" id="patient_id" class="form-control" placeholder="Patient ID (e.g. #8492)" required></div>
                    <div class="col-lg-6 col-12">
                        <select id="trial_id" class="form-control" required>
                            <option value="TRIAL-A01">TRIAL-A01: CardioX</option>
                            <option value="NONE">Reject</option>
                        </select>
                    </div>
                    <div class="col-12"><textarea id="reasoning" class="form-control" rows="3" placeholder="AI reasoning" required></textarea></div>
                    <div class="col-lg-6 col-md-6 col-12 mx-auto"><button type="submit" class="btn btn-primary w-100">Send to Environment</button></div>
                </div>
            </form>
            <div class="mt-4 json-output" id="json-output">{ "status": "standing by" }</div>
        </div>
    </div>
</section>
<script>
    document.getElementById('agent-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const pid = document.getElementById('patient_id').value;
        document.getElementById('json-output').textContent = JSON.stringify({ action: 'process_started', patient: pid }, null, 4);
    });
</script>
{% endblock %}
"""
}

base_path = r"C:\Users\thanu\OneDrive\Desktop\medic-care\templates"
os.makedirs(base_path, exist_ok=True)

for filename, content in templates.items():
    with open(os.path.join(base_path, filename), "w", encoding="utf-8") as f:
        f.write(content)

print("Jinja2 templates compiled securely to templates/ directory.")
