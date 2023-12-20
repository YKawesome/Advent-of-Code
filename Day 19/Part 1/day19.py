from collections import namedtuple


WorkflowStep = namedtuple('WorkflowStep', ['condition', 'destination'])
Condition = namedtuple('Condition', ['var', 'type', 'value'])


def get_file_data(kind: str) -> tuple[list[str], list[str]]:
    '''Gets the data from the file.'''
    f = open(f'Day 19/day19{kind}.txt', 'r')
    data = [line.strip() for line in f.readlines()]
    workflows = []
    items = []

    for i, line in enumerate(data):
        if line == '':
            workflows = data[:i]
            items = data[i+1:]
            break

    return workflows, items


def make_workflows(data: list[str]) -> dict[str, list[WorkflowStep]]:
    '''Makes the workflows from the data.'''
    workflows = {}
    for line in data:
        name, wf_steps = make_workflow(line)
        workflows[name] = wf_steps
    return workflows


def make_workflow(line: str) -> tuple[str, list[WorkflowStep]]:
    '''Makes a workflow from a line of data.'''
    name, remainder = line.split('{')
    conditions = remainder[:-1].split(',')
    wf_steps = []
    for condition in conditions:
        if len(x := condition.split(':')) == 2:
            var = x[0][0]
            _type = x[0][1]
            value = int(x[0][2:])
            wf_steps.append(WorkflowStep(Condition(var, _type, value), x[1]))
        else:
            wf_steps.append(WorkflowStep(None, x[0]))
    return name, wf_steps


def make_items(data: list[str]) -> list[dict[str, int]]:
    '''Makes the items from the data.'''
    items = []
    for line in data:
        items.append(make_item(line))
    return items


def make_item(line: str) -> dict[str, int]:
    '''Makes an item from a line of data.'''
    item = {}
    line = line[1:-1]
    for x in line.split(','):
        var = x[0]
        value = int(x[2:])
        item[var] = value
    return item


def item_acceptable(item: dict[str, int], workflows: dict[str, list[WorkflowStep]]) -> bool:
    '''Checks if an item is acceptable.'''
    wf_steps = workflows['in']
    while True:
        for step in wf_steps:
            if step.condition is None:
                if step.destination == 'A':
                    return True
                elif step.destination == 'R':
                    return False
                else:
                    wf_steps = workflows[step.destination]
                    break
            else:
                condition = step.condition
                if condition.type == '>':
                    if item[condition.var] > condition.value:
                        if step.destination == 'A':
                            return True
                        elif step.destination == 'R':
                            return False
                        wf_steps = workflows[step.destination]
                        break
                elif condition.type == '<':
                    if item[condition.var] < condition.value:
                        if step.destination == 'A':
                            return True
                        elif step.destination == 'R':
                            return False
                        wf_steps = workflows[step.destination]
                        break


def run() -> None:
    '''Runs the program'''
    workflow_data, item_data = get_file_data('input')

    workflows = make_workflows(workflow_data)
    items = make_items(item_data)

    accepted_items = filter(lambda item: item_acceptable(item, workflows), items)
    total_value = sum(sum(item.values()) for item in accepted_items)
    print(total_value)


if __name__ == '__main__':
    run()
