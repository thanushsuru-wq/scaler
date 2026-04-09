import os

common_head = """<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Adaptive Clinical Trial Environment</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <link href="css/bootstrap-icons.css" rel="stylesheet">
        <link href="css/owl.carousel.min.css" rel="stylesheet">
        <link href="css/owl.theme.default.min.css" rel="stylesheet">
        <link href="css/templatemo-medic-care.css" rel="stylesheet">
        <style>
            .json-output {
                background: #f8f9fa;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-family: monospace;
                white-space: pre-wrap;
            }
        </style>
    </head>
    <body id="top">
"""

common_nav = """
        <main>
            <nav class="navbar navbar-expand-lg bg-light fixed-top shadow-lg">
                <div class="container">
                    <a class="navbar-brand mx-auto d-lg-none" href="index.html">
                        Trial AI
                        <strong class="d-block">Recruitment Specialist</strong>
                    </a>

                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>

                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav mx-auto">
                            <li class="nav-item">
                                <a class="nav-link" href="index.html">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="about.html">About Agent</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="trials.html">Active Trials</a>
                            </li>

                            <a class="navbar-brand d-none d-lg-block" href="index.html">
                                Trial AI
                                <strong class="d-block">Recruitment Specialist</strong>
                            </a>

                            <li class="nav-item">
                                <a class="nav-link" href="patients.html">Patients</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="assign.html">Evaluate & Assign</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
"""

common_footer = """
        </main>
        <footer class="site-footer section-padding" id="contact">
            <div class="container">
                <div class="row">
                    <div class="col-lg-5 me-auto col-12">
                        <h5 class="mb-lg-4 mb-3">AI Cluster Status</h5>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item d-flex">
                                Environment: Active
                            </li>
                            <li class="list-group-item d-flex">
                                Precision Matching: 99.8% Accuracy
                            </li>
                            <li class="list-group-item d-flex">
                                Capacity: Online
                            </li>
                        </ul>
                    </div>

                    <div class="col-lg-2 col-md-6 col-12 my-4 my-lg-0">
                        <h5 class="mb-lg-4 mb-3">System Access</h5>
                        <p><a href="mailto:admin@clinicaltrials.ai">admin@clinicaltrials.ai</a></p>
                        <p>Adaptive Trial Network Data Center</p>
                    </div>

                    <div class="col-lg-3 col-md-6 col-12 ms-auto">
                        <h5 class="mb-lg-4 mb-2">Socials</h5>
                        <ul class="social-icon">
                            <li><a href="#" class="social-icon-link bi-facebook"></a></li>
                            <li><a href="#" class="social-icon-link bi-twitter"></a></li>
                            <li><a href="#" class="social-icon-link bi-instagram"></a></li>
                            <li><a href="#" class="social-icon-link bi-youtube"></a></li>
                        </ul>
                        <div>
                            <p class="copyright-text">Copyright © Trial AI 2026</p>
                        </div>
                    </div>
                </div>
            </div>
        </footer>

        <!-- JAVASCRIPT FILES -->
        <script src="js/jquery.min.js"></script>
        <script src="js/bootstrap.bundle.min.js"></script>
        <script src="js/owl.carousel.min.js"></script>
        <script src="js/scrollspy.min.js"></script>
        <script src="js/custom.js"></script>
    </body>
</html>
"""

# Page specific contents
index_content = """
            <section class="hero" id="hero">
                <div class="container">
                    <div class="row">
                        <div class="col-12">
                            <div id="myCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel">
                                <div class="carousel-inner">
                                    <div class="carousel-item active">
                                        <img src="images/slider/portrait-successful-mid-adult-doctor-with-crossed-arms.jpg" class="img-fluid" alt="">
                                    </div>
                                    <div class="carousel-item">
                                        <img src="images/slider/young-asian-female-dentist-white-coat-posing-clinic-equipment.jpg" class="img-fluid" alt="">
                                    </div>
                                    <div class="carousel-item">
                                        <img src="images/slider/doctor-s-hand-holding-stethoscope-closeup.jpg" class="img-fluid" alt="">
                                    </div>
                                </div>
                            </div>
                            <div class="heroText d-flex flex-column justify-content-center">
                                <h1 class="mt-auto mb-2">
                                    Adaptive
                                    <div class="animated-info">
                                        <span class="animated-item">precision</span>
                                        <span class="animated-item">healthcare</span>
                                        <span class="animated-item">clinical trials</span>
                                    </div>
                                </h1>
                                <p class="mb-4">Autonomous Clinical Trial Recruitment Specialist. Maximizing trial enrollment efficiency with 100% adherence to patient eligibility criteria.</p>
                                <div class="heroLinks d-flex flex-wrap align-items-center">
                                    <a class="custom-link me-4" href="assign.html" data-hover="Start Assigning">Start Assigning</a>
                                    <p class="contact-phone mb-0"><i class="bi-diagram-3"></i> AI Environment Active</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

about_content = """
            <section class="section-padding" id="about">
                <div class="container" style="margin-top: 80px;">
                    <div class="row">
                        <div class="col-lg-6 col-md-6 col-12">
                            <h2 class="mb-lg-3 mb-3">Autonomous Specialist</h2>
                            <p><strong>Goal:</strong> Maximize trial enrollment efficiency while ensuring 100% adherence to patient eligibility criteria and prioritizing high-risk candidates.</p>
                            <p><strong>Environment:</strong> Adaptive Clinical Trial Recruitment Environment. Analyzes patient profiles against active clinical trials based on requirements, capacity limits, and diversity goals.</p>
                            <ul>
                                <li><strong>Precision Matching:</strong> Analyze medical history vs trial inclusion/exclusion criteria.</li>
                                <li><strong>Prioritization:</strong> Highlight "High-Risk" patients for urgent placement.</li>
                                <li><strong>Capacity Management:</strong> Strategic placement when trials near capacity.</li>
                            </ul>
                        </div>
                        <div class="col-lg-4 col-md-5 col-12 mx-auto">
                            <div class="featured-circle bg-white shadow-lg d-flex justify-content-center align-items-center">
                                <p class="featured-text"><span class="featured-number">100</span> %<br> Criteria Adherence</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

trials_content = """
            <section class="section-padding pb-0" id="timeline">
                <div class="container" style="margin-top: 80px;">
                    <div class="row">
                        <h2 class="text-center mb-lg-5 mb-4">Active Clinical Trials</h2>
                        <div class="timeline">
                            <div class="row g-0 justify-content-end justify-content-md-around align-items-start timeline-nodes">
                                <div class="col-9 col-md-5 me-md-4 me-lg-0 order-3 order-md-1 timeline-content bg-white shadow-lg">
                                    <h3 class="text-light">TRIAL-A01: CardioX</h3>
                                    <p><strong>Target:</strong> High-risk cardiovascular patients.<br><strong>Capacity:</strong> 45/50 slots filled.<br><strong>Criteria:</strong> Age > 50, History of hypertension. No contraindications for beta-blockers.</p>
                                </div>
                                <div class="col-3 col-sm-1 order-2 timeline-icons text-md-center"><i class="bi-heart-pulse timeline-icon"></i></div>
                                <div class="col-9 col-md-5 ps-md-3 ps-lg-0 order-1 order-md-3 py-4 timeline-date"><time>Phase 3 - Actively Recruiting</time></div>
                            </div>
                            <div class="row g-0 justify-content-end justify-content-md-around align-items-start timeline-nodes my-lg-5 my-4">
                                <div class="col-9 col-md-5 ms-md-4 ms-lg-0 order-3 order-md-1 timeline-content bg-white shadow-lg">
                                    <h3 class="text-light">TRIAL-B02: NeuroRegen</h3>
                                    <p><strong>Target:</strong> Early-stage Alzheimer's.<br><strong>Capacity:</strong> 12/100 slots filled.<br><strong>Criteria:</strong> Mild cognitive impairment. Strict demographic goals for diverse representation.</p>
                                </div>
                                <div class="col-3 col-sm-1 order-2 timeline-icons text-md-center"><i class="bi-diagram-2 timeline-icon"></i></div>
                                <div class="col-9 col-md-5 pe-md-3 pe-lg-0 order-1 order-md-3 py-4 timeline-date"><time>Phase 2 - Diverse Pool Needed</time></div>
                            </div>
                            <div class="row g-0 justify-content-end justify-content-md-around align-items-start timeline-nodes">
                                <div class="col-9 col-md-5 me-md-4 me-lg-0 order-3 order-md-1 timeline-content bg-white shadow-lg">
                                    <h3 class="text-light">TRIAL-C03: ImmunoBoost</h3>
                                    <p><strong>Target:</strong> Autoimmune disorder treatment.<br><strong>Capacity:</strong> FULL (Waitlist Open).<br><strong>Criteria:</strong> Documented autoimmune diagnosis, age 18-65.</p>
                                </div>
                                <div class="col-3 col-sm-1 order-2 timeline-icons text-md-center"><i class="bi-shield-check timeline-icon"></i></div>
                                <div class="col-9 col-md-5 ps-md-3 ps-lg-0 order-1 order-md-3 py-4 timeline-date"><time>Phase 1 - Capacity Reached</time></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

patients_content = """
            <section class="section-padding pb-0" id="reviews">
                <div class="container" style="margin-top: 80px;">
                    <div class="row">
                        <div class="col-12">
                            <h2 class="text-center mb-lg-5 mb-4">Patient Pool (Pending Assignment)</h2>
                            <div class="owl-carousel reviews-carousel">
                                <figure class="reviews-thumb d-flex flex-wrap align-items-center rounded">
                                    <p class="text-primary d-block mt-2 mb-0 w-100"><strong>Patient #8492</strong> - High Risk</p>
                                    <p class="reviews-text w-100">Age: 55<br>Condition: Severe Hypertension<br>Medications: ACE Inhibitors<br>Contraindications: None</p>
                                    <img src="images/reviews/senior-man-wearing-white-face-mask-covid-19-campaign-with-design-space.jpeg" class="img-fluid reviews-image" alt="">
                                    <figcaption class="ms-4"><strong>Status:</strong><span class="text-muted">Unassigned</span></figcaption>
                                </figure>
                                <figure class="reviews-thumb d-flex flex-wrap align-items-center rounded">
                                    <p class="text-primary d-block mt-2 mb-0 w-100"><strong>Patient #1120</strong></p>
                                    <p class="reviews-text w-100">Age: 32<br>Condition: Mild Autoimmune<br>Medications: Immunosuppressants<br>Contraindications: Allergy to Compound X</p>
                                    <img src="images/reviews/portrait-british-woman.jpeg" class="img-fluid reviews-image" alt="">
                                    <figcaption class="ms-4"><strong>Status:</strong><span class="text-muted">Unassigned</span></figcaption>
                                </figure>
                                <figure class="reviews-thumb d-flex flex-wrap align-items-center rounded">
                                    <p class="text-primary d-block mt-2 mb-0 w-100"><strong>Patient #4501</strong></p>
                                    <p class="reviews-text w-100">Age: 68<br>Condition: Mild Cognitive Impairment<br>Medications: None<br>Contraindications: Pacemaker</p>
                                    <img src="images/reviews/woman-wearing-mask-face-closeup-covid-19-green-background.jpeg" class="img-fluid reviews-image" alt="">
                                    <figcaption class="ms-4"><strong>Status:</strong><span class="text-muted">Unassigned</span></figcaption>
                                </figure>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

assign_content = """
            <section class="section-padding" id="booking">
                <div class="container" style="margin-top: 80px;">
                    <div class="row">
                        <div class="col-lg-8 col-12 mx-auto">
                            <div class="booking-form">
                                <h2 class="text-center mb-lg-3 mb-2">Evaluate & Assign Patient</h2>
                                <form role="form" id="agent-form">
                                    <div class="row">
                                        <div class="col-lg-6 col-12">
                                            <input type="text" id="patient_id" class="form-control" placeholder="Patient ID (e.g. #8492)" required>
                                        </div>
                                        <div class="col-lg-6 col-12">
                                            <select id="trial_id" class="form-control" required>
                                                <option value="" disabled selected>Select Trial</option>
                                                <option value="TRIAL-A01">TRIAL-A01: CardioX (45/50)</option>
                                                <option value="TRIAL-B02">TRIAL-B02: NeuroRegen (12/100)</option>
                                                <option value="TRIAL-C03">TRIAL-C03: ImmunoBoost (Waitlist)</option>
                                                <option value="NONE">No Match / Reject</option>
                                            </select>
                                        </div>
                                        <div class="col-12">
                                            <textarea class="form-control" rows="3" id="reasoning" placeholder="Agent Reasoning (e.g., patient meets all criteria and has no contraindications)" required></textarea>
                                        </div>
                                        <div class="col-lg-6 col-md-6 col-12 mx-auto">
                                            <button type="submit" class="form-control" id="submit-button">Execute Action</button>
                                        </div>
                                    </div>
                                </form>
                                <div class="mt-4">
                                    <h5>Environment Output Data (JSON)</h5>
                                    <div id="json-output" class="json-output">{ "status": "waiting for input..." }</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <script>
                    document.addEventListener("DOMContentLoaded", function() {
                        const form = document.getElementById("agent-form");
                        const jsonOutput = document.getElementById("json-output");
                        
                        form.addEventListener("submit", function(e) {
                            e.preventDefault();
                            
                            const patientId = document.getElementById("patient_id").value;
                            const trialId = document.getElementById("trial_id").value;
                            const reasoning = document.getElementById("reasoning").value;
                            
                            let action = "reject_candidate";
                            let payload = { patient_id: patientId, reasoning: reasoning };
                            
                            if (trialId === "TRIAL-C03") {
                                action = "waitlist_patient";
                                payload.trial_id = trialId;
                            } else if (trialId && trialId !== "NONE") {
                                action = "assign_to_trial";
                                payload.trial_id = trialId;
                            }
                            
                            const response = {
                                timestamp: new Date().toISOString(),
                                action: action,
                                payload: payload
                            };
                            
                            jsonOutput.textContent = JSON.stringify(response, null, 4);
                        });
                    });
                </script>
            </section>
"""

files = {
    "index.html": index_content,
    "about.html": about_content,
    "trials.html": trials_content,
    "patients.html": patients_content,
    "assign.html": assign_content
}

base_path = r"c:\Users\thanu\OneDrive\Desktop\medic-care"

for filename, content in files.items():
    full_path = os.path.join(base_path, filename)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(common_head + common_nav + content + common_footer)
        
print("HTML pages generated successfully.")
