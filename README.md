

<img src="https://user-images.githubusercontent.com/8284677/232368549-5337cf02-63fd-43ae-bf15-6ba9935a5419.png" width="200px">

Language model to build representations for Non-Axiomatic Reasoning Systems
LLM together with NARS for reasoning on natural language input. 
This system with long-term learning that can be applied to new knowledge.

[![NARS-GPT](https://img.youtube.com/vi/l4rklYGbcTo/0.jpg)](https://www.youtube.com/watch?v=l4rklYGbcTo "Integrating GPT and NARS (gptONA)")

**Features:**

- Interactive NARS-style declarative inference and question answering with long-term memory storage
- Identifies which memory support a specific conclusion, and certainty
- Seamless interfacing with Narsese input and sensorimotor capabilities of NARS.
- The system is able to build and maintain long-term, a useful and evidentally supported set of beliefs through reasoning.
- Various types of reasoning, truth maintenance and automated memory management, which benefit adaptive autonomous agents.
- Applies decades of knowledge about reasoning under uncertainty, evidence tracking and resource allocation in Non-Axiomatic Reasoning Systems

**Architecture:**

![gptONA Architecture](https://user-images.githubusercontent.com/8284677/234759143-0fc48767-68cd-44fc-800a-fc7023e11f37.png)

**Technical aspects:**
- NARchy is industrial strength NARS implementation - the most mature implementation of NARS for large-scale experiments and entertainment
- Sentences are stored in logical/structural form in the memory of NARS whereby introduction of new similar terms is avoided through the usage of embedding similarity of terms.
- Accurate reasoning with Non-Axiomatic Logic truth calculations
- The long-term memory does not have any context window-size limitation.
- The memory can nevertheless be bounded if users desire so, whereby a maximum amount of items remembered by a usefulness ranking (how often an item was accessed and how recently).
- Attention buffer is a view of up to k relevant items in NARS's memory decided based on recency and relevance to other items in the attention buffer, whereby recency is based on the time stamp of when the knowledge item was created, and relevance is decided by cosine similarity of the sentence embedding to the questions's embedding.
- Mentioned certainty values are NAL confidence values, whereby if frequency value is smaller than $0.5$ the belief appears in negated formulation in the prompt.

**Installation:**

Run build.sh (which compiles & runs the ONA implementation of NARS with Clang or GCC)
and also install the depencencies via install_python_dependencies.sh
which will install the OpenAI API and other relevant Python packages.

**How to run:**

```
python3 NarsGPT.py API_KEY=YOUR_OPENAI_API_KEY
```

**Evaluation:**

Relevant folders:

```
./NARS-GPT/Evaluation_babI_qa16/
./NARS-GPT/Evaluation_INT_inf/
```

Side note: As different prompts can lead to different results which would make comparisons less fair,
these scripts ensure the prompts to GPT-4 and NARS-GPT for the task are compatible.
To run vanilla GPT-4 for evaluation on babI for comparison purposes, use the baseline branch.

In each of these folders, run:

```
python3 1_GenerateTestOutput.py API_KEY=YOUR_OPENAI_API_KEY
```
(which runs the model on the QA16 part of babI specified in line 11 of the script and generates TestOutput.json including input, actual and expected output for each example)

```
python3 2_EvaluateTestOutput.py API_KEY=YOUR_OPENAI_API_KEY
```
(which judges output correctness and generates Scores.json, and in addition Correct.json and Incorrect.json with the examples determined as correct and incorrect)

Scores.json then contains the relevant numbers, in terms of Correct amount, Incorrect amount, and the correctness ratio.

Please note that both scripts can be interrupted, with the resulting .json files reflecting the current state.
That way one can also choose to use part of the dataset (say 100-200 examples) for replication.
