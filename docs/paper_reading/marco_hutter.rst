ETH Marco Hutter
================

Learning agile and dynamic motor skills for legged robots
---------------------------------------------------------

Reference: [2019SR-MarcoHutter]_

.. [2019SR-MarcoHutter] J\. Hwangbo, J\. Lee, A. Dosovitskiy, D. Bellicoso, V. Tsounis, V. Koltun, and M. Hutter, “Learning agile and dynamic motor skills for legged robots,” Sci. Robot., vol. 4, no. 26, p. eaau5872, Jan. 2019.

Insights
^^^^^^^^

* Although the proposed approach allows for largely automated discovery of performant policies, it still requires some human expertise.

  * Takes about 2 days for the locomotion policies presented in this work.
  * Developing the recovery policy took about a week largely owing to the fact that some safety concerns.
  * Constructing an analytical actuator model for ANYmal takes at least 3 weeks even if there is a very similar model studied in literature

* A single neural network trained in one session manifests **single-faceted** behaviors that do not generalize across multiple tasks.
* One of the biggest challenges with walking robots is the dynamics at intermittent contacts. This requires rigid body contact solver presented in the previous work (ref41)
* SEA modeling

  * SEAs are extremely difficult to model accurately. The SOTA model includes nearly 100 parameters.
  * The authors assumed that the network could be trained to estimate the internal states given a history of position errors and velocities, because otherwise the given information is simply insufficient to control the robot adequately.
  * The length of the history should be chosen such that it is sufficiently longer than the sum of all communication delays and the mechanical response time.

* Training setup

  * The nonlinearity has a strong effect on performance on the physical system. ﻿Unbounded activation functions, such as rectified linear unit, can degrade performance on the real robot, because actions can have very high magnitude when the robot reaches states that were not visited during training. Softsign activation function is used in this paper.
  * TRPO is used for training.
  * Peng and van de Panne (ref57) found that a low-impedance PD controller using desired joint positions can outperform a torque controller in both training speed and final control performance.
  * Position controllers are sometimes limited in performance when the position reference is time indexed, which means that there is a higher-level controller that assumes that the position plan will be followed at high accuracy. This is the main reason that torque controllers have become popular in legged robotics. However, as in many other RL literature, the proposed control policy is state indexed and does not suffer from the limitations of common PD controllers.
  * The policy with the ability to exert appropriate impulse on the environment for locomotion enables robustness because impulse-based control approaches are known to be more robust against system changes and model inaccuracies (ref44).
  * Use of curriculum-based learning scheme allows the robot first learn how to achieve the objective and then how to respect various constraints.
  * A sufficiently high discount factor shows more natural standing posture owing to the fact that it penalizes standing torque more than motion (torque, joint velocities, and other quantities incurring due to motion).
  * Another crucial detail is that joint velocities cannot be directly measured on the real robot. Removing velocities from the observation altogether led to a complete failure to train, although in theory, the policy network could infer velocities as finite differences of observed positions.
  * Controller performance is unexpectedly insensitive to the control rate when the maneuver has low joint velocities.


Keynote speech Marco Hutter ICRA 2022
-------------------------------------

Link: https://www.youtube.com/watch?v=abdLIFOzdRo

Insights
^^^^^^^^

* Currently, the most challenging part (where there is a lot to do) of achieving autonomy for legged robots is Planning.
* Planning involves both continuous (motion, ref torque) and discrete (foothold/contact) parts.
* robot can estimate environment property (e.g., friction coefficient).
* Reflexes might be important for handling unexpected environment (related to saliency map, video does not say too much about this)
  
* Future work
  
  * They want to do end-to-end between target position and actuator command generation: currently there are intermediate steps like path planning, path following, locomotion. They want to eliminate these steps via a network.   
  
    .. image:: /resources/paper_reading/marco_hutter/planning_end_to_end.png
       :align: center
       :width: 500

  * To understand the environment with very few sensor measurement + using the synthetic/real-world data used during training to predict the properties of the environment. 
  * Manipulate the environment through robotic arms.
  * Become faster and more efficient