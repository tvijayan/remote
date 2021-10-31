import re

ghost = open("D:\\Thiru\\logdna\\qa_ghost_enroll_20210330.jsonl", "r")


regex = re.compile(r'7069[0-9]{12}')

for line in ghost:
    log_file = regex.findall(line)
    tombstone = open("d:\\thiru\\logdna\\20210330-ghost-cards.txt", "a")
    for card in log_file:
        # print (card)
        tombstone.write(card + "\n")
tombstone.close()
