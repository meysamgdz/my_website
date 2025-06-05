# Portfolio Website

A modern Flask-based portfolio website showcasing my projects, skills, and contact information.  
Live demo: [meysam-goodarzi.com](https://meysamgdz.pythonanywhere.com) *(Replace with your actual URL)*

## Features

- **Responsive Design**: Works on desktop
- **Project Showcase**: Highlight key projects with descriptions and icons
- **Contact Form**: Email integration via Flask-Mail

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python, Flask
- **Deployment**: PythonAnywhere (or your hosting platform)
- **Tools**: Git, GitHub, VS Code

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```
### 2. Set up Virtal Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3. Install Depenedencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create `.env` file
```bas
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password  # For Gmail, use an "App Password"
```

### 5. Add Images
Add the folder `static/images` and copy your profile photo and logo of companies from which you have testimonies

### 6. Run the Development Server
```bash
flask run
```