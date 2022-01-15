import numpy as np
obs_mask = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02])

# def termination_function(paths):
#     for path in paths:
#         obs = path["observations"]
#         angle = obs[:, 1]
#         T = obs.shape[0]
#         t = 0
#         done = False
#         while t < T and done is False:
#             # print("Cheetah angle: {}".format(angle[t]))
#             done = abs(angle[t]) > 2.5
#             t = t + 1
#             T = t if done else T
#
#         # if done:
#         #     path["rewards"][T-1] -= 6000
#
#         path["observations"] = path["observations"][:T]
#         path["actions"] = path["actions"][:T]
#         path["rewards"] = path["rewards"][:T]
#         path["terminated"] = done
#     return paths
