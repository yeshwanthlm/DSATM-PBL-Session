# DSATM PBL Session

## Projects:

#,Project Name,Expanded Description,AWS Services Used
01,"Serverless ""Contact Us"" Form","Build a website contact form that triggers a backend process. When a user submits their name and email via a web interface, a Lambda function processes the data and sends a notification email to the admin.","Lambda, API Gateway, SES"
02,Automated Image Resizer,"Create a media pipeline. When an image is uploaded to a ""Source"" S3 bucket, a Lambda function is triggered to resize the image into a thumbnail and save it to a ""Processed"" bucket.","S3, Lambda, CloudWatch"
03,Cloud-Based Phonebook (CRUD),"Develop an application to manage student records. Users can add, view, update, and delete contact details through an API, teaching NoSQL database interactions and RESTful design.","DynamoDB, Lambda, API Gateway"
04,Text-to-Speech Converter,"Build a tool that converts written notes into audio. A student uploads a .txt file to S3, triggering a Lambda function to call Polly to synthesize the text into an MP3 file.","Amazon Polly, Lambda, S3"
05,Celebrity Face Detector,Use AI to identify famous personalities. Create an interface where an uploaded photo is analyzed by Rekognition to return the name and details of any recognized celebrities.,"Rekognition, Lambda, S3"
06,Global Portfolio Delivery,Host a personal portfolio website and ensure global speed. Secure the site with an SSL certificate and use a CDN to cache content at edge locations near users.,"S3, CloudFront, ACM"
07,Auto-Start/Stop Scheduler,"A cost-optimization project where a script or Lambda is scheduled to run at specific times (e.g., 9 AM and 6 PM) to automatically manage development EC2 instances.","EC2, Lambda, EventBridge"
08,Cloud Watchdog Billing Alarm,Set up proactive monitoring. Configure a CloudWatch alarm that tracks estimated charges and sends an immediate SMS or Email if the monthly spend exceeds a $5 threshold.,"CloudWatch, SNS"
09,Mass Email Automator,Automate college newsletters. Create a script that reads a list of student emails from a CSV in S3 and uses a verified email identity to send personalized bulk emails.,"Lambda, SES, S3"
10,Language Translator Bot,A simple translation utility. Build an API that accepts English text and uses AWS Machine Learning to provide an accurate translation into local languages like Hindi or Kannada.,"Amazon Translate, Lambda, API Gateway"
11,SQL Inventory Manager,"Set up a relational database for a ""Library"" system. Students provision a managed SQL database and run standard queries (SELECT, INSERT) from a remote script.",RDS (MySQL/PostgreSQL)
12,Resource Security Auditor,Write a Boto3 script that scans Security Groups and flags any that have port 22 (SSH) or 80 (HTTP) open to the entire internet (0.0.0.0/0).,"EC2, IAM, Boto3"
13,S3 File Explorer & Utility,"Create a Python-based CLI tool that allows users to list all files in an S3 bucket, see their sizes, and download them using the Boto3 SDK.","S3, Boto3, Python"
14,Custom Domain Setup,"Map a professional domain name to a cloud resource. Students learn to manage DNS records (A records, CNAMEs) to point a domain to an S3 website or EC2 instance.",Route 53
15,Serverless FAQ Chatbot,Build a conversational interface for college FAQs. Use a managed bot service to handle natural language understanding and trigger Lambda for data lookups.,"Amazon Lex, Lambda"
16,S3 Data Ingestion Pipeline,"Create a ""Data Lake"" entry point. When a JSON file is uploaded to S3, a Lambda function parses it and automatically inserts records into a DynamoDB table.","S3, Lambda, DynamoDB"
17,Secret Manager Vault Demo,"Security best practice: instead of hardcoding passwords in scripts, students learn to store credentials in a secure vault and fetch them programmatically.","Secrets Manager, Boto3"
18,Daily Motivational Quotes API,"A serverless API that serves content. Store quotes in DynamoDB and use an API call to fetch and return a ""Quote of the Day"" in JSON format.","DynamoDB, API Gateway, Lambda"
19,EC2 Health Reporter,"An automation script that generates a daily email report listing all running instances, their types, and their average CPU utilization over the last 24 hours.","EC2, CloudWatch, SNS, Boto3"
20,Secure Multi-User Login,"Add authentication to a web app. Use a managed user pool to allow students to ""Sign Up"" and ""Log In"" with email verification without managing a database.",Amazon Cognito
