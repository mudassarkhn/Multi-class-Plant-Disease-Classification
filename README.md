# 🍃 LeafLens - Plant Disease Classification 🌿
![](Web App screenshots\Screenshot (4).png)
![](Web App screenshots\Screenshot (5).png)
![](Web App screenshots\Screenshot (6).png)

## Introduction
Welcome to **LeafLens**, a powerful and user-friendly application for identifying plant diseases from leaf images using a Convolutional Neural Network (CNN) model. This project combines a Flask backend API with a sleek frontend interface to provide accurate disease predictions and detailed descriptions.

---

## 🚀 Features

- 🖼️ Upload leaf images in JPG, JPEG, or PNG formats.
- 🤖 CNN model predicts the plant disease class.
- 📚 Detailed disease descriptions fetched dynamically.
- 🌐 Interactive and responsive web interface.
- 🔄 Cross-Origin Resource Sharing (CORS) enabled for flexible frontend-backend communication.

---

## 🗂️ Project Structure

- `application.py` - Flask backend serving the CNN model and API endpoints.
- `detection_model.h5` - Pre-trained CNN model for disease classification.
- `class_indices.json` - Mapping of model output indices to disease names.
- `Disease_description.json` - Detailed descriptions of each disease class.
- `index.html` - Frontend UI for image upload, prediction, and description display.
- `Testing images/` - Sample images for testing the model.
- `Training Notebook/` - Jupyter notebook for training and experimentation.

---

## ⚙️ Setup and Installation

1. **Clone the repository**  
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask backend**  
   ```bash
   python application.py
   ```

5. **Open the frontend**  
   Open `index.html` in your preferred web browser.

---

## 🖥️ Usage

1. On the frontend page, click **Upload an image** and select a leaf image (JPG, JPEG, PNG).
2. Click the **Prediction** button to send the image to the backend for classification.
3. View the predicted disease name displayed on the page.
4. Click **Get Description** to fetch detailed information about the predicted disease.

---

## 🧠 How It Works

- The backend loads a pre-trained CNN model (`detection_model.h5`) to classify images into multiple plant disease categories.
- The model outputs a class index, which is mapped to a disease name using `class_indices.json`.
- Detailed disease descriptions are stored in `Disease_description.json` and served via the `/description` API endpoint.
- The frontend interacts with the backend through REST API calls to provide a seamless user experience.

---

## 📁 Additional Resources

- **Testing images:** Located in the `Testing images/` folder for quick testing.
- **Training Notebook:** Jupyter notebook available in `Training Notebook/` for model training and experimentation.

---

## 🛠️ Technologies Used

- Python 3.x
- Flask
- TensorFlow / Keras
- NumPy
- Pillow (PIL)
- HTML, CSS, JavaScript
- Flask-CORS

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

---

---

## 🎉 Acknowledgments

Thanks to all contributors and the open-source community for making this project possible!

---

Enjoy using LeafLens to keep your plants healthy and thriving! 🌱🍀
