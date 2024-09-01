import torch.nn as nn
from transformers import PretrainedConfig, PreTrainedModel


# COPY from model_training.ipynb
class DigitClassifier(nn.Module):
    def __init__(self, image_size=28, num_classes=10, **kwargs):
        super().__init__(**kwargs)
        fl_size_s = ((image_size - 4) / 2 - 2) / 2
        fl_size = int(fl_size_s * fl_size_s * 5)
        self.fl = nn.Sequential(
            nn.Conv2d(1, 16, 5),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 5, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Flatten(1),
            nn.Linear(fl_size, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
        )
        self.out = nn.Sequential(
            nn.Linear(128, 64), nn.ReLU(), nn.Linear(64, num_classes)
        )

    def forward(self, x):
        x = self.fl(x)
        x = self.out(x)
        return x


class DigitConfig(PretrainedConfig):
    model_type = "Classifier"

    def __init__(self, image_size=28, num_classes=10, **kwargs):
        self.image_size = image_size
        self.num_classes = num_classes
        super().__init__(**kwargs)


class DigitClassifierModel(PreTrainedModel):
    config_class = DigitConfig

    def __init__(self, config):
        super().__init__(config)
        self.model = DigitClassifier(config.image_size, config.num_classes)

    def forward(self, tensor):
        return self.model.forward(tensor)
