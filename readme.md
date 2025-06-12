# Django Pagination Project

A Django web application demonstrating pagination functionality with AI-generated sample data.

## 🚀 Features

- Django-based web application with pagination
- 60+ AI-generated sample records
- Clean, responsive UI with navigation controls
- Displays 10 records per page
- Admin interface for data management
- Sorting by creation date (newest first)

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Latjor-Wuon/pagination_project.git
   cd pagination_project
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Populate sample data**
   ```bash
   python populate_data.py
   ```
   This will create 60 sample records with various categories and priorities.

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

## 🏃‍♂️ Running the Application

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - Main application: http://localhost:8000/records/
   - Admin interface: http://localhost:8000/admin/

## 📁 Project Structure

```
pagination_project/
├── manage.py
├── populate_data.py
├── pagination_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── records/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── records/
            └── record_list.html
```

## 📊 Data Model

### Record Model
- **title**: CharField (max 200 characters)
- **description**: TextField
- **category**: CharField (Business, Technical, Marketing, HR, Finance, Operations)
- **priority**: IntegerField (1-5)
- **created_at**: DateTimeField (auto-generated)

## 🎨 Features Demonstration

### Pagination Controls
- **First/Last**: Navigate to first or last page
- **Previous/Next**: Navigate between adjacent pages
- **Page Info**: Shows current page and total pages
- **Responsive Design**: Works on desktop and mobile devices

### Sample Data Categories
- Business
- Technical
- Marketing
- HR
- Finance
- Operations

## 🧪 Testing

Run the Django development server and verify:
1. Records are displayed 10 per page
2. Navigation controls work correctly
3. Page information is accurate
4. Records are sorted by creation date (newest first)

## 🔧 Customization

### Change Items Per Page
In `records/views.py`, modify the paginator:
```python
paginator = Paginator(records, 10)  # Change 10 to desired number
```

### Modify Styling
Edit the CSS in `records/templates/records/record_list.html`

### Add More Fields
1. Update the model in `records/models.py`
2. Run migrations
3. Update the template to display new fields

## 📝 Admin Interface

Access the Django admin at `/admin/` to:
- View all records
- Add/Edit/Delete records
- Filter by category, priority, or date
- Search records by title or description

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is created for educational purposes as part of the ALU BSE program.

## 👥 Author

- **Name**: Latjor Wuon
- **Email**: l.dak@alustudent.com
- **GitHub**: [@Latjor-Wuon](https://github.com/Latjor-Wuon)

## 🙏 Acknowledgments

- Django documentation
- ALU BSE program
- AI tools for generating sample data