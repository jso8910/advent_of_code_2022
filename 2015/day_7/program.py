SIXTEEN_BIT_MASK = 0b1111111111111111


def get_input():
    with open("day_7/input.txt", "r") as f:
        file = f.read().splitlines()

    # TODO make sure this code works
    ops = {}
    for line in file:
        match line.split(" "):
            case [in1, "LSHIFT", in2, "->", out]:
                ops[out] = {"op": "LSHIFT", "in1": in1,
                            "in2": int(in2), "res": None}
            case [in1, "RSHIFT", in2, "->", out]:
                ops[out] = {"op": "RSHIFT", "in1": in1,
                            "in2": int(in2), "res": None}
            case [in1, op, in2, "->", out]:
                ops[out] = {"op": op, "in1": in1 if not in1.isdigit() else int(
                    in1), "in2": in2 if not in2.isdigit() else int(in2), "res": None}
            case [in1, "->", out]:
                ops[out] = {"op": None, "in1": in1 if not in1.isdigit()
                            else int(in1), "in2": None, "res": None if not in1.isdigit() else int(in1)}
            case ["NOT", in1, "->", out]:
                ops[out] = {"op": "NOT", "in1": in1 if not in1.isdigit() else int(
                    in1), "in2": None, "res": None}

    return ops


def part_one(ops: dict):
    while ops["a"]["res"] is None:
        for key, op in ops.items():
            both_val = True
            if (isinstance(op["in1"], str) and ops[op["in1"]]["res"] is None) and op["in1"] is not None:
                both_val = False
            elif isinstance(op["in1"], str):
                val_1 = ops[op["in1"]]["res"]
            else:
                val_1 = op["in1"]
            if (isinstance(op["in2"], str) and ops[op["in2"]]["res"] is None) and op["in2"] is not None:
                # if (isinstance(op["in2"], str) and ops[op["in2"]]["res"]) and not isinstance(op["in2"], int):
                both_val = False
            elif isinstance(op["in2"], str):
                val_2 = ops[op["in2"]]["res"]
            else:
                val_2 = op["in2"]

            if both_val:
                operation = op["op"]
                match operation:
                    case "AND":
                        ops[key]["res"] = val_1 & val_2
                    case "OR":
                        ops[key]["res"] = val_1 | val_2
                    case "LSHIFT":
                        ops[key]["res"] = (val_1 << val_2) & SIXTEEN_BIT_MASK
                    case "RSHIFT":
                        ops[key]["res"] = (val_1 >> val_2) & SIXTEEN_BIT_MASK
                    case "NOT":
                        ops[key]["res"] = 2**16-1 - val_1
                    case None:
                        ops[key]["res"] = val_1
    return ops["a"]["res"]


def part_two(ops: dict):
    ops["b"] = {"in1": "b", "in2": None,
                "op": None, "res": part_one(__import__('copy').deepcopy(ops))}

    while ops["a"]["res"] is None:
        for key, op in ops.items():
            both_val = True
            if (isinstance(op["in1"], str) and ops[op["in1"]]["res"] is None) and op["in1"] is not None:
                both_val = False
            elif isinstance(op["in1"], str):
                val_1 = ops[op["in1"]]["res"]
            else:
                val_1 = op["in1"]
            if (isinstance(op["in2"], str) and ops[op["in2"]]["res"] is None) and op["in2"] is not None:
                # if (isinstance(op["in2"], str) and ops[op["in2"]]["res"]) and not isinstance(op["in2"], int):
                both_val = False
            elif isinstance(op["in2"], str):
                val_2 = ops[op["in2"]]["res"]
            else:
                val_2 = op["in2"]

            if both_val:
                operation = op["op"]
                match operation:
                    case "AND":
                        ops[key]["res"] = val_1 & val_2
                    case "OR":
                        ops[key]["res"] = val_1 | val_2
                    case "LSHIFT":
                        ops[key]["res"] = (val_1 << val_2) & SIXTEEN_BIT_MASK
                    case "RSHIFT":
                        ops[key]["res"] = (val_1 >> val_2) & SIXTEEN_BIT_MASK
                    case "NOT":
                        ops[key]["res"] = 2**16-1 - val_1
                    case None:
                        ops[key]["res"] = val_1
    return ops["a"]["res"]


print(part_one(get_input()))
print(part_two(get_input()))
