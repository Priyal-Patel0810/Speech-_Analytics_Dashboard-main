# 🎧 Speech Analytics Dashboard

A full-stack application to transcribe and analyze customer call recordings using AWS Transcribe, S3, and NLP tools — deployed with Docker and provisioned via Terraform on AWS EC2.

---

## 🧠 Features

- Upload `.mp3` call recordings
- Store files in AWS S3
- Transcribe speech to text using AWS Transcribe
- Perform sentiment analysis using TextBlob
- Display results in a Streamlit-based dashboard
- Infrastructure provisioned using Terraform

---

## 🛠 Tech Stack

| Layer         | Technology                     |
|--------------|---------------------------------|
| Frontend     | Streamlit                       |
| Backend      | Python, Boto3, TextBlob         |
| Infra        | Docker, AWS EC2, Terraform      |
| NLP          | TextBlob (Sentiment Analysis)   |
| Cloud Services | AWS Transcribe, S3, IAM       |

---

## 🏗️ Architecture Overview

```plaintext
[User Uploads File] → [EC2 (Docker + Streamlit)] → [S3 Bucket]
                                                ↘
                                          [AWS Transcribe]
                                                ↘
                                      [TextBlob Sentiment Analysis]
                                                ↘
                                      [Dashboard: Transcription + Scores]
```

> EC2 instance is provisioned via Terraform with Docker, IAM role, and open port 8501. Streamlit app runs in a container.

---

## 📁 Project Structure

```bash
.
├── app/
│   ├── app.py               # Streamlit dashboard
│   ├── Dockerfile           # Docker image definition
│   └── requirements.txt     # Python dependencies
├── terraform/
│   ├── main.tf              # EC2, IAM, user_data
│   ├── variables.tf         # Input variables
│   ├── outputs.tf           # Outputs public IP
│   └── terraform.tfvars     # Actual key pair
```

---

## 🚀 Getting Started

### Prerequisites

- AWS account
- EC2 key pair created
- Terraform installed
- Docker installed

---

### 1️⃣ Provision Infrastructure

```bash
cd terraform/
terraform init
terraform plan
terraform apply -auto-approve
```

Copy the public IP output from Terraform after provisioning.

---

### 2️⃣ Deploy the App

```bash
# SSH into your EC2 instance
ssh -i your-key.pem ec2-user@<EC2_PUBLIC_IP>

# Install Docker (if not via user_data)
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user

# Clone the repo and run the app
git clone https://github.com/Akshat-kay/Speech-_Analytics_Dashboard.git
cd Speech-_Analytics_Dashboard/app
docker build -t speech-dashboard .
docker run -p 8501:8501 speech-dashboard
```

---

### 3️⃣ Access the App

Open your browser and visit:

```bash
http://<EC2_PUBLIC_IP>:8501
```

Upload an `.mp3` file and view results in real-time!

---

## 🔐 IAM Role

Ensure your EC2 instance has an IAM role attached with:
- `AmazonS3FullAccess`
- `AmazonTranscribeFullAccess`

---

## 📌 TODOs / Improvements

- ✅ Add automatic job cleanup for Transcribe
- 🟡 Replace TextBlob with spaCy + VADER for better accuracy
- 🟡 Add keyword/complaint extraction (NER)
- 🟡 CI/CD via GitHub Actions
- 🟢 Add HTTPS and authentication layer

---

## 📎 Related

- [AWS Transcribe Docs](https://docs.aws.amazon.com/transcribe/)
- [Streamlit](https://streamlit.io/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

Built with ❤️ to explore cloud-based NLP, AWS services, and DevOps best practices.
