Generative GaitNet
==================

Reference: [2022GaitNet]_

.. [2022GaitNet] J\. Park, S\. Min, P. S. Chang, J. Lee, M. S. Park, and J. Lee, “Generative GaitNet,” in Special Interest Group on Computer Graphics and Interactive Techniques Conference Proceedings, Vancouver BC Canada: ACM, Aug. 2022, pp. 1–9.

GitHub link: https://github.com/namjohn10/GenerativeGaitNet

.. note::

    I tried this code on Linux 18.04 and Python 3.6 as the authors suggested. I used Anaconda to create the virtual environement. See below notes on how to install Anaconda on Linux.


Installation (Anaconda)
-----------------------

* Install Anaconda extended dependencies:
  
  .. code-block:: bash

    apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

* Install curl (if not installed already):
  
  .. code-block:: bash

    sudo apt install curl

* Download Anaconda for Linux (check filename `here <https://repo.anaconda.com/archive/>`_):
  
  .. code-block:: bash

    curl -O https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh

* Install Anaconda for Linux:
  
  .. code-block:: bash

    bash ~/Downloads/Anaconda3-2024.02-1-Linux-x86_64.sh
  
* Do not activate conda environment on command prompt startup:
  
  .. code-block:: bash

    conda config --set auto_activate_base false

* Manually initialize conda:
  
  .. code-block:: bash

    source ~/anaconda3/bin/activate
    conda init
    source ~/.bashrc

* Reopen shell and open anaconda (in base environment):
  
  .. code-block:: bash

    anaconda-navigator

Installation (Prerequisites)
----------------------------

* Install pytorch and torchvision

  .. code-block:: bash

    conda install pytorch
    conda install torchvision
  
* Install OpenAI gym

  .. code-block:: bash

    conda install -c powerai gym

* Install pickle5

  .. code-block:: bash

    conda install conda-forge::pickle5

* Install Ray

  .. code-block:: bash

    pip install ray==1.8.0
    pip install ray[rllib]==1.8.0
  
  .. warning:: 

    The authors verified the code works on Ray 1.8.0. I tried the latest version of Ray (2.0?) but it seems incompatible with Python 3.6 due to the use of *annotations*.

* Install dm_tree

  .. code-block:: bash

    pip install dm_tree

* Install pandas

  .. code-block:: bash

    conda install pandas

* Install IPython

  .. code-block:: bash

    pip install ipython


Installation (GaitNet)
----------------------

Follow the instructions in the README.md in the repository.

* Install libraries automatically:
  
  .. code-block:: bash

    source ~/.bashrc
    cd '/path/to/downloaded/folder'
    sudo bash install.sh

  .. note:: 
    If you get an error saying cmake is not installed or the version is too low, run this command: ``sudo apt install cmake``.

* Compile:

  .. code-block:: 

    source ~/.bashrc
    cd '/path/to/downloaded/folder'
    sudo bash pc_build.sh
    cd build
    sudo make -j16
  
  .. note:: 
    Change the number after *j* to the number of cores of your CPU.

* Rendering (with no policy):
 
  .. code-block::

    source ~/.bashrc
    cd {downloaded folder}/build
    ./imgui_render/imgui_render ../data/metadata.txt

  .. note:: 

    I ran this part and it looks fine.

    .. raw:: html

      <iframe width="560" height="315" src="https://www.youtube.com/embed/YBSJo4Acv84?si=Gs4mYejnCJgB-Cd6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

* Rendering (with default 4 trained policy to the lower body):
 
  .. code-block::

    source ~/.bashrc
    cd {downloaded folder}/build
    ./imgui_render/imgui_render ../data/trained_nn/Skeleton ../data/trained_nn/Ankle ../data/trained_nn/Hip ../data/trained_nn/Merge

  .. error:: 

    I ran this part and the renderer crashed after I started the animation by pressing *Space*.

    .. raw:: html

      <iframe width="560" height="315" src="https://www.youtube.com/embed/cXz2SlOzqdg?si=NA_X6mfkWp015sdM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

* Rendering (with trained policy):
 
  .. code-block::

    source ~/.bashrc
    cd {downloaded folder}/build
    ./imgui_render/imgui_render {network_path}
  
  .. note:: 

    I haven't tried this part yet because I wasn't able to run the training. See the following part.

* Training a single policy (cluster setting):
 
  .. code-block::

    source ~/.bashrc
    cd {downloaded folder}/python
    python3 ray_train.py --config=ppo_medium_node

  .. error:: 

    I ran this part but the training didn't start. It seemed that the code is for running on cluster instead of PC. See the warning messages in the following screenshots.

    .. image:: /resources/gaitnet/training_1.png
      :align: center
    
    .. image:: /resources/gaitnet/training_2.png
      :align: center

* Training (cascading and Subsumption learning):
 
  .. code-block::

    source ~/.bashrc
    cd {downloaded folder}/python
    python3 ray_train.py --config=ppo_medium_node --cascading_nn={previous network paths}

  .. note:: 
    
    I haven't tried this part yet.


.. .. raw:: html

..   <video controls src="./_static/gaitnet/relu and max pooling.mp4" width="620"></video>

.. test