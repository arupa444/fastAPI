# 🏥 Patient Management System API

A simple and powerful Patient Management System built with **FastAPI** and **Pydantic** to demonstrate modern API design with input validation, computed fields, and JSON-based persistence.

---


## 🚀 Features

- ✅ Create new patient records
- 📝 Update existing patient data
- ❌ Delete a patient by ID
- 🔍 View all patients or fetch a specific patient by ID
- 📊 Sort patients by `height`, `weight`, or `bmi`
- 📦 Data persistence using a local `patients.json` file
- 🧠 Includes computed fields like BMI and health verdict (`Underweight`, `Normal`, `Obese`)

---

## 🧰 Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Validation**: [Pydantic](https://docs.pydantic.dev/)
- **Data**: JSON file (`patients.json`)
- **Run Environment**: Python 3.9+

---

## 📦 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/arupa444/fastAPI.git
   cd fastAPI
   ```
2. **Create virtual environment**
   ```bash
   python -m venv myFASTenv
   source myFASTenv/bin/activate  # On Windows use `myFASTenv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the app**
   ```bash
   uvicorn main:app --reload
   ```
5. **Access the app**
   ```bash
   Swagger UI: your_local_host/docs # for ex mine its http://127.0.0.1:8000/docs
   ReDoc: your_local_host/redoc # for ex mine its http://127.0.0.1:8000/redoc
   ```

## 🧪 API Endpoints

### 🌐 General

| Method | Endpoint       | Description                                 |
|--------|----------------|---------------------------------------------|
| GET    | `/`            | Welcome route                               |
| GET    | `/about`       | About the Patient Management API            |

---

### 👁️ View Data

| Method | Endpoint           | Description                                   |
|--------|--------------------|-----------------------------------------------|
| GET    | `/view`            | View all patient records                      |
| GET    | `/patient/{p_id}`  | Get a specific patient by ID                  |
| GET    | `/sort`            | Sort patients by `height`, `weight`, or `bmi`<br>**Query Params:** `sortBy` and `order` |

**Example for sort endpoint:**
GET /sort?sortBy=bmi&order=asc


---

### ➕ Add Patient

| Method | Endpoint    | Description                 |
|--------|-------------|-----------------------------|
| POST   | `/create`   | Add a new patient to system |

**Request Body Example:**
```json
{
  "id": "P003",
  "name": "Alice",
  "city": "Delhi",
  "age": 24,
  "gender": "Female",
  "height": 1.68,
  "weight": 65,
  "feeling": "Good",
  "disease": {
    "name": "Asthma",
    "description": "Chronic breathing issue"
  }
}
### 🔁 Update Patient

| Method | Endpoint           | Description                        |
|--------|--------------------|------------------------------------|
| PUT    | `/update/{p_id}`   | Update an existing patient by ID   |

**Path Parameter:**

- `p_id` (string): ID of the patient you want to update.

**Request Body (Partial Update Allowed):**
```json
{
  "city": "Bhubaneswar",
  "feeling": "Better",
  "weight": 68.5
}
```

**Success Response:**
```json
{
  "Message": "The data is updated"
}
```
### ❌ Delete Patient

| Method | Endpoint           | Description            |
|--------|--------------------|------------------------|
| DELETE | `/delete/{p_id}`   | Delete patient by ID   |

**Path Parameter:**

- `p_id` (string): The unique ID of the patient you want to delete.

**Example Request:**
DELETE /delete/P002


**Success Response:**
```json
{
  "message": "Perfectly deleted the P002"
}
```
