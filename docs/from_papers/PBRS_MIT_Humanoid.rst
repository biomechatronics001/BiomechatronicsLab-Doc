Potential Based Rewards for Learning Humanoid Locomotion
========================================================

Reference: [2023PBRS]_

.. [2023PBRS] Jeon, S. H., Heim, S., Khazoom, C., & Kim, S. (2023, May). Benchmarking potential based rewards for learning humanoid locomotion. In 2023 IEEE International Conference on Robotics and Automation (ICRA) (pp. 9204-9210).

Paper: https://ieeexplore.ieee.org/abstract/document/10160885/

GitHub link: https://github.com/se-hwan/pbrs-humanoid

.. note::

    * Procedure tested by Apr. 1st, 2024 by Ivan Lopez-Sanchez.
    * I tested this code on Linux 18.04 with Python 3.6.9 (authors recommend Python 3.8).
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

<<<<<<< Updated upstream:docs/from_papers/PBRS_MIT_Humanoid.rst
  1. Download Isaac Gym Preview 4 from https://developer.nvidia.com/isaac-gym (extract the zip package, copy the isaacgym folder in the virtual enviornment directory)
=======
  1. Download Isaac Gym Preview 4 from https://developer.nvidia.com/isaac-gym
  2. Extract the zip package in MITlegged virtual environment folder
  3. 
>>>>>>> Stashed changes:docs/from papers/apple.rst
