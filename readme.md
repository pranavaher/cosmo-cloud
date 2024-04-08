# FASTAPI
### Library Management System _(CRUD Application)_

###### This is a FastAPI-based API for a Library Management System, utilizing MongoDB as the database backend. The API provides endpoints for managing students and their information.

## Installation

**Clone the repository:**

```bash
git clone https://github.com/pranavaher/cosmo-cloud
cd cosmo-cloud
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Set up environment variables:**
Create a .env file in the root directory and add the following:

```bash
MONGODB_URL=MONGODB_CONNECTION_URL
DB_NAME=MONGODB_DB_NAME
COLLECTION_NAME=COLLECTION_NAME
```

**Run the application:**

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000
