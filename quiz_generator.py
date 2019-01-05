import random

capital = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

states = list(capital.keys())
capitals = capital.values()
ques_set = 3

for set_no in range(ques_set):
    with open('Set ' + str(set_no + 1) + '.txt', 'w') as q, open('Answer Sheet No {}.txt'.format(set_no+1), 'w') as a:
        random.shuffle(states)
        q.write('Questions for SET-{}\n\n\n'.format(set_no+1))
        a.write('Answers for SET-{}\n\n\n'.format(set_no+1))
        for i in range(len(states)):
            q.write('Q{0}. What is the capital of the state {1}?\n'.format(i+1, states[i]))
            correct_option = [capital[states[i]]]
            wrong_options = random.sample(set(capitals).difference(correct_option), 3)
            options = correct_option + wrong_options
            random.shuffle(options)
            q.write('A. {0},\nB. {1},\nC. {2},\nD. {3}\n\n'.format(options[0], options[1], options[2], options[3]))
            a.write('{0}) {1}\n'.format(i+1, 'ABCD'[options.index(correct_option[0])]))






