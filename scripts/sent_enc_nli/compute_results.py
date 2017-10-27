scores = []
labels = []
labels_map = {'0': 'ENTAILMENT', '1': 'NEUTRAL', '2': 'CONTRADICTION'}

with open('results/taska.txt') as f:
    for l in f:
        labels.append(l)

with open('results/taskb.txt') as f:
    for l in f:
        scores.append(l)

lines = []
with open('../../data/SICK_test.txt') as f:
    for l in f:
        lines.append(l)

with open('results/Results.txt', 'w') as f:
    head_cols = lines[0].strip().split('\t')
    f.write(head_cols[0].strip())
    f.write('\t')
    f.write(head_cols[3].strip())
    f.write('\t')
    f.write(head_cols[4].strip())
    f.write('\n')
    for i in range(1,len(lines)):
        f.write(lines[i].strip().split('\t')[0])
        f.write('\t')
        f.write(scores[i-1].strip())
        f.write('\t')
        f.write(labels_map[labels[i-1].strip()])
        f.write('\n')
