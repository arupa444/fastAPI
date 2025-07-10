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
```
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
## 📊 Patient Model

Each patient entry includes the following fields:

```json
{
  "id": "P001",
  "name": "John Doe",
  "city": "New York",
  "age": 35,
  "gender": "Male",
  "height": 1.75,
  "weight": 70,
  "feeling": "Good",
  "disease": {
    "name": "Diabetes",
    "description": "Type 2 diabetes"
  },
  "bmi": 22.86,
  "verdict": "Normal"
}
```
## 📁 Project Structure
FASTAPI-PMS/

├── main.py # Main FastAPI application with all routes

├── patients.json # JSON file storing patient data

├── withPydantic.py # Pydantic models (modular version - optional)

├── withoutPydantic.py # Version of the app without Pydantic (optional)

├── serialization.py # Optional file for custom serializers (if used)

├── requirements.txt # Python dependencies

├── README.md # Project documentation (this file)


> You can remove or restructure optional files like `withPydantic.py` and `serialization.py` if not used in your deployment.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- ⭐ Star the repository
- 🍴 Fork it
- 🐛 Report issues
- 🔧 Submit pull requests

Let’s improve this API together!

---

## 🧑 Author

**Arupa Nanda Swain**

Building clean, efficient, and developer-friendly tools.

- GitHub: [@arupa444](https://github.com/arupa444)
- LinkedIn: [linkedin.com/in/arupa-nanda-swain](https://www.linkedin.com/in/arupa-nanda-swain)

---

## 📜 License

You are free to use, modify, and distribute this software with proper attribution.

