Potential Based Rewards for Learning Humanoid Locomotion
========================================================

Reference: [2023PBRS]_

.. [2023PBRS] Jeon, S. H., Heim, S., Khazoom, C., & Kim, S. (2023, May). Benchmarking potential based rewards for learning humanoid locomotion. In 2023 IEEE International Conference on Robotics and Automation (ICRA) (pp. 9204-9210).

Paper: https://ieeexplore.ieee.org/abstract/document/10160885/

GitHub link: https://github.com/se-hwan/pbrs-humanoid

.. note::

    * Procedure tested on Apr. 1st, 2024 by Ivan Lopez-Sanchez.
    * I tested this code on Ubuntu 18.04 with Python 3.6.9 (authors recommend Python 3.8).
    * I used Python's venv to create the virtual environment.
    * I used Isaac Gym Preview 4. (Authors recommend Preview 3).

Installation
------------

* Create the virtual environment using Python 3.6.9 (``user`` is your machine username)
  
  .. code-block:: bash

    virtualenv /home/user/MITlegged --python=python3

* Activate the virtual environment

  .. code-block:: bash
      
    source /home/user/MITlegged/bin/activate

  .. note::

      You should see the name of the active virtual environment in parenthesis at the begining of the line.
      Something like this ``(MITlegged)user@PCname:~$``.
    

* Install required libraries (pythorch 1.10 and cuda 11.3)

  .. code-block:: bash
      
    pip install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio==0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

* Install Isaac Gym

  1. Download Isaac Gym Preview 4 from https://developer.nvidia.com/isaac-gym
  2. Extract the zip package in the MITlegged virtual environment folder.
  3. ``cd isaacgym_lib/python && pip install -e .`` to install the requirements.
  4. Test the installation by running an example: ``cd isaacgym/python/examples && python 1080_balls_of_solitude.py``.
  
  .. Note:: You sould be able to see a new window apperaing with a group of balls falling

    .. image:: /resources/PBRS_MIT_Humanoid/balls_of_solitude.png
      :align: center
      :width: 700
    

* Clone the pbrs-humanoid repository and initialize the submodules
  
  1. ``git clone https://github.com/se-hwan/pbrs-humanoid.git``
  2. ``cd pbrs-humanoid/gpugym && git submodule init && git submodule update``

  .. Note::
    
    In case you dont have installed git: ``sudo apt-get install git``. Then, clone the repository.
  
* Install gpu_rl (Proximal Policy Optimization - PPO implementation)

  ``cd pbrs-humanoid/gpu_rl && pip install -e .``

* Install gpuGym

  ``cd .. && pip install -e .``

* Install WandB (for traking on the learned policy during the training stage)

  ``pip install wandb==0.15.11``

Usage
-----

* Training

  ``python gpugym/scripts/train.py --task=pbrs:humanoid``
    .. Note:: You shold see something like this

      .. image:: /resources/PBRS_MIT_Humanoid/PBRS_MIT_Humanoid_Training.png
        :align: center
        :width: 700

    * To run on CPU add following arguments: --sim_device=cpu, --rl_device=cpu (sim on CPU and rl on GPU is possible).
    * To run headless (no rendering) add --headless.
    * Important: To improve performance, once the training starts press v to stop the rendering. You can then enable it later to check the progress.
    * The trained policy is saved in gpugym/logs/<experiment_name>/<date_time>_<run_name>/model_<iteration>.pt. Where <experiment_name> and <run_name> are defined in the train config.
    * The following command line arguments override the values set in the config files:
  
      * ``--task`` TASK: Task name.
      * ``--resume`` Resume training from a checkpoint
      * ``--experiment_name`` EXPERIMENT_NAME: Name of the experiment to run or load.
      * ``--run_name`` RUN_NAME: Name of the run.
      * ``--load_run`` LOAD_RUN: Name of the run to load when resume=True. If -1: will load the last run.
      * ``--checkpoint`` CHECKPOINT: Saved model checkpoint number. If -1: will load the last checkpoint.
      * ``--num_envs`` NUM_ENVS: Number of environments to create.
      * ``--seed`` SEED: Random seed.
      * ``--max_iterations`` MAX_ITERATIONS: Maximum number of training iterations.

* Implement the trained policy

  ``python gpugym/scripts/play.py --task=pbrs:humanoid``

  .. Note:: This is the result

    .. raw:: html

      <iframe width="560" height="315" src="https://www.youtube.com/watch?v=4AzTJMkW2ZA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

  * By default the loaded policy is the last model of the last run of the experiment folder.
  * Other runs/model iteration can be selected by setting ``load_run`` and ``checkpoint`` in the train config.