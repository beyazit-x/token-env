import token_env
import gymnasium as gym

if __name__ == '__main__':
    env = gym.make("TokenEnv-v1")
    obs, info = env.reset()
    done = False
    i = 0
    while not done:
        i += 1
        action = env.action_space.sample()
        # print("obs:", obs)
        # print("action:", action)
        obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        # print("next obs:", obs)
        # print("reward:", reward)
        # print("label:", token_env.TokenEnv.label_f(obs))
        # input()
    env.close()
