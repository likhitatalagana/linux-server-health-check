
# Python-Based Linux Server Health Check Automation

## Project Overview

This project automates remote Linux server health monitoring using Python and SSH.

The Python script runs on a Monitoring Server and connects to a remote Host Server to collect system health information and generate a report.

## Tech Stack

- Python 3.12
- Red Hat Enterprise Linux (RHEL)
- Linux
- Paramiko
- SSH
- Git and GitHub

## Architecture

Monitoring Server (Server 1)
        |
        | SSH Connection
        |
Host Server (Server 2)
        |
        | Remote Command Execution
        |
CPU, Memory and Disk Monitoring
        |
        |
Automated Health Report

## Features

- Remote SSH connectivity
- CPU utilization monitoring
- Memory utilization monitoring
- Disk space monitoring
- Filesystem capacity monitoring
- Hostname and operating system information
- System uptime monitoring
- Automated text report generation
- Timestamp-based report filenames

## Project Structure

```text
remote-server-monitor/
|
|-- system_health_check.py
|-- ssh_test.py
|-- reports/
|-- README.md
|-- .gitignore
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd remote-server-monitor
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install paramiko
```

## Configuration

Configure the following details in the Python script:

- Host server IP address
- SSH username
- SSH private key path

Ensure SSH key-based authentication is configured between both servers.

Never upload private SSH keys or credentials to GitHub.

## Execution

Run the Python script:

```bash
python system_health_check.py
```

## Output

The script collects remote Linux server health information and generates a timestamped text report inside the reports directory.

## Learning Outcomes

- Python scripting and automation
- Linux system administration
- SSH remote connectivity
- Paramiko library
- Server health monitoring
- Automated report generation

