def flatten(root):
    if root == None or root.next == None:
        return root
    root.next = flatten(root.next)
    root = sortedMerge(root, root.next)
    return root


def sortedMerge(a, b):
    if a is None:
        return b
    elif b is None:
        return a

    if a.data < b.data:
        result = a
        result.down = sortedMerge(a.down, b)
    else:
        result = b
        result.down = sortedMerge(a, b.down)
    result.next = None
    return result
