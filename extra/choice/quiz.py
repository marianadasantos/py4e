from cl import questions

question_prompts = [
    'What color are apples?\n(a) Red/Green\n(b) Purple\n(c)Orange\n\n',
    'What color are bananas\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
    'What color are strawberries?\n(a) Yellow\n(b) Blue\n(c) Red\n\n'
]

question = [
    questions(question_prompts[0], 'a'),
    questions(question_prompts[1], 'c'),
    questions(question_prompts[2], 'c'),
]

def run_test(quest):
    score = 0
    for question in quest:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print('You got ' + str(score) + ' out of ' + str(len(quest)) + ' correct.' )

run_test(question)