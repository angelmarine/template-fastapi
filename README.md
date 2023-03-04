# template-fastapi
FastAPI server template for quick production-level deployment on Azure App Service(Linux)

### Features
1. **Pydantic(FastAPI) schema**
   - For convenient response/request validation
   - For auto-generation of Swagger API docs

2. **Easy Function Logging**
   - Embedded a decorator function for easier production-level debugging using console (customizable)

3. **Customzed Exception Classes**
   - For detailed error handling

4. **Configuration**
   - Easy management of app configuration using config.py file.
   - Azure App Service allows setting of environment variables using Azure App Service dashboards.
   - Note that prefix "APPSETTING" is added by Azure by default.

### How to use
1. Install virtual environment
```commandline
python -m venv venv
```

2. Activate virtual environment
```commandline
# Windows
.\venv\Script\activate

# Mac or Linux
source /venv/bin/activate
```

3. Install requirements
- For Windows, package 'uvloop' might cause error. 
- You can temporarilty remove it from requirement.txt first and test locally.
```commandline
pip install -r requirements.txt
```


4. Start server
- You can also run/debug on app.py using IDE 
```commandline
python app.py
```

