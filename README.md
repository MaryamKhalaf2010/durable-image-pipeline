# Durable Workflow for Image Metadata Processing 📸

**Course**: CST8917 – Serverless Cloud Apps  
**Assignment**: A1 – Durable Workflow for Image Metadata Processing  
**Student**: Maryam Khalaf  
**Date**: July 19, 2025  

---

##  Objective

To build a serverless image metadata processing pipeline using **Azure Durable Functions in Python** that automatically processes and stores metadata of images uploaded to Azure Blob Storage.

---

##  Scenario

A fictional content moderation team needs to analyze image metadata. This app performs the following automatically:

1. **Triggers** on new blob uploads (.jpg, .png, .gif).
2. **Extracts metadata**: file name, size, width, height, format.
3. **Stores metadata** in an **Azure SQL Database** using output bindings.

---

##  Architecture Overview

- **Blob Trigger Function**: Watches `images-input` container.
- **Orchestrator Function**: Coordinates the flow.
- **ExtractMetadataActivity**: Reads blob properties using Azure SDK and Pillow.
- **StoreMetadataActivity**: Writes to Azure SQL DB via output binding.

---

##  Folder Structure

```
durable-image-pipeline/
│
├── BlobTriggerFunction/           # Blob-trigger client
├── ExtractMetadataActivity/      # Activity function to extract metadata
├── OrchestratorFunction/         # Durable orchestrator
├── StoreMetadataActivity/        # Activity function to store metadata
├── local.settings.json           # Local config
├── requirements.txt              # Python dependencies
├── host.json                     # Host configuration
├── proxies.json                  # (if used)
└── README.md                     # This file
```

---

##  Azure Resources Used

- **Azure Blob Storage** – `images-input` container
- **Azure Functions App** – Python (v4)
- **Azure SQL Database** – `imagemetadatadb` on `maryam-sqlserver`
- **Azure Durable Functions** – Orchestration

---

##  SQL Table Schema

```sql
CREATE TABLE dbo.metadata (
    id INT IDENTITY(1,1) PRIMARY KEY,
    fileName NVARCHAR(255),
    fileSizeKB FLOAT,
    width INT,
    height INT,
    format NVARCHAR(50),
    created_at DATETIME DEFAULT GETDATE()
);
```
## SQL Table Schema-Confirmed metadata extraction via logs

```sql 
SELECT * FROM dbo.metadata;

);
```
---

##  Demo Video

[![YouTube Demo](https://img.shields.io/badge/Watch-Demo%20Video-red?style=for-the-badge&logo=youtube)](https://youtu.be/YOUR_VIDEO_LINK)

---

##  Results

- Metadata correctly extracted and logged.
- Data successfully inserted into Azure SQL DB.
- Blob trigger and orchestration working end-to-end.

---

##  Developed by

**Maryam Khalaf**  
Cloud Development and Operations Student  
[LinkedIn](https://www.linkedin.com/in/maryam-khalaf)