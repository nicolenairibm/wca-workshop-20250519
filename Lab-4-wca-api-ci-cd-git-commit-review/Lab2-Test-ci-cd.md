# Lab 2: Tirggering CI/CD review

This document gives step-by-step guide to finish Lab 2, which will involve creating a git commit and git push, which will automatically trigger the git webhook to review the contents of the push.

## Lab 2 content:

### 1. Start the smee client (in one terminal):
   ```bash
   smee -u <your-smee-url> -t http://localhost:8000/webhook/github
   ```

### 2. Start the webhook server (in another terminal):
   ```bash
   python main.py
   ```

The server will:
- Run on http://localhost:8000
- Auto-reload when you make code changes
- Receive webhooks through smee.io
- Display commit information in real-time
- Show code diffs with syntax highlighting
- Create detailed code review issues

### 3. To test it, create a git commit and push it to the repository for which you configured the git webhooks. The output should look like this:

![alt text](../images/ci-cd-1.png)
![alt text](../images/ci-cd-2.png)
