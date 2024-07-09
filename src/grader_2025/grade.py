import json

def part1_grader(answer):
    ret = []
    qid = 0
    for group in answer:
        for q in group:
            ret.append({f'question_{qid + 1}': f'{q}'})
            qid += 1

    js = {"part1": ret}

    # print(js)
    retJson = json.dumps(js)

    return retJson

def part2_grader(answer):
    ret = []
    qid = 1
    for question in answer:
        cur = []
        for q in question:
            cur.append(q)

        ret.append({f'question_{qid}': cur})
        # print(q)
        qid += 1
    js = {"part2": ret}
    return json.dumps(js)

def part3_grader(answer):
    ret = []
    qid = 1
    for question in answer:
        cur = []
        for q in question:
            cur.append(q)

        ret.append({f'question_{qid}': cur})
        # print(q)
        qid += 1
    js = {"part3": ret}
    return json.dumps(js)

def get_info(answer):
    js = {"sbd" : answer[0], "mdt" : answer[1]}
    return json.dumps(js)