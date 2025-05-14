# Lab1: Envrionment Setup

This document gives step-by-step guide to finish Lab 1.

## Lab1 covers:

- Configure Smee
- Configure github webhooks
- Setting all environment variables

### 1. Code Asset Download
- Git clone the workshop repository which has all the necessary files required to run the labs

### 2. Install required python library and Configure Smee 
- go into the ci-cd-wca folder
   ```bash
   cd wca-ci-cd
   pip install -r requirements.txt
   npm install --global smee-client
   ```
- Visit https://smee.io/new
   - Copy the URL provided


### 3. Configure github webhook (for your personal repository for which you need to monitor push request)
   - Go to your repository's Settings > Webhooks (this is the repository for which you want to run automatic ci/cd evaluations)
   - Click "Add webhook"
   - Set Payload URL to your smee.io URL
   - Content type: application/json
   - Set Secrets: add any value of your choice
   - Select events: Choose "Just the push event"


### 4. Set environment variables
- Create a `.env` file in the project root (wca-ci-cd folder):
   ```bash
   # Required: Your smee.io URL for webhook forwarding
   export SMEE_URL='https://smee.io/your-unique-url'
   
   # Required: GitHub personal access token for API access
   export GITHUB_TOKEN='your-github-token'
   
   # Required: Watson Code Assistant API key
   export IAM_APIKEY='your-wca-api-key'
   
   # Optional: Webhook secret for added security
   export GITHUB_WEBHOOK_SECRET='your-webhook-secret'
   ```