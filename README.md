# app-services
app service demo python code



# Database Credentials 
## create .env file and keep your credentials
'''
| Name          | Value                                           |
|---------------|-------------------------------------------------|
| `DB_HOST`     | `azure2501db.postgres.database.azure.com`      |
| `DB_NAME`     | `demo_app`                                      |
| `DB_USER`     | `adminuser`                                     |
| `DB_PASSWORD` | `Crmedify@12345`                                |
'''
# Deploy Using Azure Portal GUI
✅ Step-by-Step in Azure Portal:
- Login to Azure Portal
- Click Create a resource > Search for App Service > Click Create
- Fill the form:
    Resource Group: flask-rg (or create new)
    App name: e.g., flaskpgdemo123
    Publish: Code
    Runtime stack: Python 3.10
    OS: Linux
    Region: Choose nearby

- Click Next or directly click Review + Create, then Create

# Add PostgreSQL Environment Variables
- In your App Service → Left menu → Configuration
- Under Application settings, click + New application setting and add:

# Upload the Flask ZIP App:
- After creation, go to your App Service
- In the left menu, click Deployment Center
Choose:
  Source: Local Git or ZIP
  Build provider: App Service build service
  Upload your flask-app.zip file
  Click Save

# Access Your Web App
- In Overview tab of your App Service
- Click on the URL (e.g., https://flaskpgdemo123.azurewebsites.net)
- You should see the form and be able to insert data into PostgreSQL!
