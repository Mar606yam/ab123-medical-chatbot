# DOCY - Medical Chat-Doc Assistant 👩‍⚕️🩺

## Project Overview
This project is an end-to-end cloud-based medical chat assistant developed for **CISC 886 - Cloud Computing**. It leverages **AWS EMR** for big data preprocessing, **Google Colab (Unsloth)** for fine-tuning the **Llama-3-8B** model, and **AWS EC2** for deployment. 

## **Authors** 
YOMNA ALGENDY , YASMEEN ALGENDY , MARYAM ABDALBARY. 

## **NetIDs** 
25hcgx , 25bqdp , 25vrqw


---

##  Prerequisites
Before replicating this project, ensure you have:
- **AWS Account:** Access to S3, EMR, and EC2 (g4dn.xlarge recommended). 
- **Google Colab:** For fine-tuning with GPU (T4 or higher). 
- **Tools:** Hugging Face account (for model access), Ollama installed on EC2, and optionally Terraform for VPC provisioning. 
- **Region:** US East (N. Virginia) `us-east-1` is used for all resources. 

---

##  Project Architecture
- **Infrastructure:** Custom VPC, Public Subnets, and Security Groups (provisioned via AWS Console). 
- **Data Processing:** Apache Spark on AWS EMR (Configured for 20M+ records scale). 
- **Model:** Llama-3-8B-Instruct (Fine-tuned using QLoRA/PEFT). 
- **Deployment:** Ollama runner on AWS EC2 (g4dn.xlarge) with Open WebUI. 

---

##  Cost Summary Table 
| Service | Estimated Cost | Usage Description |
|---------|----------------|-------------------|
| S3      | $0.05          | Data & Script storage |
| EMR     | $0.50          | Spark Preprocessing step (Terminated after use) |
| EC2     | $1.20          | Model serving (g4dn.xlarge instance) |
| **Total**| **~$1.75** | |

---

##  Replication Steps
*(Steps will be added here following each phase of the project: VPC Setup -> EMR Preprocessing -> Fine-Tuning -> Deployment)*
