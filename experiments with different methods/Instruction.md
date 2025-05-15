
This folder contains all the model definitions and optimization experiments we've tried so far.

To begin, please run the clinical_data_process script to generate the required JSON input. You should ensure that the partner-provided images and spreadsheet are downloaded and placed in the correct directories before running it.

We've experimented with five different model variants: (1) ResNet101 vanilla 3-view, (2) ResNet101 vanilla 2-view, (3) ResNet101 2-view with classification loss, (4) ResNet101 3-view with reference object, and (5) ResNet101 2-view with reference object. The last two models incorporate reference-object features using Grounding DINO and person detection with detectron2. They are still being tuned and currently do not outperform the vanilla baselines. However, we have two main observations: (1) 2-view (without motion) performs as well as or better than 3-view; (2) introducing a classification loss leads to better metrics and seems working well. We will update the final loss design soon.

To run training, start with one of the ResNet101 vanilla file ending in run_this. These file will train the model once in first two cells and save the output checkpoint. You can then add downstream tasks as needed.

The evaluation-only files do not need to be run at this point. They are for internal benchmarking and will be updated once parameters are finalized. Their structure can still serve as a reference.

You can download the pretrained ResNet101 weight file used in our models from https://download.pytorch.org/models/resnet101-63fe2227.pth and place it in the appropriate location on your Drive.




Update: files ending with with_mask are better performing models compared to old ones.
To run files with ending with_mask, you might want to build masks caches at first. You can run cache_preparation at first. 

Different views comparison works as a way to determine how different views combination affects the model performance, under vanilla resnet101.
