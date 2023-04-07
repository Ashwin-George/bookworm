import nltk
from nltk.tree import Tree

dependency_tree = ('said', ['John', 'he', ('likes', ['dogs'])])
pos_tags = [('John', 'NNP'), ('said', 'VBD'), ('he', 'PRP'), ('likes', 'VBZ'), ('dogs', 'NNS')]

def to_parse_tree(dependency_tree, pos_tags):
    root_label, children = dependency_tree
    if isinstance(children, str):
        pos_tag = next((tag for (word, tag) in pos_tags if word == children), None)
        return Tree(root_label, [Tree(pos_tag, [children])])
    else:
        children_trees = []
        for child in children:
            if isinstance(child, str):
                pos_tag = next((tag for (word, tag) in pos_tags if word == child), None)
                children_trees.append(Tree(pos_tag, [child]))
            else:
                children_trees.append(to_parse_tree(child, pos_tags))
        return Tree(root_label, children_trees)

parse_tree = to_parse_tree(dependency_tree, pos_tags)

print(parse_tree)
