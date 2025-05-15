This work is based on the repository: 2DImage2BMI  https://github.com/FVL2020/2DImage2BMI/tree/5649a9fc47badb2038c712c9550c6b69cdd7eda6.

The Human_feature_extraction module is used to extract human features and generate the corresponding dataset.

resnet101 serves as the current baseline model.
concatresnet101_32f is the current method. It concatenates the extracted human features, trains a ResNet-101 model to obtain deep features, and uses a Gaussian process for prediction.
Pretrained Models
The pretrained models used in this work can be downloaded from the following links and put them into singleimg models:

pose2seg_release.pkl: https://drive.google.com/file/d/1BsIbUWktXxIe75fM_JWphvYB0yjV-RZy/view
exp-schp-201908270938-pascal-person-part.pth: https://drive.google.com/file/d/1E5YwNKW2VOEayK9mWCS3Kpsxf-3z04ZE/view

Note: There is no need to modify any files inside the singleimg models folder.
