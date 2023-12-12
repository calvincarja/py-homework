line_sum = []
line_count = 0
line_total = 0
with open('/Users/calvinpineda/Downloads/mbox-short.txt','r') as file:
    for x in file:
        if x.startswith('X-DSPAM-Confidence:'):
            line_count += 1
            non_space = x.strip()
            line_split = non_space.split(':')
            line_sum.append(float(line_split[1]))
            line_total += float(line_split[1]) # keep a running total
line_cal = line_total/line_count
print('Average spam confidence: ',line_cal)
