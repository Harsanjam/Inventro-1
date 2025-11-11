# Team members: Harsanjam Saini, Alexander Vicol, Terry Luan, Shubham Panchal

# Motivation

In many small and medium-sized businesses, inventory management is often handled through outdated software or manual spreadsheets that lack real-time synchronization, scalability, and reliability. These systems make it difficult to monitor stock levels accurately across distributed warehouses or retail locations. As a result, manual data entry and disconnected systems frequently lead to stockouts, overstocking, and data inconsistencies, all of which negatively affect operational efficiency and customer satisfaction.

While modern inventory management tools such as Zoho Inventory, Sortly, or Ordoro provide advanced functionality, they can cost hundreds of dollars per month, making them impractical for small teams and startups. Moreover, these third-party SaaS solutions are hosted externally, meaning users often lack full ownership and control over their data. For small businesses that prioritize affordability, customization, and privacy, this poses a significant limitation.

To address these challenges, the team is developing Inventa, a cloud-native, real-time inventory management system that is reliable, scalable, and self-hosted. Inventa leverages containerized microservices to ensure consistent performance, persistent cloud storage to maintain state across restarts and redeployments, and Kubernetes orchestration to provide automated scaling and fault tolerance. The system will also feature real-time communication and alerting mechanisms to reduce downtime and support faster, data-driven decision-making for managers and staff.

This project is worth pursuing because it demonstrates core cloud computing concepts including containerization, orchestration, CI/CD, monitoring, and persistence in a real-world business context. Invento not only provides hands-on experience with modern cloud technologies but also delivers tangible value by creating an affordable, customizable, and secure inventory management platform tailored to small and medium enterprises.

The target users are warehouse managers, retail operators, and staff in small to medium-sized businesses who require an accessible yet robust solution for tracking inventory across multiple locations. By giving users full control over their deployment, scalability, and data, Inventro bridges the gap between costly commercial platforms and limited manual systems, offering a practical, high-performance alternative that aligns with both business needs and modern cloud-native design principles.

# Objectives

The primary goal is to build and deploy a stateful, cloud-native web application that allows users to create, update, and track inventory items in real time. The system will use Digital Oceans Volumes, Django, and DigitalOceans Kubernetes (DOKS) to ensure persistent storage, secure access control, and proper data monitoring. The system will showcase the core principles of containerization, orchestration, persistence, and observability.

Inventro aims to provide a reliable, scalable, and self-hosted inventory management platform that gives users full control over their data while reducing operational costs. The project also fulfills ECE1779's technical learning objectives by integrating persistent storage, automated deployment pipelines, and real-time monitoring into a production-grade system.

## Core Features

### General Overview

### 1. User Authentication and Role-Based Access

- Users can register and log in securely using Django's authentication system.  
- Roles include Admin (full access), Manager (inventory access) and Staff (restricted access).

### 2. Inventory CRUD Operations

- Add, edit, delete, and view inventory items.  
- Each item includes fields such as name, category, quantity, location, and last updated.  
- There will be limited support for some bulk API's.

### 3. Database and Persistent Storage

- PostgreSQL hosted on DigitalOcean with Persistent Volume Claims (PVCs) for data persistence.  
- Ensures inventory data is retained even after container restarts or redeployments.

### 4. Containerization

- Application will be Dockerized using a Dockerfile (for Django) and docker-compose.yml (for local multi-container setup with PostGRESQL).

### 5. Orchestration and Deployment

- Deployed on DigitalOcean Kubernetes (DOKS).

- Includes Kubernetes Deployments, Services, and PersistentVolumeClaims (PVC).  
- Implemented Load Balancer Service for external access and scaling.

### 6. Monitoring and Observability

- Integrated DigitalOcean Metrics Dashboard to track CPU, memory, and disk usage.  
- Kubernetes logs for event tracing and debugging.  
- Optional: Basic Grafana dashboard for visual monitoring/analytics.

### 7. Optional Real-Time Features

- Real-time Stock Updates using Django Channels or WebSockets for live updates without refreshing the page.  
- Serverless email notifications (using DigitalOcean Functions + SendGrid) to alert managers of low-stock conditions.

## Architecture (Core Requirements)

### Frontend (user interface): 
- Bootstrap with server-rendered HTML templates + HTMX; only introduce a client-side component framework if we truly need richer interactivity (React if needed)  

### Backend (application server): 
- Python with the Django web framework; deployed using Gunicorn  

### Database: 
- PostgreSQL with persistent storage volumes on DigitalOcean Volumes (data remains intact across restarts and rolling updates)  

### Containerization: 
- Docker with Docker compose  

### Orchestration and Deployment: 

- DigitalOcean's fully managed Kubernetes service (DOKS)  

### Monitoring and Logs: 
- DigitalOcean metrics and alerts, plus Kubernetes logs

## ERD Diagram

![ERD diagram](assets/images/entity_relationships.png)

## Advanced Features

### 1. CI/CD Pipeline with GitHub Actions

- Automates the build, test, and deployment of Docker images to the DigitalOcean Container Registry and Kubernetes cluster.
- Enforces a consistent testing and deployment pipeline for faster iteration and reliable continuous delivery on each code change.

### 2. Automated PostgreSQL Backup (Kubernetes CronJob)

- Uses a scheduled Kubernetes job to automatically back up the PostgreSQL database at regular intervals.

- Stores backups securely in a DigitalOcean Spaces bucket and includes a documented restore procedure to ensure data reliability and recovery capability.

### 3. (Optional) Serverless Email Notifications for Low-Stock Alerts

- If time permits, use DigitalOcean Functions to trigger email alerts (via SendGrid API) when item quantity falls below a threshold.

### 4. (Optional) Web-socket based low-stock alerts that display in the browser in real time

## Risks and Failbacks

- Optional Features: Ensures proper workload.
- Test-Driven Development (TDD): Create tests in tandem with the development of features.
- Real-time complexity: If stability is an issue, limit live updates to the item-detail page and add a prominent "refresh" button to lists.  
- Search tuning: If full-text ranking takes too long, ship exact-match filters first and enable full-text search later behind a feature toggle.  
- Cluster complexity: If a multi-node cluster slows progress, use a single-node cluster with persistent storage while still demonstrating orchestration, health checks, and rolling updates.

## Fulfillment of Course Requirements

<table><tr><td>Requirement</td><td>Implementation in Project</td></tr><tr><td>Containerization &amp; Local Dev</td><td>Docker &amp; DockerCompose for Django + PostgreSQL setup</td></tr><tr><td>State Management</td><td>PostgreSQL with Persistent Volumes</td></tr><tr><td>Deployment Provider</td><td>DigitalOcean Kubernetes (DOKS)</td></tr><tr><td>Orchestration</td><td>Kubernetes Deployments, Services, PVCs</td></tr><tr><td>Monitoring</td><td>DigitalOcean Metrics Dashboard + K8s Logs</td></tr><tr><td>Advanced Features (≥2)</td><td>CI/CD with GitHub Actions, Automated Backups, optional WebSocket alerts</td></tr></table>

The project scope is realistic for a four-person team within the 5-week course timeline. Each team member will focus on one major subsystem (frontend, backend, architecture, and DevOps), enabling efficient parallel development. The system's modular design allows incremental feature integration while always maintaining full deployability. The optional features (serverless and WebSockets) will only be implemented if core milestones are achieved early. This approach ensures the team delivers a fully functional, containerized, and monitored stateful application by the due date while demonstrating mastery of all required course technologies.

This setup fully meets all course technical requirements while maintaining a realistic and achievable scope. Our objectives are specific and map directly to the ECE1779 course technologies. Our project is a containerized application with local development using Docker, DockerCompose, deployment on Kubernetes, PostgreSQL with persistent storage, provider monitoring, and at least two advanced features. Continuous integration + deployment, automated backups, and real-time alerts. The scope is intentionally sized for our team of four and project timeline.

# Tentative Plan

The team will follow Agile and Test-Driven Development (TDD) practices throughout the project to ensure iterative progress, continuous integration, and early detection of issues. The work will be divided into three main phases over the next several weeks, focusing on continuous functionality and deployability at every stage. Each member will maintain an independent branch for development while contributing to a shared staging environment on DigitalOcean Kubernetes.

## Phase 1: Foundation (Weeks 1-2)

Goal: Establish the base infrastructure, environment setup, and core backend logic.

### All Members:

- Collaborate on project structure, GitHub repository, and documentation.  
- Set up Docker and DockerCompose for local multi-container development.

### Member A – Frontend (Harsanjam Saini):

- Design the initial UI/UX layouts and HTML dashboard templates (Bootstrap).  
- Prototype user flows for login, dashboard, and item listing.

### Member B – Backend (Terry Luan):

- Set up Django backend with initial REST APIs and authentication endpoints.  
- Implement PostgreSQL schema and basic CRUD operations for inventory items.  
- Write unit tests for models and views.

### Member C - System Architecture (Alexander Vicol):

- Design database schema and configure DigitalOcean Persistent Volumes.  
- Implement role-based access control in Django.  
- Integrate metadata tracking for item creation and updates.

### Member D - DevOps (Shubham Panchal):

- Configure Dockerfile andCompose setup.  
- Initialize DigitalOcean Droplet and connect to the cluster.  
- Set up GitHub Actions for CI/CD pipeline and DigitalOcean registry.  
- Implement initial monitoring via DigitalOcean Metrics Dashboard.

### Minimum Deliverables:

- Local Dockerized setup for Django + PostgreSQL.  
- One functioning CRUD flow tested locally.  
- Basic authentication working via Django admin.

## Phase 2: Core Features (Weeks 3-4)

Goal: Deploy the application on Kubernetes and enable core course features.

### Member A – Frontend (Harsanjam):

- Connect frontend templates with live backend APIs.  
- Optional, if time permits: Add forms and dashboard widgets for real-time item management.

### Member B – Backend (Terry):

- Extend API endpoints for search and filtering.  
- Optional, if time permits: Implement email setup and stock threshold checks.  
- Optional, if time permits: Begin integration of Django Channels/WebSockets for real-time updates.

### Member C - System Architecture (Alex):

- Create database migration scripts and backup procedures.  
- Optimize PostgreSQL indexes for search and filtering.  
- Optional, if time permits: Implement serverless notification functions for low-stock alerts.

### Member D - DevOps (Shubham):

- Deploy the containerized app on DigitalOcean Kubernetes (DOKS).  
- Configure Deployments, Services, and PersistentVolumeClaims.  
- Implement Kubernetes CronJob for nightly PostgreSQL backups to DigitalOcean Spaces.

### Minimum Deliverables:

- Application running on Kubernetes cluster (staging).  
- Full CRUD flow (create  $\rightarrow$  edit  $\rightarrow$  view  $\rightarrow$  delete) operational in the cloud.  
- Automated CI/CD pipeline functional.  
- One working backup/restore test.

## Phase 3: Enhancement & Testing (Week 5)

Goal: Finalize advanced features, testing, and documentation for delivery.

### All Members:

- Conduct integration and usability testing.  
- Document setup, architecture, and deployment steps in README.  
- Record final demo walkthrough for presentation (see Appendix A)

### Member A - Frontend (Harsanjam):

- Polish UI  
- Help with other overflow tasks

### Member B - Backend (Terry):

- Finalize role-based permissions and refine error handling.

### Member C - System Architecture (Alex):

- Validate data persistence, backup, and restore workflows.

### Member D - DevOps (Shubham):

- Verify monitoring, metrics, and alert triggers.  
- Ensure CI/CD auto-deploys to production cluster without manual steps.

### Minimum Deliverables:

- Live, cloud-deployed application accessible externally.  
- Monitoring and backup/restore validated.  
- Documentation and presentation complete.

### Optional Features:

- OpenSearch integration  
- Web sockets integration for in-app notifications  
- Using serverless functions for email notifications

## Plan Justification

This plan is concise, achievable, and ownership-driven, ensuring that each team member has a defined role aligned with their strengths. By maintaining an always-functional system through CI/CD, automated testing, and containerization, the project can be completed within the course timeline, meeting all technical and advanced requirements.

By adhering to this structured yet flexible workflow, the team will confidently deliver a fully functional, containerized, and cloud-deployed inventory management system that meets all ECE1779 project requirements by the due date.

# Appendix

Demo Script (about one to three minutes)

1. Sign in as a manager and create a new item.  
2. Open a second browser session as a staff member and observe the new item appear in real time.  
3. Reduce the quantity below its threshold and show both the in-app notice and the received email.  
4. Open the monitoring dashboard and point out processor usage, restarts, and one alert.  
5. Show last night's backup in object storage and the restore steps written in theREADME.
