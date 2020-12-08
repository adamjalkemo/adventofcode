accumulator = 0


from pathlib import Path

with Path("input.txt").open() as f:
    instructions = f.read().splitlines()


print("Part 1:")


def run_instructions(instructions):
    visited_instructions = set()
    accumulator = 0
    instruction_idx = 0
    while True:
        if instruction_idx in visited_instructions:
            break
        if instruction_idx == len(instructions):
            break

        visited_instructions.add(instruction_idx)
        instruction = instructions[instruction_idx]
        if "nop" in instruction:
            instruction_idx += 1
        elif "jmp" in instruction:
            instruction_idx += int(instruction.split()[1])
        elif "acc" in instruction:
            accumulator += int(instruction.split()[1])
            instruction_idx += 1
        else:
            raise NotImplementedError
    return instruction_idx, accumulator


_, accumulator = run_instructions(instructions)
print(
    f"Solution: The accumulator is at {accumulator} when the same instruction is visited again"
)
assert accumulator == 1816


print("Part 2:")
accumulator = 0
nbr_instructions = len(instructions)
for i in range(nbr_instructions):
    fixed_instructions = list(instructions)
    if "jmp" in fixed_instructions[i]:
        fixed_instructions[i] = fixed_instructions[i].replace("jmp", "nop")
    elif "nop" in fixed_instructions[i]:
        fixed_instructions[i] = fixed_instructions[i].replace("nop", "jmp")
    instruction_idx, accumulator = run_instructions(fixed_instructions)
    if instruction_idx == nbr_instructions:
        break
else:
    raise Exception
print(f"Solution: The accumulator is at {accumulator} when the program exits")
assert accumulator == 1149
