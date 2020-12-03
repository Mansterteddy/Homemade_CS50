import re

line_list = []
with open("raw.txt", "r", encoding="utf8") as f:
    for line in f:
        line_list.append(line.strip())

raw_text = line_list[0]

qa_list = re.split("[0-9]+\. ", raw_text)
print(len(qa_list))

res_list = []
for item in qa_list[1:]:
    print(item)

    candidate_a = re.search("A\. ", item)
    candidate_b = re.search("B\. ", item)
    candidate_c = re.search("C\. ", item)
    candidate_d = re.search("D\. ", item)
    candidate_e = re.search("E\. ", item)
    student_item = re.search("学员答案", item)
    correct_item = re.search("正确答案", item)
    explain_item = re.search("解释说明", item)

    candidate_list = []

    question = item[:candidate_a.start()].replace("", "")
    print(question)

    cand_a = item[candidate_a.start():candidate_b.start()]
    candidate_list.append(cand_a)

    if candidate_c != None:
        cand_b = item[candidate_b.start():candidate_c.start()]
        candidate_list.append(cand_b)
    else:
        cand_b = item[candidate_b.start():student_item.start()]
        candidate_list.append(cand_b)

    if candidate_c != None:
        if candidate_d != None:
            cand_c = item[candidate_c.start():candidate_d.start()]
            candidate_list.append(cand_c)
        else:
            cand_c = item[candidate_c.start():student_item.start()]
            candidate_list.append(cand_c) 

    if candidate_d != None:
        if candidate_e != None:
            cand_d = item[candidate_d.start():candidate_e.start()]
            candidate_list.append(cand_d)
        else:
            cand_d = item[candidate_d.start():student_item.start()]
            candidate_list.append(cand_d)

    if candidate_e != None:
        cand_e = item[candidate_e.start():student_item.start()]
        candidate_list.append(cand_e)
    
    print(candidate_list)

    answer = item[correct_item.start():explain_item.start()]
    print(answer)

    explain = item[explain_item.start():]
    print(explain)

    res_list.append((question, candidate_list, answer, explain))

print(len(res_list))

with open("res.tsv", "w", encoding="utf8") as w:
    for item in res_list:
        question = item[0]
        candidate_list = item[1]
        answer = item[2]
        explain = item[3]

        new_line = question + "\t" + str(candidate_list) + "\t" + answer + "\t" + explain + "\n"
        w.write(new_line)