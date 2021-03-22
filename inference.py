from parlai.core.agents import create_agent
from parlai.core.opt import Opt
import re

opt = Opt(
    model_file = 'model',
    interactive_task = True,
    task = 'interactive',
    interactive_mode=True,
    override = {
        'fp16' : True,
        'beam_context_block_ngram' : 3,
        'beam_block_ngram' : 3,
        'inference' : 'topk',
        'topk' : 40,
        'beam_size' : 20,
        'beam_min_length' : 10,
        'temperature' : 0.88
    }
)

agent = create_agent(opt, requireModelExists=True)
agent.opt.log()

def preprocess_sentence(sentence):
    sentence = sentence.lower().strip()
    # creating a space between a word and the punctuation following it
    # eg: "he is a boy." => "he is a boy ."
    sentence = re.sub(r"([?.!,])", r" \1 ", sentence)
    sentence = sentence.replace("'", "' ")
    sentence = re.sub(r'[" "]+', " ", sentence)
    sentence = sentence.strip()
    return sentence

def postprocess_sentence(sentence):
    # remove space before punctuation
    sentence = sentence.rstrip(" .")
    return re.sub(r"\s+(\W)", r"\1", sentence)

def infer_from_history(history):
    agent.reset()
    for message in history:
        reply_text = preprocess_sentence(message)
        reply = {'episode_done': False, 'text': reply_text}
        agent.observe(reply)

    model_res = agent.act()
    text, score = model_res['beam_texts'][0]
    return postprocess_sentence(text), score


def infer_single(message, episode_done=False):
    reply_text = preprocess_sentence(message)
    reply = {'episode_done': episode_done, 'text': reply_text}
    agent.observe(reply)
    model_res = agent.act()
    text, score = model_res['beam_texts'][0]
    return postprocess_sentence(text), score

def main():
    while True:
        sentence = input("Input: ")
        response, score = infer_single(sentence)
        print(response)

if __name__ == '__main__':
  main()