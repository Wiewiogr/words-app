def parse_srt_format(content):
    word_list = []

    lines = content.split("\n")[2:]
    counter = 2
    should_skip = False

    for line in lines:
        if len(line) <= 0:
            continue

        if should_skip:
            should_skip = False
            continue

        if line.rstrip() == str(counter):
            counter += 1
            should_skip = True
            continue


        for word in line.rstrip().split(" "):
            word_list.append(word)

    return word_list
