# 🛠️ doc2md-api - Convert Documents to Markdown Easily

## 🎉 Overview
Welcome to doc2md-api! This application allows you to turn various document formats into Markdown with ease. Whether you need to convert DOCX, PDF, PPTX, or images, doc2md-api has you covered. Built using Python with FastAPI and Microsoft MarkItDown, it provides a secure way to manage files and offers a health check endpoint to ensure everything runs smoothly.

## 📦 Download & Install
To get started, visit our GitHub Releases page to download the latest version of doc2md-api:

[![Download doc2md-api](https://img.shields.io/badge/Download-doc2md--api-blue)](https://github.com/airiseworks/doc2md-api/releases)

1. Click on the link above.
2. You will see a list of available releases.
3. Find the latest version and download the appropriate file for your system.

## 🚀 Getting Started
After downloading, follow these steps to set up and run the application:

### 1. Install Docker
doc2md-api is packaged for Docker, making it easy to run without needing to set up a local environment. If you don't have Docker installed, follow these instructions:

- Visit the [Docker installation guide](https://docs.docker.com/get-docker/) to download and install Docker on your system.
- Follow the prompts to complete the installation.

### 2. Run the Application
Once Docker is installed, you can run doc2md-api using the command line. Here’s how:

1. Open your command prompt or terminal.
2. Pull the latest doc2md-api image:
   ```bash
   docker pull airiseworks/doc2md-api
   ```
3. Run the application with the following command:
   ```bash
   docker run -d -p 8000:8000 airiseworks/doc2md-api
   ```

### 3. Access the API
After running the command, the API will be accessible at `http://localhost:8000`. You can now use it to convert your documents. 

## 🔑 Using the API
To use the API for document conversion, you will need an API key. Follow these steps:

1. **Get Your API Key:** Make sure to obtain an API key from your administrator or through your account settings.
2. **Setting the Key in the Header:** When making a request to the API, you’ll need to include your key in the header. Use `X-API-Key` as your header key.

### Example Request
Here is how you can make a request to convert a document:

```plaintext
POST http://localhost:8000/convert
Headers:
    X-API-Key: your_api_key
Body:
    {
        "input_file": "path/to/your/document.docx",
        "output_format": "markdown"
    }
```

### Health Check
You can verify that the service is running correctly by accessing the health check endpoint:

```
GET http://localhost:8000/health
```

A successful response will confirm that the API is up and running.

## 📄 Supported Formats
doc2md-api can convert the following document types to Markdown:

- DOCX (Word Documents)
- PDF (Portable Document Format)
- PPTX (PowerPoint Presentations)
- Images (JPG, PNG, etc.)
- XLSX (Excel Spreadsheets)

## 💻 System Requirements
To run doc2md-api without issues, ensure your system meets the following requirements:

- Docker installed
- Minimum of 2 GB of RAM
- Stable internet connection (for downloads and API usage)

## 📃 Additional Information
For more detailed information about each endpoint, including parameters and expected responses, please refer to the [API Documentation](https://github.com/airiseworks/doc2md-api#api-docs).

## ❓ Frequently Asked Questions

### Q: What do I do if I encounter issues?
A: Please check the issues section on our GitHub page for reports and solutions. If you still need help, open a new issue, and our team will assist you.

### Q: Can I contribute to this project?
A: We welcome contributions! Please check our contribution guidelines in the repository for details.

## 📧 Contact
For support or inquiries, feel free to reach out via the GitHub repository or contact the project maintainers through the listed channels.

Happy converting! Enjoy using doc2md-api to simplify your document processing tasks.