# **AI-Powered Deepfake Detection in Biometric Systems**

## Description
This project focuses on detecting deepfake videos using deep learning techniques, particularly in biometric systems where facial recognition is critical for security. We implemented a solution using the XceptionNet architecture to identify manipulated facial data from real and fake video datasets.

---

## 🧠 Features

### 📁 Datasets Used
- **Celeb-DF-v2**: 42,000+ real and fake facial images.
- **FaceForensics++**: 57,000+ real and fake facial images.
- **Hybrid Dataset**: Combined version for better generalization (99,000+ images).

<p align="center">
  <img src="figure/performanceexample.jpg" width="500"/>
  <br>
  <i>Example training batch combining Celeb-DF-v2 and FaceForensics++</i>
</p>

---

### 🔧 Preprocessing
- Face detection and alignment using **Dlib** (68 landmark points).
- Images resized to **128×128 pixels** and converted to tensors.
- Visual difference maps calculated between raw and normalized images.

<p align="center">
  <img src="figure/dlib.jpg" width="500"/>
  <br>
  <i>Dlib facial landmark detection example</i>
</p>

<p align="center">
  <img src="figure/preprocessed_data.png" width="400"/>
  <img src="figure/preprocessed_data3.png" width="400"/>
  <br>
  <i>Preprocessing: subject face examples with difference maps</i>
</p>

---

### 🧱 Model Architecture
- **XceptionNet** with depthwise separable convolutions.
- Optimized using **Binary Cross-Entropy Loss** and **Adam Optimizer**.

<p align="center">
  <img src="figure/moreonxception.jpg" width="700"/>
  <br>
  <i>XceptionNet architectural flow (Entry → Middle → Exit Flow)</i>
</p>

---

### 🔍 Feature Extraction

<p align="center">
  <img src="figure/featex_first10_1.jpg" width="600"/>
  <img src="figure/featex_first10_2.jpg" width="600"/>
  <br>
  <i>Feature maps from XceptionNet’s Entry Flow (Layers 1–10)</i>
</p>

<p align="center">
  <img src="figure/featex_last10.jpg" width="600"/>
  <br>
  <i>Feature maps from XceptionNet’s Exit Flow (final classification layer)</i>
</p>

---

### 🖥️ System Pipeline

<p align="center">
  <img src="figure/systemarch.png" width="500"/>
  <br>
  <i>System architecture overview for end-to-end detection</i>
</p>

---

## 📈 Performance Evaluation

### Training Curves

<p align="center">
  <img src="figure/traincurve20.png" width="600"/>
  <br>
  <i>Training and validation curves (20 epochs)</i>
</p>

<p align="center">
  <img src="figure/traincurve100.png" width="600"/>
  <br>
  <i>Training and validation curves (100 epochs)</i>
</p>

### Confusion Matrices

<p align="center">
  <img src="figure/confusion_matrix_hybrid_20epochs.png" width="300"/>
  <img src="figure/confusion_matrix_hybrid_100epochs.png" width="300"/>
  <img src="figure/unseen_confusion_matrix_hybrid_100epochs.png" width="300"/>
  <br>
  <i>Confusion matrices: 20 epochs / 100 epochs / Unseen data</i>
</p>

---

### Prediction Examples

<p align="center">
  <img src="figure/predicted_hybrid_100epochs.png" width="500"/>
  <br>
  <i>Predictions on hybrid dataset (100 epochs, seen data)</i>
</p>

<p align="center">
  <img src="figure/unseen_predicted_hybrid_100epochs.png" width="500"/>
  <br>
  <i>Predictions on hybrid dataset (unseen data)</i>
</p>

<p align="center">
  <img src="figure/performanceexampleunseen.jpg" width="500"/>
  <br>
  <i>Example batch from unseen test data</i>
</p>

---

## ✅ Achievements
- Built a high-performance deepfake detection system using state-of-the-art CNN techniques.
- Successfully evaluated model generalizability with unseen test data.
- Visualized preprocessing and internal feature extraction layers to understand the learning process.

---

## ❗ Challenges
- Ensuring generalization to unseen deepfake manipulations.
- Balancing between accuracy and computational efficiency.
- Limited dataset diversity in real-world-like scenarios.

---

## 🚀 Future Work
- Explore transformer-based and real-time detection architectures.
- Extend dataset diversity through ethical data collection.
- Integrate model into real-time biometric security pipelines.

---

## 📚 References
1. A. Rössler et al., “FaceForensics++,” ICCV, 2019.  
2. Y. Li et al., “Celeb-DF,” CVPR, 2020.  
3. Y. Mirsky and W. Lee, ACM Computing Surveys, 2021.  
4. B. Dolhansky et al., “DFDC Dataset,” 2020.  
5. M. S. Rana et al., IEEE Access, 2022.  
6. B. Zi et al., “WildDeepfake,” ACM Multimedia, 2020.  
7. A. Heidari et al., Wiley Reviews, 2023.  
8. M.-H. Maras and A. Alexandrou, The Int. J. of Evidence & Proof, 2019.  
9. S. Hussain et al., WACV, 2021.  
10. L. Floridi, Philosophy & Technology, 2018.  
