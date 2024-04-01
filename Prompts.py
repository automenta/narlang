Prompts_belief_start = """
RelationClaim(noun,verb,noun) ... this relation is claimed to be true in the sentence
RelationClaim(noun,"IsA",noun) ... this relation is claimed to be true in the sentence
PropertyClaim(noun,"HasProperty", adjective) ... this relation is claimed to be true in the sentence
NegatedRelationClaim(noun,verb,noun) ... this relation is claimed to be false in the sentence with an explicit 'not' word
NegatedRelationClaim(noun,"IsA",noun) ... this relation is claimed to be false in the sentence with an explicit 'not' word
NegatedPropertyClaim(noun,"HasProperty",adjective) ... this relation is claimed to be false in the sentence with an explicit 'not' word

Capture the complete sentence meaning with code that calls the four functions.
Please make sure that the word "not" is not included in your call, just use the functions and Negated functions instead.
And use verbs for comparative relations!

Memory:
"""

Prompts_belief_end = "Encode all relations in the sentence, and the sentence has to be believed!"

Prompts_question_start = """
Mention concrete memory contents with certainty values.
Use the minimum involved certainty value.

Memory:
"""

Prompts_question_end = " according to Memory and which memory item i? Answer in a probabilistic sense and within 15 words based on memory content only."
#If it should be allowed to consider GPT's 'weight-based' knowledge too, set IncludeGPTKnowledge=True, then the following is utilized:
Prompts_question_end_alternative = " according to Memory and which memory item i? Answer in a probabilistic sense and within 15 words. Make sure to answer with your own beliefs instead of memory contents only if there is no memory item!"
