# LlamaPal Chat

LlamaPal Chat is a web-based chat application that uses the Llama 3.1 AI model to generate responses. This repository contains the source code for setting up and running the chat application.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Hardware Requirements](#hardware-requirements)
- [Setup](#setup)
  - [Linux](#linux)
  - [Windows](#windows)
- [Running the Application](#running-the-application)
- [Setting Up ngrok](#setting-up-ngrok)
- [Usage](#usage)
- [Contributing](#contributing)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- Flask
- Markdown
- Ollama
- ngrok
- Any additional Python packages specified in `requirements.txt`

## Hardware Requirements

To run Llama 3.1 efficiently, your system should meet the following hardware requirements:

- **Processor**: Intel Core i7 or AMD Ryzen 7 or better
- **Memory**: 16 GB RAM or more
- **Graphics Card (GPU)**: NVIDIA RTX 2080 or better (for hardware acceleration)
- **Operating System**: Windows 10 64-bit, Ubuntu 18.04 or higher
- **Storage**: SSD with at least 50 GB free space

### Example System Configuration

Below is the configuration of the system used to run this application:

- **Processor**: AMD Ryzen 9 5900HS, 3301 Mhz, 8 Core(s), 16 Logical Processor(s)
- **Memory**: 16 GB RAM
- **Graphics Card (GPU)**: NVIDIA GeForce RTX 3060 GPU
- **Operating System**: Windows 10 Pro 64-bit
- **Storage**: 512 GB SSD

## Setup

### Linux

1. Clone the Repository
    ```sh
    git clone https://github.com/manudeepp/llama_3_1_app.git
    cd llama_3_1_app
    ```
2. Create and Activate a Virtual Environment
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install Dependencies
    ```sh
    pip install -r requirements.txt
    ```
4. Install Llama 3.1 using Ollama
    Follow the instructions on the [Ollama website](https://ollama.com/library/llama3.1) to install Ollama. After installing Ollama, download and install Llama 3.1 with the following command:
    ```sh
    ollama install llama3.1
    ```

### Windows

1. Clone the Repository
    ```sh
    git clone https://github.com/manudeepp/llama_3_1_app.git
    cd llama_3_1_app
    ```
2. Create and Activate a Virtual Environment
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```
3. Install Dependencies
    ```sh
    pip install -r requirements.txt
    ```
4. Install Llama 3.1 using Ollama
    Follow the instructions on the [Ollama website](https://ollama.com/library/llama3.1) to install Ollama. After installing Ollama, download and install Llama 3.1 with the following command:
    ```sh
    ollama install llama3.1
    ```

## Running the Application

1. Start the Flask Application
    ```sh
    python app.py
    ```
    The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Setting Up ngrok

ngrok allows you to expose a local server to the internet securely. Follow the steps below to set up ngrok:

1. Download ngrok
    Visit the [ngrok](https://ngrok.com/) website and download the appropriate version for your operating system.

2. Install ngrok
    Follow the installation instructions provided on the ngrok website.

3. Start ngrok
    ```sh
    ngrok http 5000
    ```
    ngrok will provide a forwarding URL that you can use to access your local server from anywhere.

## Usage

1. Open your web browser and navigate to the ngrok forwarding URL provided in the previous step.
2. Enter your message in the input box and press "Send".
3. The AI will respond with an appropriate message.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code follows the project's coding standards and includes relevant tests.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
