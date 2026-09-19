# 📄 Serverless Resume Submission System — AWS

![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?logo=amazonaws&logoColor=white)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?logo=awslambda&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon-S3-569A31?logo=amazons3&logoColor=white)
![API Gateway](https://img.shields.io/badge/Amazon-API%20Gateway-FF4F8B?logo=amazonaws&logoColor=white)
![DynamoDB](https://img.shields.io/badge/Amazon-DynamoDB-4053D6?logo=amazondynamodb&logoColor=white)
![CloudFront](https://img.shields.io/badge/Amazon-CloudFront-FF9900?logo=amazonaws&logoColor=white)

> A serverless resume submission platform built with AWS that automates resume storage, metadata tracking, and recruiter email notifications.

---

## 📌 Project Overview

This project demonstrates a serverless workflow for collecting resumes through a web-based interface.

Instead of manually collecting and organizing resume files, the system automates the submission process using AWS managed services.

When a candidate submits a resume:

1. The request is received through **API Gateway**.
2. **AWS Lambda** processes the submission.
3. The resume is stored in **Amazon S3**.
4. Submission metadata is recorded in **Amazon DynamoDB**.
5. **Amazon SES** sends a recruiter notification.

The frontend is delivered through **Amazon CloudFront** with the frontend files stored in a private S3 bucket.

---

# 🎯 Problem Statement

Manual resume collection through email can result in:

- Unstructured submissions
- Manual file management
- Difficult metadata tracking
- Repetitive recruiter notifications
- Increased administrative effort

This project demonstrates how a serverless AWS architecture can automate the resume intake workflow.

---

# 🏗️ Architecture

### High-Level Architecture

```text
                         Candidate
                            │
                            ▼
                      Amazon CloudFront
                            │
                            ▼
                   Private S3 Frontend
                            │
                            ▼
                     Amazon API Gateway
                            │
                            ▼
                       AWS Lambda
                      /     |      \
                     /      |       \
                    ▼       ▼        ▼
              Resume S3  DynamoDB    SES
                 │          │         │
                 ▼          ▼         ▼
             Resume      Metadata   Recruiter
             Storage     Tracking   Notification
````

### Architecture Flow

```text
User
  │
  ▼
CloudFront
  │
  ▼
Private S3
  │
  ▼
API Gateway
  │
  ▼
Lambda
  ├──────────────► S3 Resume Storage
  │
  ├──────────────► DynamoDB Metadata
  │
  └──────────────► SES Email Notification
```

---

# ⚙️ AWS Services Used

| AWS Service        | Purpose                             |
| ------------------ | ----------------------------------- |
| Amazon S3          | Frontend hosting and resume storage |
| Amazon CloudFront  | Frontend content delivery           |
| Amazon API Gateway | Receives resume submission requests |
| AWS Lambda         | Processes the submission workflow   |
| Amazon DynamoDB    | Stores resume submission metadata   |
| Amazon SES         | Sends recruiter email notifications |

---

# 💻 Frontend Technologies

The web interface is built using:

* HTML
* CSS
* JavaScript

The frontend is delivered through Amazon CloudFront.

---

# 🔄 Resume Submission Workflow

### Step 1 — Candidate Submission

The candidate accesses the resume submission interface through CloudFront.

### Step 2 — API Request

The submission is sent to an API Gateway endpoint.

### Step 3 — Lambda Processing

AWS Lambda processes the incoming request.

### Step 4 — Resume Storage

The submitted resume is stored in Amazon S3.

### Step 5 — Metadata Storage

Submission metadata is recorded in DynamoDB.

### Step 6 — Recruiter Notification

Amazon SES sends an email notification to the recruiter.

```text
Candidate
   │
   ▼
Web Interface
   │
   ▼
API Gateway
   │
   ▼
Lambda
   ├──► S3
   ├──► DynamoDB
   └──► SES
```

---

# 🔐 Storage & Delivery

The architecture uses separate S3 responsibilities:

### Frontend S3

Stores the static frontend files.

The frontend is delivered through:

```text
Private S3 → CloudFront → User
```

### Resume S3

Stores submitted resume files.

```text
Lambda → Resume S3
```

### Metadata

Submission metadata is stored separately in DynamoDB.

```text
Lambda → DynamoDB
```

---

# 📂 Project Documentation

The project includes an architecture diagram in:

```text
Documentation.pdf
```

The document provides additional details about the implemented AWS architecture.

---

# 🚀 Deployment Components

### Frontend

```text
Amazon S3
      │
      ▼
Amazon CloudFront
```

### Backend

```text
API Gateway
      │
      ▼
AWS Lambda
```

### Database

```text
Amazon DynamoDB
```

### Resume Storage

```text
Amazon S3
```

### Notifications

```text
Amazon SES
```

---

# 🌟 Key Features

* ☁️ Serverless AWS architecture
* 📄 Web-based resume submission
* 📦 Automated resume storage in S3
* 🗃️ Metadata tracking with DynamoDB
* 📧 Recruiter email notifications using SES
* 🌐 CloudFront-based frontend delivery
* 🔄 Automated serverless workflow
* 📈 AWS-managed scalable architecture
* 🖥️ No traditional application server required

---

# 🧠 Key Concepts Practiced

This project provided hands-on practice with:

* AWS serverless architecture
* Amazon S3
* AWS Lambda
* API Gateway
* DynamoDB
* Amazon SES
* Amazon CloudFront
* Event-driven application workflow
* Static frontend delivery
* Cloud-based document storage
* Automated notification workflows

---

# 📈 Advantages

### Serverless

The application uses managed AWS services instead of maintaining traditional application servers.

### Scalability

The architecture uses AWS managed services designed to handle changing workloads.

### Automation

Resume storage, metadata tracking, and notifications are handled automatically.

### Reduced Infrastructure Management

There is no traditional backend server to maintain for the workflow.

### Centralized Data

Resume files and submission metadata are stored in dedicated AWS services.

---

# 🔮 Future Improvements

Potential improvements include:

* 📊 Resume management dashboard
* 🔐 User authentication
* 📑 Automated resume parsing
* 🔎 Resume search and filtering
* ✅ File type and size validation
* 📁 Multi-file upload support
* 👨‍💼 Admin panel

These features are **not part of the current implementation** and are listed as future enhancements.

---

# 🛠️ Example Use Cases

The architecture can be adapted for:

* HR resume collection
* Internship application portals
* College placement systems
* Job application intake
* Document submission portals

---

# 👨‍💻 Author

## Snehal Pawar

**Aspiring DevOps Engineer | AWS & Cloud**

AWS | Linux | Docker | Kubernetes | Terraform | Jenkins | CI/CD

* GitHub: [snehalpawar29](https://github.com/snehalpawar29)
* LinkedIn: [Snehal Pawar](https://www.linkedin.com/in/snehalpawar29/)
* Portfolio: [DevOps Portfolio](https://snehalpawar29.github.io/Snehal-Pawar-Devops-Portfolio/)

---

# 📜 License

This project is created for **learning and demonstration purposes**.

---

<p align="center">

### ☁️ Learn by Building • Automate • Deploy • Improve 🚀

</p>
