import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QTextEdit,
    QVBoxLayout, QHBoxLayout, QGroupBox, QCheckBox,
    QPushButton, QLineEdit
)
from PyQt5.QtCore import Qt, QTimer


def evaluate_esu(weight, age, mode, power, activation, pad_contact, impedance, rem):
    warnings = []
    errors = []

    pediatric = age < 8 or (age <= 12 and weight < 40)

    if mode == "Cut":
        max_power = 120
        rec_power = 80
    else:
        max_power = 90
        rec_power = 60

    if pediatric:
        max_power *= 0.7
        rec_power *= 0.7

    if power > max_power:
        errors.append("Power exceeds maximum safe limit")
    elif power > rec_power:
        warnings.append("Power above recommended level")

    if activation > 20:
        errors.append("Activation time too long (thermal injury risk)")
    elif activation > 10:
        warnings.append("Long activation time")

    if impedance > 300:
        errors.append("Very high impedance (unsafe)")
    elif impedance > 200:
        warnings.append("High impedance")

    if pad_contact == "Poor":
        if rem:
            errors.append("REM detected poor return pad contact")
        else:
            warnings.append("Poor return pad contact – burn risk")

    if errors:
        status = "ERROR"
    elif warnings:
        status = "WARNING"
    else:
        status = "SAFE"

    return status, warnings, errors



class ESUDevice(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Electrosurgical Unit – Safety Test")
        self.setGeometry(200, 80, 950, 650)
        self.setStyleSheet("background-color: #0b0f14; color: #e6e6e6;")

        self.flash_timer = QTimer()
        self.flash_timer.timeout.connect(self.flash_alert)
        self.flash_state = False

        main = QVBoxLayout()
        self.setLayout(main)

        # -------- HEADER --------
        header = QLabel("ELECTROSURGICAL UNIT – SAFETY EVALUATION")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 26px; font-weight: bold; padding: 15px;")
        main.addWidget(header)

        # -------- STATUS --------
        self.status_label = QLabel("READY")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet(
            "background-color: #444; font-size: 24px; font-weight: bold; padding: 15px;"
        )
        main.addWidget(self.status_label)

        body = QHBoxLayout()
        main.addLayout(body)

        # -------- LEFT --------
        left = QVBoxLayout()
        body.addLayout(left, 2)

        left.addWidget(self.create_patient_group())
        left.addWidget(self.create_device_group())

        # -------- BUTTONS --------
        btn_layout = QHBoxLayout()

        self.start_btn = QPushButton("START")
        self.start_btn.setStyleSheet(
            "font-size: 18px; padding: 12px; background-color: #1d3557; color: white;"
        )
        self.start_btn.clicked.connect(self.run_evaluation)

        self.reset_btn = QPushButton("RESET")
        self.reset_btn.setStyleSheet(
            "font-size: 18px; padding: 12px; background-color: #6c757d; color: white;"
        )
        self.reset_btn.clicked.connect(self.reset_system)

        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.reset_btn)
        left.addLayout(btn_layout)

        # -------- RIGHT --------
        alerts_group = QGroupBox("SYSTEM ALERTS")
        alerts_layout = QVBoxLayout()
        alerts_group.setLayout(alerts_layout)

        self.alerts = QTextEdit()
        self.alerts.setReadOnly(True)
        self.alerts.setStyleSheet(
            "background-color: #121822; font-size: 14px; padding: 10px;"
        )
        alerts_layout.addWidget(self.alerts)

        body.addWidget(alerts_group, 1)



    def create_patient_group(self):
        group = QGroupBox("PATIENT INPUTS")
        layout = QVBoxLayout()
        group.setLayout(layout)

        self.age = self.add_input(layout, "Age (years)", "30")
        self.weight = self.add_input(layout, "Weight (kg)", "70")

        return group

    def create_device_group(self):
        group = QGroupBox("DEVICE INPUTS")
        layout = QVBoxLayout()
        group.setLayout(layout)

        self.mode = self.add_dropdown(layout, "Mode", ["Cut", "Coag"])
        self.power = self.add_input(layout, "Power (W)", "50")
        self.activation = self.add_input(layout, "Activation Time (sec)", "5")
        self.impedance = self.add_input(layout, "Impedance (Ohms)", "120")
        self.pad = self.add_dropdown(layout, "Return Pad Contact", ["Good", "Marginal", "Poor"])

        self.rem = QCheckBox("REM Enabled")
        self.rem.setChecked(True)
        layout.addWidget(self.rem)

        return group




    def add_input(self, layout, label, default):
        lbl = QLabel(label)
        layout.addWidget(lbl)

        field = QLineEdit()
        field.setText(default)
        field.setStyleSheet("padding: 6px; background-color: #ffffff; color: #000000;")
        layout.addWidget(field)

        return field

    def add_dropdown(self, layout, label, options):
        lbl = QLabel(label)
        layout.addWidget(lbl)

        combo = QComboBox()
        combo.addItems(options)
        layout.addWidget(combo)

        return combo





    def run_evaluation(self):
        self.flash_timer.stop()
        self.flash_state = False
        self.alerts.clear()

        try:
            weight = float(self.weight.text())
            age = int(self.age.text())
            power = float(self.power.text())
            activation = float(self.activation.text())
            impedance = float(self.impedance.text())
        except ValueError:
            self.status_label.setText("INPUT ERROR")
            self.status_label.setStyleSheet(
                "background-color: #e63946; font-size: 24px; font-weight: bold; padding: 15px;"
            )
            self.alerts.setText("⛔ Invalid numeric input detected")
            return

        status, warnings, errors = evaluate_esu(
            weight,
            age,
            self.mode.currentText(),
            power,
            activation,
            self.pad.currentText(),
            impedance,
            self.rem.isChecked()
        )

        for w in warnings:
            self.alerts.append(f"⚠ {w}")
        for e in errors:
            self.alerts.append(f"⛔ {e}")

        if status == "SAFE":
            self.status_label.setText("SAFE")
            self.status_label.setStyleSheet(
                "background-color: #1faa59; font-size: 26px; font-weight: bold; padding: 15px;"
            )
        elif status == "WARNING":
            self.status_label.setText("WARNING")
            self.start_flashing("#f4a261", "#0b0f14")
        else:
            self.status_label.setText("ERROR")
            self.start_flashing("#e63946", "#0b0f14")





    def reset_system(self):
        self.flash_timer.stop()
        self.flash_state = False

        self.age.setText("30")
        self.weight.setText("70")
        self.power.setText("50")
        self.activation.setText("5")
        self.impedance.setText("120")
        self.mode.setCurrentIndex(0)
        self.pad.setCurrentIndex(0)
        self.rem.setChecked(True)

        self.status_label.setText("READY")
        self.status_label.setStyleSheet(
            "background-color: #444; font-size: 24px; font-weight: bold; padding: 15px;"
        )
        self.alerts.clear()




    def start_flashing(self, color1, color2):
        self.flash_colors = (color1, color2)
        self.flash_timer.start(500)

    def flash_alert(self):
        self.flash_state = not self.flash_state
        color = self.flash_colors[self.flash_state]
        self.status_label.setStyleSheet(
            f"background-color: {color}; font-size: 26px; font-weight: bold; padding: 15px;"
        )




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ESUDevice()
    window.show()
    sys.exit(app.exec_())
