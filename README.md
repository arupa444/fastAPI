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
   and
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

