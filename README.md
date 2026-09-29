# AI SSH Honeypot Threat Profiler

## 📌 Project Overview

This project combines the **Cowrie SSH honeypot** with a custom **AI-based threat profiling system** to monitor, analyze, and classify suspicious SSH activity.

The honeypot creates a controlled environment that captures attacker interactions such as login attempts, commands, and session activity. The AI Threat Profiler analyzes the collected activity and generates a risk assessment for each observed source.

## 🎯 Objectives

- Detect and monitor suspicious SSH activity.
- Capture attacker commands and session behavior.
- Analyze attacker activity using automated threat profiling.
- Calculate a risk score based on observed behavior.
- Classify activity into different threat levels.
- Generate an easy-to-understand threat report.

## 🏗️ System Architecture

```text
Attacker
   │
   │ SSH Connection
   ▼
┌─────────────────────┐
│   Cowrie Honeypot   │
│                     │
│  SSH Interaction    │
│  Command Capture    │
│  Session Logging    │
└──────────┬──────────┘
           │
           │ Cowrie Logs
           ▼
┌─────────────────────┐
│  AI Threat Profiler │
│                     │
│  Log Analysis       │
│  Behavior Analysis  │
│  Risk Scoring       │
│  Threat Level       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Threat Report     │
│                     │
│  IP Address         │
│  Sessions           │
│  Commands           │
│  Risk Score         │
│  Threat Level       │
│  Response           │
└─────────────────────┘

## 🛠️ Technologies Used

- Python
- Cowrie SSH Honeypot
- Ubuntu Linux
- SSH
- VirtualBox
- Git & GitHub
- Log Analysis
- Threat Profiling

## ⚙️ How It Works

1. Cowrie starts the SSH honeypot.
2. An SSH client connects to the honeypot.
3. Cowrie captures the SSH session and commands.
4. The activity is stored in Cowrie logs.
5. `ai_profiler.py` analyzes the collected activity.
6. The profiler calculates a risk score.
7. The activity is classified into a threat level.
8. A threat report is generated.

## 🧪 Testing

The honeypot was tested using SSH connections and commands such as:

```bash
ls
whoami
pwd
The commands were successfully captured in the Cowrie logs and processed by the AI Threat Profiler.

## 📊 Example Threat Report

```text
AI THREAT REPORT

IP Address : 10.0.2.2
Sessions   : 1
Commands   : ls, whoami, pwd

Risk Score : Calculated by the profiler
Threat     : Classified by the profiler
Response   : Generated recommendation

## ⚠️ Disclaimer

This project is intended for educational, cybersecurity research, and controlled laboratory environments.

Only deploy the honeypot on systems and networks where you have authorization to monitor activity.

## 🔮 Future Enhancements

- Real-time threat detection
- Machine-learning-based threat classification
- Security dashboard
- Automated security alerts
- Attack pattern visualization
- SIEM integration
