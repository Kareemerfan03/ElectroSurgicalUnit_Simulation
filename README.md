# Electrosurgical Unit Safety Simulation

This project is a simple desktop simulation for an **Electrosurgical Unit (ESU)**.  
The purpose of the program is to check if the device settings are safe before use, based on basic medical safety rules.

The application was created for an academic assignment about **medical device standards**.

---

## What is an ESU?
An Electrosurgical Unit is a medical device used during surgeries to:
- Cut tissue (Cut mode)
- Control bleeding (Coag mode)

Because ESUs use electrical energy, wrong settings can cause burns or tissue damage.  
This simulation helps detect unsafe conditions before activation.

---

## What the Program Does
The user enters:
- Patient age and weight
- ESU mode (Cut / Coag)
- Power level
- Activation time
- Tissue impedance
- Return pad contact condition
- REM (Return Electrode Monitoring) status

After pressing **START**, the system shows:
- **SAFE**
- **WARNING**
- **ERROR**

Warnings and errors are displayed on the screen.

---

## User Interface Steps
1. Run the program to open the main window  
2. Enter patient information  
3. Enter device settings  
4. Press **START** to evaluate safety  
5. Press **RESET** to clear inputs and test again  

---

## Standard Used
The safety logic in this project is based on:

**IEC 60601-2-2**  
(Medical electrical equipment – safety requirements for electrosurgical devices)

This standard focuses on:
- Power limits
- Patient safety
- Thermal injury prevention
- Return electrode monitoring

---

## Safety Limits Used (Examples)
- Cut mode max power: 120 W  
- Coag mode max power: 90 W  
- Pediatric patients: power reduced  
- Long activation time: warning or error  
- High impedance: warning or error  
- Poor pad contact with REM: error  

---

## Limitations
- This is only a software simulation
- No real electrical energy is used
- Not a certified medical device
- For educational use only

---

## Tools Used
- Python
- PyQt5

---

## GitHub Link
https://github.com/Kareemerfan03/ElectroSurgicalUnit_Simulation
