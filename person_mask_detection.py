
import time
import numpy as np
import cv2
from openvino.inference_engine import IENetwork
from openvino.inference_engine import IECore
import argparse

def main(args):
    '''
    Main function
    '''
    raise NotImplementedError
    
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--model_path', required=True)
    parser.add_argument('--device', default=None)
    parser.add_argument('--path', default=None)
    parser.add_argument('--batches', default=None)
    
    args=parser.parse_args() 
    main(args)
    
