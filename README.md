# AI-Powered Deepfake Detection System


## Introduction

### Problem
Deepfake technology poses significant security threats by manipulating facial images and videos, potentially compromising biometric systems that rely on facial recognition for identity verification.

### Purpose
Develop an AI-powered system using XceptionNet to accurately detect deepfake facial data, enhancing the security of biometric applications.

### Scope
Focuses on detecting facial deepfakes in images and videos using publicly available datasets. Excludes other biometric modalities like voice.

## System Overview
The system detects deepfakes by analyzing images and videos for subtle artifacts using the following steps:

1. **Data Acquisition**: Collect real and fake facial data.
2. **Preprocessing**: Normalize and crop facial regions.
3. **Feature Extraction**: Use XceptionNet to extract distinguishing features.
4. **Classification**: Classify data as real or fake.
5. **Output**: Provide labels and confidence scores.

Supports both static images and video streams for real-time detection.

## Data Collection

### Datasets
- **Celeb-DF**: 590 original and 5,639 deepfake videos with diverse subjects.
- **FaceForensics++**: 1,000 original and manipulated videos using various methods.

### Process
Extract facial images from videos, preprocess them, and label as `real` or `fake` based on the source.

**Workflow:**
1. **Input**: Video/Image
2. **Preprocessing**: Normalize and crop faces
3. **Feature Extraction**: XceptionNet
4. **Classification**: Real or Fake
5. **Output**: Labels and confidence scores

## References
[1] Dolhansky, B., Bitton, J., Pflaum, B., Lu, J., Howes, R., Wang, M., & Canton Ferrer, C. (2020). The
DeepFake Detection Challenge (DFDC) Dataset. arXiv preprint arXiv:2006.07397.
[2] Zi, B., Chang, M., Chen, J., Ma, X., & Jiang, Y.-G. (2020). WildDeepfake: A Challenging Real-World
Dataset for Deepfake Detection. In *Proceedings of the 28th ACM International Conference on Multi-
media* (MM ’20) (pp. 2382–2390), October 12–16, Seattle, WA, USA.
[3] Mirsky, Y., & Lee, W. (2020). The Creation and Detection of Deepfakes: A Survey. arXiv preprint
arXiv:2006.12432.
[4] Malik, A., Kuribayashi, M., Abdullahi, S. M., & Khan, A. N. (2022). DeepFake Detection for Human
Face Images and Videos: A Survey. *IEEE Access*, 10, 124328-124351.
[5] Yu, P., Xia, Z., Fei, J., & Lu, Y. (2021). A Survey on Deepfake Video Detection. *Journal of Information
Security and Applications*, 58, 102790.
[6] Li, Y., Yang, X., Sun, P., Qi, H., & Lyu, S. (2020). Celeb-DF: A Large-scale Challenging Dataset for
DeepFake Forensics. arXiv preprint arXiv:1909.12962.
[7] R¨ossler, A., Cozzolino, D., Verdoliva, L., Riess, C., Thies, J., & Nießner, M. (2019). FaceForensics++:
Learning to Detect Manipulated Facial Images. arXiv preprint arXiv:1901.08971.
[8] R¨ossler, A., Cozzolino, D., Verdoliva, L., Riess, C., Thies, J., & Nießner, M. (2018). FaceForensics: A
Large-scale Video Dataset for Forgery Detection in Human Faces. arXiv preprint arXiv:1803.09179.
