import torch
from PIL import Image
from torchvision import transforms
from torchvision.models import vgg19

from utils import GradCam

if __name__ == '__main__':
    test_image = (transforms.ToTensor()(Image.open('both.png'))).unsqueeze(dim=0)
    model = vgg19(pretrained=True)
    model.__setattr__(name='net_mode', value='CNN')
    if torch.cuda.is_available():
        test_image = test_image.cuda()
        model.cuda()
    grad_cam = GradCam(model)
    feature_image = grad_cam(test_image).squeeze(dim=0)
    feature_image = transforms.ToPILImage()(feature_image)
    feature_image.save('grad_cam.png')
