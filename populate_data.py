import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pagination_project.settings')
django.setup()

from records.models import Record

# AI-generated sample data
titles = [
    "Project Alpha Launch", "Customer Feedback Analysis", "Q4 Budget Review",
    "Team Building Workshop", "Security Audit Report", "Mobile App Update",
    "Marketing Campaign Results", "Infrastructure Upgrade", "Sales Performance Review",
    "Product Roadmap Planning", "Client Onboarding Process", "Database Optimization",
    "User Experience Research", "Compliance Training", "Innovation Summit",
    "Partnership Agreement", "Technical Documentation", "Risk Assessment",
    "Performance Metrics Dashboard", "Employee Survey Results"
]

descriptions = [
    "Comprehensive analysis of project outcomes and key performance indicators.",
    "Detailed review of customer feedback and satisfaction metrics from Q3.",
    "Budget allocation and expense tracking for the upcoming quarter.",
    "Team collaboration exercises and professional development activities.",
    "Security vulnerabilities assessment and recommended improvements.",
    "New features and bug fixes for the mobile application version 2.0.",
    "ROI analysis and engagement metrics for recent marketing initiatives.",
    "System infrastructure improvements and scalability enhancements.",
    "Monthly sales targets achievement and team performance evaluation.",
    "Strategic planning for product development over the next 12 months.",
    "Streamlined processes for new client integration and setup.",
    "Database performance tuning and query optimization strategies.",
    "User research findings and recommendations for UI improvements.",
    "Mandatory compliance training modules and certification requirements.",
    "Innovation workshop outcomes and new project proposals.",
    "Legal review and finalization of strategic partnership terms.",
    "Updated technical documentation for API endpoints and integrations.",
    "Comprehensive risk analysis and mitigation strategies.",
    "Real-time dashboard implementation for KPI monitoring.",
    "Annual employee satisfaction survey results and action items."
]

categories = ["Business", "Technical", "Marketing", "HR", "Finance", "Operations"]

# Clear existing records
Record.objects.all().delete()

# Generate 60 records
for i in range(60):
    title = f"{random.choice(titles)} - {i + 1}"
    description = random.choice(descriptions)
    category = random.choice(categories)
    priority = random.randint(1, 5)

    # Random date within last 6 months
    days_ago = random.randint(0, 180)
    created_at = datetime.now() - timedelta(days=days_ago)

    Record.objects.create(
        title=title,
        description=description,
        category=category,
        priority=priority
    )

print("Successfully created 60 records!")
