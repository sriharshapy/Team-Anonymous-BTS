## Intro

Read more about YOLO (in darknet) and download weight files [here](http://pjreddie.com/darknet/yolo/). 

### Clone repo
 ```
    git clone https://github.com/muffyharsha/traffic-annotation.git
 ```

### Dependencies

Python3, tensorflow 1.4, numpy, opencv 3.

Install python 3.6 preferably.

 ```
    pip install tensorflow==1.4.0
 ```
  ```
    pip install numpy
 ```
 ```
    pip install opencv-python
 ```
 ```
    pip install opencv-contrib-python
 ```

### Getting started

You can choose _one_ of the following three ways to get started. Run the following commands while in the project directory.

1. Just build the Cython extensions in place. 
    ```
    python setup.py build_ext --inplace
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



### Run the program
```
    python app.py
```

