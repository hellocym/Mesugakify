import litellm
from config import cfg


# https://open.bigmodel.cn/api/paas/v4

def mesugakify(text: str) -> str:
    response = litellm.completion(
        model="openai/CharGLM-3",               # add `openai/` prefix to model so litellm knows to route to OpenAI
        api_key=cfg.get("OPENAI_API_KEY"),                  # api key to your openai compatible endpoint
        api_base="https://open.bigmodel.cn/api/paas/v4",     # set API Base of your Custom OpenAI Endpoint
        messages=[
                    {
                        "role": "user",
                        "content": "Hey, how's it going?",
                    }
        ],
    )
    print(response)

if __name__ == "__main__":
    mesugakify("Hello, world!")