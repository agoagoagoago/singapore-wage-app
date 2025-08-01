# Deployment Guide for Singapore Wage App

This guide covers deploying the Singapore Wage Streamlit app to Render and connecting it to the domain singaporewage.com.

## Prerequisites

- GitHub repository: https://github.com/agoagoagoago/singapore-wage-app
- Render account: https://render.com
- Domain ownership: singaporewage.com

## Step 1: Create Render Web Service

1. **Sign up/Log in to Render**
   - Go to https://render.com
   - Create account or log in

2. **Connect GitHub Repository**
   - Click "New +" → "Web Service"
   - Connect your GitHub account if not already connected
   - Select the repository: `agoagoagoago/singapore-wage-app`

3. **Configure Web Service**
   - **Name**: `singapore-wage-app`
   - **Environment**: `Python`
   - **Region**: Choose closest to your users (e.g., Oregon for global)
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

4. **Environment Variables** (Add these in Advanced settings)
   - `PYTHON_VERSION`: `3.11.0`
   - `STREAMLIT_SERVER_HEADLESS`: `true`
   - `STREAMLIT_BROWSER_GATHER_USAGE_STATS`: `false`

5. **Instance Type**
   - Start with "Starter" (free tier) for testing
   - Upgrade to "Starter+" or higher for production

6. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete (5-10 minutes)

## Step 2: Configure Custom Domain

1. **Add Custom Domain in Render**
   - Go to your service dashboard
   - Click "Settings" tab
   - Scroll to "Custom Domains"
   - Click "Add Custom Domain"
   - Enter: `singaporewage.com`
   - Click "Save"

2. **Get DNS Information**
   - Render will provide DNS records to configure:
     - `A` record pointing to Render's IP
     - `CNAME` record for www subdomain

## Step 3: Configure DNS at Domain Provider

1. **Access Your Domain DNS Settings**
   - Log into your domain registrar (GoDaddy, Namecheap, etc.)
   - Navigate to DNS management for singaporewage.com

2. **Add DNS Records**
   ```
   # A Record
   Type: A
   Name: @
   Value: [Render's IP address - provided in dashboard]
   TTL: 300

   # CNAME Record (for www)
   Type: CNAME
   Name: www
   Value: singaporewage.com
   TTL: 300
   ```

3. **SSL Certificate**
   - Render automatically provides SSL certificates
   - Certificate will be issued after DNS propagation (5-30 minutes)

## Step 4: Set Up Automatic Deployments

1. **GitHub Integration**
   - Automatic deployments are enabled by default
   - Every push to `main` branch triggers a new deployment

2. **Deploy Hooks** (Optional)
   - Go to service Settings → "Deploy Hooks"
   - Generate deploy hook URL for manual deployments
   - Use webhook for external CI/CD if needed

## Step 5: Verify Deployment

1. **Test Render URL**
   - Check `https://singapore-wage-app.onrender.com` works
   - Verify all features function correctly

2. **Test Custom Domain**
   - Wait for DNS propagation (up to 48 hours, usually 5-30 minutes)
   - Check `https://singaporewage.com` loads correctly
   - Verify HTTPS certificate is active

## Monitoring and Maintenance

1. **Check Logs**
   - Use Render dashboard "Logs" tab for troubleshooting
   - Monitor for any startup errors

2. **Performance**
   - Free tier has limitations (spinning down after 15 minutes of inactivity)
   - Consider upgrading for production use

3. **Updates**
   - Push changes to GitHub `main` branch
   - Render automatically redeploys

## Troubleshooting

**Common Issues:**

1. **Build Failures**
   - Check requirements.txt has all dependencies
   - Verify Python version compatibility

2. **Port Issues**
   - Ensure start command uses `$PORT` environment variable
   - Render assigns port dynamically

3. **Domain Not Working**
   - Verify DNS records are correct
   - Wait for DNS propagation
   - Check SSL certificate status in Render dashboard

4. **App Performance**
   - Monitor memory usage in Render dashboard
   - Consider upgrading instance type if needed

## Configuration Files

The repository includes:
- `render.yaml`: Infrastructure as code configuration
- `.gitignore`: Excludes unnecessary files from deployment
- `requirements.txt`: Python dependencies