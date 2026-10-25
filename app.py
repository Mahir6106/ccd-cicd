
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CloudLab | Cloud Computing & DevOps</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --bg: #0b1020;
            --card: #121a2d;
            --border: #26334c;
            --blue: #60a5fa;
            --text: #f1f5f9;
            --muted: #94a3b8;
            --green: #4ade80;
        }

        body {
            font-family: Inter, "Segoe UI", Arial, sans-serif;
            background:
                radial-gradient(ellipse at 80% 10%, #172554 0, transparent 40%),
                var(--bg);
            color: var(--text);
            min-height: 100vh;
        }

        a {
            color: inherit;
            text-decoration: none;
        }

        .container {
            max-width: 1120px;
            width: 90%;
            margin: auto;
        }

        nav {
            height: 76px;
            border-bottom: 1px solid #ffffff12;
            display: flex;
            align-items: center;
        }

        .nav-inner {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 11px;
            font-size: 21px;
            font-weight: 750;
            letter-spacing: -0.7px;
        }

        .logo {
            display: grid;
            place-items: center;
            width: 38px;
            height: 38px;
            border-radius: 12px;
            background: linear-gradient(135deg, #3b82f6, #6366f1);
            font-size: 21px;
        }

        .nav-right {
            display: flex;
            align-items: center;
            gap: 26px;
            color: var(--muted);
            font-size: 14px;
        }

        .status {
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--green);
            background: #4ade8010;
            border: 1px solid #4ade8030;
            padding: 9px 13px;
            border-radius: 30px;
            font-size: 12px;
            font-weight: 650;
        }

        .dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: var(--green);
            box-shadow: 0 0 12px #4ade8080;
        }

        .hero {
            padding: 88px 0 68px;
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 56px;
            align-items: center;
        }

        .eyebrow {
            color: var(--blue);
            text-transform: uppercase;
            letter-spacing: 2.5px;
            font-size: 11px;
            font-weight: 750;
            margin-bottom: 23px;
        }

        h1 {
            font-size: clamp(40px, 5vw, 62px);
            line-height: 1.08;
            letter-spacing: -2.7px;
            margin-bottom: 23px;
        }

        h1 span {
            color: var(--blue);
        }

        .intro {
            color: var(--muted);
            line-height: 1.8;
            font-size: 16px;
            max-width: 510px;
        }

        .actions {
            display: flex;
            flex-wrap: wrap;
            gap: 13px;
            margin-top: 31px;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 13px 18px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 700;
            transition: transform .2s, background .2s;
        }

        .btn:hover {
            transform: translateY(-2px);
        }

        .primary {
            background: #3b82f6;
            color: white;
            box-shadow: 0 8px 25px #3b82f630;
        }

        .secondary {
            border: 1px solid var(--border);
            background: #ffffff05;
        }

        .visual {
            min-height: 290px;
            padding: 27px;
            border-radius: 24px;
            border: 1px solid #ffffff18;
            background: linear-gradient(145deg, #182746, #101728);
            box-shadow: 0 25px 80px #00000030;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden;
        }

        .visual::before {
            content: "";
            position: absolute;
            width: 220px;
            height: 220px;
            background: #3b82f620;
            filter: blur(60px);
            border-radius: 50%;
        }

        .cloud {
            position: relative;
            font-size: 100px;
            filter: drop-shadow(0 0 25px #60a5fa60);
            margin-bottom: 25px;
        }

        .tech {
            position: relative;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 9px;
        }

        .tech span {
            font-size: 11px;
            color: #bfdbfe;
            border: 1px solid #60a5fa40;
            background: #3b82f618;
            border-radius: 30px;
            padding: 8px 12px;
        }

        .section-title {
            font-size: 19px;
            letter-spacing: -.4px;
            margin-bottom: 21px;
        }

        .metrics {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 17px;
            margin-bottom: 24px;
        }

        .metric, .api-card {
            background: #121a2dce;
            border: 1px solid var(--border);
            border-radius: 16px;
        }

        .metric {
            padding: 23px;
        }

        .metric-icon {
            width: 39px;
            height: 39px;
            border-radius: 11px;
            display: grid;
            place-items: center;
            background: #3b82f61c;
            color: var(--blue);
            font-size: 19px;
            margin-bottom: 19px;
        }

        .metric-label {
            font-size: 12px;
            color: var(--muted);
            margin-bottom: 8px;
        }

        .metric h3 {
            font-size: 16px;
            margin-bottom: 13px;
        }

        .healthy {
            color: var(--green);
            font-size: 12px;
        }

        .api-card {
            padding: 25px;
            margin: 17px 0 60px;
        }

        .api-top {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 15px;
            margin-bottom: 21px;
        }

        .api-top p {
            color: var(--muted);
            font-size: 13px;
            margin-top: 7px;
        }

        .get {
            color: var(--green);
            background: #4ade8012;
            border: 1px solid #4ade8030;
            border-radius: 6px;
            padding: 5px 9px;
            font-size: 11px;
            font-weight: 800;
            margin-right: 9px;
        }

        code {
            color: #bfdbfe;
            font-family: Consolas, monospace;
            font-size: 13px;
        }

        pre {
            background: #080e1b;
            border: 1px solid #26334c;
            border-radius: 12px;
            padding: 21px;
            overflow-x: auto;
            color: #c4b5fd;
            line-height: 1.9;
            font-size: 13px;
        }

        footer {
            border-top: 1px solid #ffffff12;
            padding: 22px 0;
            color: #64748b;
            font-size: 12px;
        }

        .footer-inner {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
        }

        @media (max-width: 760px) {
            .hero {
                grid-template-columns: 1fr;
                gap: 35px;
                padding: 58px 0;
            }

            .metrics {
                grid-template-columns: 1fr;
            }

            .nav-right > a {
                display: none;
            }

            h1 {
                letter-spacing: -1.7px;
            }

            .visual {
                min-height: 240px;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container nav-inner">
            <a class="brand" href="/">
                <span class="logo">☁</span>
                CloudLab
            </a>
            <div class="nav-right">
                <a href="/">Overview</a>
                <a href="#student">Student API</a>
                <span class="status"><span class="dot"></span> Service Online</span>
            </div>
        </div>
    </nav>

    <main class="container">
        <section class="hero">
            <div>
                <p class="eyebrow">Cloud Computing &amp; DevOps . BUILD 2</p>
                <h1>Your cloud lab,<br><span>beautifully deployed.</span></h1>
                <p class="intro">
                    A lightweight Flask microservice, containerized with Docker
                    and deployed on Kubernetes through an automated Jenkins CI/CD pipeline.
                </p>
                <div class="actions">
                    <a class="btn primary" href="#student">Explore student data →</a>
                    <a class="btn secondary" href="/student">View API response ↗</a>
                </div>
            </div>

            <div class="visual">
                <div class="cloud">☁️</div>
                <div class="tech">
                    <span>FLASK</span>
                    <span>DOCKER</span>
                    <span>KUBERNETES</span>
                    <span>JENKINS CI/CD</span>
                </div>
            </div>
        </section>

        <section>
            <h2 class="section-title">Deployment overview</h2>
            <div class="metrics">
                <article class="metric">
                    <div class="metric-icon">⌘</div>
                    <p class="metric-label">Application</p>
                    <h3>Flask Microservice</h3>
                    <span class="healthy">● Application configured</span>
                </article>
                <article class="metric">
                    <div class="metric-icon">▣</div>
                    <p class="metric-label">Container</p>
                    <h3>Docker Image</h3>
                    <span class="healthy">● Image built &amp; pushed</span>
                </article>
                <article class="metric">
                    <div class="metric-icon">◇</div>
                    <p class="metric-label">Orchestration</p>
                    <h3>Kubernetes</h3>
                    <span class="healthy">● Deployment verified</span>
                </article>
            </div>
        </section>

        <section class="api-card" id="student">
            <div class="api-top">
                <div>
                    <h2 class="section-title">Student endpoint preview</h2>
                    <p>Structured data served by your Flask API</p>
                </div>
                <div><span class="get">GET</span><code>/student</code></div>
            </div>
            <pre>{
  "name": "Student",
  "course": "Cloud Computing and DevOps"
}</pre>
        </section>
    </main>

    <footer>
        <div class="container footer-inner">
            <span>CloudLab · Cloud Computing &amp; DevOps Lab</span>
            <span>Flask · Docker · Kubernetes · Jenkins</span>
        </div>
    </footer>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE)


@app.route("/student")
def student():
    return jsonify({
        "name": "Student",
        "course": "Cloud Computing and DevOps"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


