import os
import shutil

# pretrained_models = os.path.join(dir, 'pretrained_models')
# routers = os.path.join(dir, 'routers')

# print(pretrained_models)
# print(routers)

def test_reset():
    dir = os.path.dirname(os.path.abspath(__file__))
    dir = os.path.dirname(dir)
    dir = os.path.dirname(dir)

    pretrained_models = os.path.join(dir, 'pretrained_models')
    routers = os.path.join(dir, 'routers')


    shutil.rmtree(pretrained_models)
    shutil.rmtree(routers)