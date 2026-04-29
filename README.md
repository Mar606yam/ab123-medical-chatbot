# MY DOC - Medical Chat-Doc Assistant 🩺

## Project Overview
This project is an end-to-end cloud-based medical chat assistant developed for **CISC 886 - Cloud Computing**. [cite_start]It leverages **AWS EMR** for big data preprocessing, **Google Colab (Unsloth)** for fine-tuning the **Llama-3-8B** model, and **AWS EC2** for deployment. [cite: 133, 155]

**Author:** YOMNA ALGENDY , YASMEEN ALGENDY , MARYAM ABDALBARY. 
**NetID:** 25hcgx , 25bqdp , 25vrqw


---

## 🛠️ Prerequisites
Before replicating this project, ensure you have:
- [cite_start]**AWS Account:** Access to S3, EMR, and EC2 (g4dn.xlarge recommended). [cite: 162, 181]
- [cite_start]**Google Colab:** For fine-tuning with GPU (T4 or higher). [cite: 109]
- [cite_start]**Tools:** Hugging Face account (for model access), Ollama installed on EC2, and optionally Terraform for VPC provisioning. [cite: 106, 145, 181]
- [cite_start]**Region:** US East (N. Virginia) `us-east-1` is used for all resources. [cite: 162, 194]

---

## 🚀 Project Architecture
- [cite_start]**Infrastructure:** Custom VPC, Public Subnets, and Security Groups (provisioned via AWS Console). [cite: 144, 145]
- [cite_start]**Data Processing:** Apache Spark on AWS EMR (Configured for 20M+ records scale). [cite: 161]
- [cite_start]**Model:** Llama-3-8B-Instruct (Fine-tuned using QLoRA/PEFT). [cite: 155, 173]
- [cite_start]**Deployment:** Ollama runner on AWS EC2 (g4dn.xlarge) with Open WebUI. [cite: 180, 181]

---

## [cite_start]💰 Cost Summary Table 
| Service | Estimated Cost | Usage Description |
|---------|----------------|-------------------|
| S3      | $0.05          | Data & Script storage |
| EMR     | $0.50          | Spark Preprocessing step (Terminated after use) |
| EC2     | $1.20          | Model serving (g4dn.xlarge instance) |
| **Total**| **~$1.75** | |

---

## 🛠️ Replication Steps
[cite_start]*(Steps will be added here following each phase of the project: VPC Setup -> EMR Preprocessing -> Fine-Tuning -> Deployment)*
