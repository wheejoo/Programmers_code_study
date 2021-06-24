def solution(max_weight, specs, names):
    d_specs = dict(specs)
    weight = 0
    answer = 1
    for name in names:
        weight += int(d_specs.get(name))
        if max_weight < weight:
            answer += 1
            weight = int(d_specs.get(name))
    return answer
