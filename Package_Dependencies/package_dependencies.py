
'''
0:
1: 0
2: 0
3: 1,2
4: 3

output: 0, 1, 2, 3, 4
'''



def solution(dependencies):
    visited = set()
    visiting = set() # to check for cycles
    result = []

    def dfs(node, dependency_list):
        if node in visited:
            return

        visiting.add(node)
        visited.add(node)

        for dependency in dependency_list:
            if dependency in visiting:
                raise Exception("Cycle detected")

            if dependency < 0 or dependency >= len(dependencies):
                raise Exception(" Unexpected Package Dependency")

            dfs(dependency,dependencies[dependency])

        result.append(node)
        visiting.remove(node)



    for node, dependency_list  in  enumerate(dependencies):

        if type(dependency_list) != list:
            raise Exception("Expecting dependencies to be in a list")

        dfs(node,dependency_list)


    return result







test_input_1 = [[],[0],[0],[1,2], [3]]


result = solution(test_input_1 )

print(result)