# Serverless Resume Submission System (AWS)

A fully serverless resume submission platform built using AWS. This system allows candidates to upload resumes through a web interface, automatically stores files in S3, logs metadata in DynamoDB, and sends recruiter notifications using SES.

---

# Problem Statement

Manual resume collection through email is inefficient, unstructured, and difficult to track. Recruiters must manually download files, rename them, store them, and notify team members.

This project automates the entire resume intake workflow.

---

# Solution

This system provides:

- Web-based resume upload
- Automated file storage in S3
- Metadata tracking in DynamoDB
- Email notification using SES
- Serverless architecture using Lambda
- Secure frontend using CloudFront

---

# Architecture

User
→ CloudFront
→ Private S3 (Frontend)
→ API Gateway
→ Lambda
→ S3 (Resume Storage)
→ DynamoDB (Metadata)
→ SES (Email Notification)

(Architecture diagram added below)

---

# Features

- Serverless architecture
- Resume upload UI
- Email notifications
- Metadata tracking
- Secure file storage
- Scalable backend
- Private S3 frontend
- CloudFront CDN

---

# Technologies Used

AWS S3
AWS Lambda
AWS API Gateway
AWS DynamoDB
AWS SES
AWS CloudFront
HTML
CSS
JavaScript

---

# Workflow

1. User uploads resume
2. API Gateway receives request
3. Lambda processes file
4. Resume stored in S3
5. Metadata saved in DynamoDB
6. SES sends recruiter email

---

# Advantages

- Fully serverless
- Auto scalable
- Cost efficient
- No server management
- Secure storage
- Automated workflow

---

# Future Improvements

- Resume dashboard
- Authentication
- Resume parsing
- Search & filtering
- File validation
- Multi-file upload
- Admin panel

---

# Use Cases

HR resume collection
Internship application portal
College placement system
Job application intake
Document submission portal

---

# Author

Snehal Pawar

Cloud / AWS Project

---

# Deployment

Frontend hosted on:
CloudFront Distribution

Backend:
API Gateway + Lambda

Database:
DynamoDB

Storage:
Amazon S3

Notifications:
Amazon SES

---

# License

This project is for learning and demonstration purposes.
