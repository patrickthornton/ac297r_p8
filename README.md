# ac297r_p8
## Reposity for Project 8: Anthropometric Estimation from Smart-Phone Images
### Tianfan Xu and Patrick Thornton

This repository contains all the model definitions and optimization experiments we've tried so far. In particular, all of our relevant experiments can be found in the various Jupyter Notebooks in the `experiments/` folder; `noise/` is a small Python library that adds various kinds of loss to images, which may be of some utility.

To begin, please run the `clinical_data_process.ipynb` script to generate the required JSON input. You should ensure that the partner-provided images and spreadsheet are downloaded and placed in the correct directories before running it.

Our experiments center around four different model variants. Note that 2-view refers to models trained on only the front and side photos for each patient, while 3-view refers to models trained on all three provided photos for each patient.

1. ResNet101 vanilla 3-view; see `experiments/3_view_vanilla_runthis.ipynb`.
2. ResNet101 vanilla 2-view; see `experiments/2_view_vanilla_run_this.ipynb`.
3. ResNet101 2-view with classification loss; see `experiments/2_views_cls_loss_*.ipynb`.
4. ResNet101 2-view with reference object; see `experiments/2_views_*_with_mask.ipynb`.

The last model incorporates reference-object features using Grounding DINO and person detection with detectron2. We have three main observations on the performance of these different methods:

- 2-view performs as well as or better than 3-view; we hypothesize this is due to the unpredictability inherent in the "motion view".
- Introducing a classification loss leads to better metrics and seems to be working well. We will update the final loss design soon.
- Introducing reference objects improves metrics even farther. When running them (note these are the Jupyter Notebook files in `experiments/` with `with_mask` somewhere in their name), you may want to build mask caches first; run `experiments/cache_preparation.ipynb` to do so.

To run training, start with one of the ResNet101 vanilla files ending in `run_this.ipynb`. These files will train the model once in first two cells and save the output checkpoint. You can then add downstream tasks as needed.

The `evaluation_only_*` files do not need to be run at this point. They are for internal benchmarking and will be updated once parameters are finalized. Their structure can still serve as a reference. You can also run `different_views_comparison.ipynb` to get a better idea of how the different views (front, side, motion) contribute to total model performance using a simple vanilla ResNet101 as a baseline.

You can download the pretrained ResNet101 weight file used in our models from [https://download.pytorch.org/models/resnet101-63fe2227.pth](https://download.pytorch.org/models/resnet101-63fe2227.pth) and place it in the appropriate location on your drive.

Update: files ending with with_mask are better performing models compared to old ones.
To run files with ending with_mask, you might want to build masks caches at first. You can run cache_preparation at first.
