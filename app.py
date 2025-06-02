import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from data.variable_values import projects, services, testimonials
from dotenv import load_dotenv

load_dotenv()

MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

if not MAIL_USERNAME or not MAIL_PASSWORD:
    raise ValueError("MAIL_USERNAME or MAIL_PASSWORD not set in environment")

app = Flask(__name__, template_folder='./templates')

# Email configuration
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_DEFAULT_SENDER=MAIL_USERNAME
)

mail = Mail(app)

@app.route('/')
def home_page():
    return render_template(
        'index.html',
        projects=projects,
        services=services,
        testimonials=testimonials
    )

@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    current_index = next((i for i, p in enumerate(projects) if p['id'] == project_id), None)
    if current_index is None:
        return render_template('404.html'), 404

    project = projects[current_index]
    prev_project = projects[current_index - 1] if current_index > 0 else None
    next_project = projects[current_index + 1] if current_index < len(projects) - 1 else None

    return render_template(
        'project_detail.html',
        project=project,
        prev_project=prev_project,
        next_project=next_project
    )

@app.route('/contact', methods=['POST'])
def contact_page():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    msg = Message(
        subject=f"New Contact Form Submission from {name}",
        sender=app.config['MAIL_USERNAME'],
        recipients=[app.config['MAIL_USERNAME']],
        body=f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
    )
    mail.send(msg)

    return redirect(url_for('thank_you_page'))

@app.route('/thank-you')
def thank_you_page():
    return render_template('thankyou.html')

@app.errorhandler(404)
def page_not_found_page(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
