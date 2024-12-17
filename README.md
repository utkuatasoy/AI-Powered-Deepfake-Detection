## **AI-Powered Deepfake Detection in Biometric Systems**

### Description:
This project focuses on detecting deepfake videos using deep learning techniques, particularly in biometric systems where facial recognition is critical for security. We implemented a solution using the XceptionNet architecture to identify manipulated facial data from real and fake video datasets.

### Features:
- **Deepfake Detection**: Trained a model to classify videos as real or fake.
- **Datasets Used**:
  - **Celeb-DF-v2**: 42.000+ real and fake facial images.
  - **FaceForensics++**:  57.000+ real and fake facial images.
  - **Hybrid Dataset**: Combination of both datasets for enhanced model robustness including 99.000+ images.
- **Preprocessing**: 
  - Used Dlib for face detection and alignment.
  - Resized images to 128x128 pixels for consistent input.
  - Applied tensor formatting and generated visual difference maps.
- **Model Architecture**:
  - XceptionNet with depthwise separable convolutions for efficient feature extraction.
  - Binary cross-entropy loss and Adam optimizer for classification and training.
- **Performance Evaluation**:
  - Models were trained on both seen and unseen data to simulate real-world scenarios.
  - Achieved high accuracy across different test sets, including unseen data.
  
### Achievements:
- Implemented a robust deepfake detection system using state-of-the-art CNN techniques.
- Successfully demonstrated high model accuracy and the effectiveness of preprocessing techniques.
- Evaluated the model using real-world unseen data to assess its generalizability.

### Challenges:
- Handling unseen data and ensuring real-world applicability.
- Balancing performance with computational efficiency.
- Overcoming dataset diversity limitations.

### Future Work:
- Exploring alternative deep learning architectures to improve performance.
- Investigating real-time deepfake detection for live video streams.
- Expanding datasets to include more diverse and ethically sourced data.

### References:
[1] A. Rössler, D. Cozzolino, L. Verdoliva, C. Riess, J. Thies, and M. Nießner, “FaceForensics++: Learning to Detect Manipulated Facial Images,” 2019
[2] Y. Li, X. Yang, P. Sun, H. Qi, and S. Lyu, “Celeb-DF: A Large-scale Challenging Dataset for DeepFake Forensics,” 2020.
[3] Y. Mirsky and W. Lee, “The Creation and Detection of Deepfakes: A Survey,” ACM Computing Surveys, vol. 54, no. 1, pp. 1–41, Jan. 2021.
[4] B. Dolhansky et al., “The DeepFake Detection Challenge (DFDC) Dataset.” 2020.
[5] M. S. Rana, M. N. Nobi, B. Murali, and A. H. Sung, “Deepfake Detection: A Systematic Literature Review,” IEEE Access, vol. 10, pp. 25494–25513, 2022.
[6] B. Zi, M. Chang, J. Chen, X. Ma, and Y.-G. Jiang, “WildDeepfake,” Proceedings of the 28th ACM International Conference on Multimedia, Oct. 2020.
[7] A. Heidari, Nima Jafari Navimipour, H. Dag, and M. Unal, “Deepfake detection using deep learning methods: A systematic and comprehensive review,” Wiley interdisciplinary reviews. Data mining and knowledge discovery/Wiley interdisciplinary reviews. Data mining and knowledge discovery, vol. 14, no. 2, Nov. 2023.
[8] M.-H. Maras and A. Alexandrou, “Determining authenticity of video evidence in the age of artificial intelligence and in the wake of Deepfake videos,” The International Journal of Evidence & Proof, vol. 23, no. 3, pp. 255–262, Oct. 2019.
[9] S. Hussain, P. Neekhara, M. Jere, F. Koushanfar, and J. Mcauley, “Adversarial Deepfakes: Evaluating Vulnerability of Deepfake Detectors to Adversarial Examples.” Accessed: Mar. 29, 2024.
[10] L. Floridi, “Artificial Intelligence, Deepfakes and a Future of Ectypes,” Philosophy & Technology, vol. 31, no. 3, pp. 317–321, Aug. 2018.

  
