## Intro


Read more about YOLO (in darknet) and download weight files [here](http://pjreddie.com/darknet/yolo/). 

## Dependencies

Python3, tensorflow 1.0, numpy, opencv 3.

### Getting started

You can choose _one_ of the following three ways to get started.

1. Just build the Cython extensions in place. 
    ```
    python3 setup.py build_ext --inplace
    ```

2. Let pip install darkflow globally in dev mode (still globally accessible, but changes to the code immediately take effect)
    ```
    pip install -e .
    ```

3. Install with pip globally
    ```
    pip install .
    ```


After completing the above process. Download the `yolo.weights` file from [here](https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU). Place the weights file in bin folder of the project directory. 

