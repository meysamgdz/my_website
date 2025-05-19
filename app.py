# app.py
from flask import Flask, render_template, request, redirect, url_for
from data.variable_values import projects, services, testimonials
from flask_mail import Mail, Message
from dotenv import dotenv_values

app = Flask(__name__, template_folder='./templates')

# Email configuration (replace with your actual credentials)
config = dotenv_values(".env")
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = config['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = config['MAIL_PASSWORD']

mail = Mail(app)


@app.route('/')
def home_page():
    return render_template('index.html', projects=projects)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/projects')
def project_page():
    return render_template('projects.html', projects=projects)


@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    # Find the index of the current project
    current_index = next((i for i, p in enumerate(projects) if p['id'] == project_id), None)

    if current_index is None:
        return render_template('404.html'), 404

    project = projects[current_index]

    # Get previous project if exists
    prev_project = projects[current_index - 1] if current_index > 0 else None

    # Get next project if exists
    next_project = projects[current_index + 1] if current_index < len(projects) - 1 else None

    return render_template(
        'project_detail.html',
        project=project,
        prev_project=prev_project,
        next_project=next_project
    )


# Add these new routes to your existing app.py
@app.route('/services')
def service_page():
    return render_template('services.html', services=services)

@app.route('/testimonials')
def testimonial_page():
    return render_template('testimonials.html', testimonials=testimonials)


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Construct and send the email
        msg = Message(
            subject=f"New Contact Form Submission from {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']],  # Where you want to receive it
            body=f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        )
        mail.send(msg)

        return redirect(url_for('thank_you_page'))

    return render_template('contact.html')



@app.route('/thank-you')
def thank_you_page():
    return render_template('thankyou.html')


@app.errorhandler(404)
def page_not_found_page(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)