# Electrosurgical Unit (ESU) Safety Simulation

## 📌 Project Overview
This project is a **desktop simulation of an Electrosurgical Unit (ESU)** designed to evaluate **patient safety and device operation parameters** before activation.  
The simulation is implemented using **Python and PyQt5** and follows internationally recognized **medical device safety standards**.

The system analyzes patient data and device settings, then provides:
- **SAFE**
- **WARNING**
- **ERROR**

status outputs based on predefined safety limits.

---

## 🏥 Medical Device Explanation
An **Electrosurgical Unit (ESU)** is a medical device used in surgical procedures to cut tissue or control bleeding using high-frequency electrical energy.

### Key Risks Addressed:
- Excessive power delivery
- Long activation time (thermal injury)
- Poor return electrode (pad) contact
- High tissue impedance
- Pediatric patient sensitivity

This simulation focuses on **risk detection and mitigation**, not treatment.

---

## ⚙️ Features
- Manual input of patient and device parameters
- Pediatric vs adult safety adjustment
- Real-time safety evaluation
- Visual alerts (flashing WARNING / ERROR)
- Reset function for repeated testing
- Return Electrode Monitoring (REM) logic

---

## 🖥️ User Interface (UI) Steps

> 📸 **Note:** Insert screenshots of each step when submitting the report.

### Step 1: Launch the Application
Run the Python file to open the ESU Safety Evaluation interface.

---

### Step 2: Enter Patient Information
- **Age (years)**
- **Weight (kg)**

These values determine whether pediatric safety limits apply.

---

### Step 3: Enter Device Parameters
- **Mode**: Cut / Coag
- **Power (W)**
- **Activation Time (sec)**
- **Impedance (Ohms)**
- **Return Pad Contact**: Good / Marginal / Poor
- **REM Enabled** (checkbox)

---

### Step 4: Press START
The system evaluates all parameters and displays:
- **SAFE** (green)
- **WARNING** (orange flashing)
- **ERROR** (red flashing)

Detailed alerts appear in the **System Alerts** panel.

---

### Step 5: Press RESET
Resets all fields and clears alerts for a new evaluation cycle.

---

## 🚨 Evaluation Logic Summary
The system checks:
- Power vs recommended and maximum limits
- Activation time duration
- Tissue impedance
- Return electrode contact quality
- REM status
- Pediatric safety reduction factors

---

## 📐 Medical Standard Used

### **IEC 60601-2-2**
**Medical electrical equipment – Part 2-2:  
Particular requirements for the basic safety and essential performance of high-frequency surgical equipment**

---

## 🔒 Applied Safety Limits (Examples)

| Parameter | Adult Limit | Pediatric Adjustment |
|--------|-------------|---------------------|
| Cut Power | ≤ 120 W | Reduced by 30% |
| Coag Power | ≤ 90 W | Reduced by 30% |
| Activation Time | ≤ 20 sec | Same |
| Impedance | ≤ 300 Ω | Same |
| Poor Pad Contact | WARNING / ERROR | ERROR if REM active |

---

## ⚠️ Standard Limitations
- This is a **software simulation**, not a certified medical device
- Does **not replace clinical judgment**
- No real electrical output or tissue interaction
- Intended for **educational and academic use only**

---

## 🧑‍💻 Technologies Used
- Python 3
- PyQt5
- Object-oriented design
- Event-driven GUI logic

---

## 🔗 GitHub Repository
👉 **GitHub Link:**  
https://github.com/Kareemerfan03/ElectroSurgicalUnit_Simulation

---

## 📄 Disclaimer
This project is developed **for academic purposes only** and is **not intended for clinical or commercial use**.
