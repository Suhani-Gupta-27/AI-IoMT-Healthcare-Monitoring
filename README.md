# AI-Assisted IoMT Healthcare Monitoring System

##  Overview
This project presents an AI-assisted Internet of Medical Things (IoMT)-based healthcare monitoring system designed to enhance safety during photothermal cancer therapy. The system enables real-time monitoring of key physiological parameters such as temperature, pulse rate, and light intensity, ensuring better control and early detection of abnormal conditions.

The solution integrates IoT hardware, machine learning, and data visualization to create an intelligent and scalable healthcare monitoring platform.

---

##  Key Features
- Real-time sensor data acquisition using ESP32  
- Continuous monitoring of temperature, pulse, and light intensity  
- Machine learning-based anomaly detection  
- Interactive dashboard using Streamlit  
- AI-based clinical summary generation  
- End-to-end IoMT data pipeline  

---

##  System Architecture
Sensors (Temperature, Pulse, LDR) → ESP32 → Serial Communication → Python Backend → Machine Learning Model → Streamlit Dashboard → Alerts & Summaries

---

##  Technologies Used
- **Hardware:** ESP32, Temperature Sensor, Pulse Sensor, LDR  
- **Programming:** Python, Embedded C (Arduino)  
- **Libraries & Tools:**  
  - Pandas, NumPy  
  - Scikit-learn  
  - Streamlit  
- **Concepts:** IoMT, Machine Learning, Data Analysis, Real-Time Monitoring  

---

##  Machine Learning Model
- Multi-output Linear Regression  
- Trained on synthetic physiological dataset  
- Used for real-time anomaly detection  

---

##  Project Structure

├── generate_data.py # Generates synthetic dataset
├── train_model.py # Trains ML model
├── iomt_ai_model.pkl # Saved trained model
├── esp32_ai_live.py # Real-time data processing
├── dashboard.py # Streamlit dashboard
├── gemini_assistant.py # AI-based summary generation
├── training_data.csv # Dataset


---

##  How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

2. Install dependencies
pip install -r requirements.txt

3. Run model training (optional)
python train_model.py

4. Start real-time data processing
python esp32_ai_live.py

5. Launch dashboard
streamlit run dashboard.py

## Output
Real-time sensor data visualization
AI-based anomaly detection alerts
Automated clinical summaries

## Applications
Smart healthcare monitoring
Remote patient tracking
IoMT-based clinical systems
Research in AI-driven medical solutions

## Future Scope
Integration with cloud platforms
Addition of advanced sensors (SpO₂, ECG, BP)
Deployment with real-time hospital systems
Use of advanced machine learning models
