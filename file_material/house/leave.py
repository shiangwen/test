selection = ['Morgana', 'Katerine', 'Louis', 'Arthur', 'Matthrew']
for i in selection:
    print(i)
print()

def final_judge(ans_arg):
    name = ans_arg

    if name == selection[4]:
        print('You catch the thief, good job!')
    else:
        print('You get a wrong person, and the thief is still at large! Check your code again.')

suspect = input('Who is the thief?\n')
final_judge(suspect)
