"""2115. Find All Possible Recipes from Given Supplies

link: leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

problem: You have information about n different recipes. You are given a string
array recipes and a 2D string array ingredients. The ith recipe has the name
recipes[i], and you can create it if you have all the needed ingredients from
ingredients[i]. Ingredients to a recipe may need to be created from other
recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that
you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer
in any order.

Note that two recipes may contain each other in their ingredients.

Example 1:
Input: recipes = ["bread"],
ingredients = [["yeast", "flour"]],
supplies = ["yeast","flour","corn"]

Output: ["bread"]

Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Example 2:
Input:
recipes = ["bread", "sandwich"],
ingredients = [["yeast", "flour"], ["bread", "meat"]],
supplies = ["yeast", "flour", "meat"]

Output: ["bread", "sandwich"]

Explanation:
- We can create "bread" since we have the ingredients "yeast" and "flour".
- We can create "sandwich" since we have the ingredient "meat" and can create
the ingredient "bread".

Example 3:
Input:
recipes = ["bread", "sandwich", "burger"],
ingredients = [["yeast", "flour"], ["bread", "meat"],
               ["sandwich", "meat", "bread"]],
supplies = ["yeast", "flour", "meat"]

Output: ["bread","sandwich","burger"]

Explanation:
- We can create "bread" since we have the ingredients "yeast" and "flour".
- We can create "sandwich" since we have the ingredient "meat" and can create
the ingredient "bread".
- We can create "burger" since we have the ingredient "meat" and can create the
ingredients "bread" and "sandwich".

Constraints:
- n == recipes.length == ingredients.length
- 1 <= n <= 100
- 1 <= ingredients[i].length, supplies.length <= 100
- 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
- recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase
English letters.
- All the values of recipes and supplies combined are unique.
- Each ingredients[i] does not contain any duplicate values.
"""


# non-intuitive topsort
from collections import deque


class Solution:
    def findAllRecipes(self,
                       recipes: List[str],
                       ingredients: List[List[str]],
                       supplies: List[str]) -> List[str]:
        def build_graph(set_recipes):
            graph = {supply: [0, set()] for supply in supplies}
            graph.update({recipe: [0, set()] for recipe in recipes})

            for i, recipe in enumerate(recipes):
                for ingredient in ingredients[i]:
                    if ingredient in graph:
                        graph[ingredient][1].add(recipe)
                        graph[recipe][0] += 1
                    else:
                        # the ingredient is not in the supply, flag the recipe
                        # as -1 to say it can't be made.
                        graph[recipe][0] = -1

            return graph

        def bfs(graph, source, set_recipes):
            visited = {source}
            queue = deque([source])
            can_be_done = []

            while queue:
                curr = queue.popleft()
                if curr in set_recipes:
                    can_be_done.append(curr)
                for neighbor in graph[curr][1]:
                    if neighbor not in visited and graph[neighbor][0] != -1:
                        graph[neighbor][0] -= 1
                        if graph[neighbor][0] == 0:
                            visited.add(neighbor)
                            queue.append(neighbor)

            return can_be_done

        set_recipes = set(recipes)
        graph = build_graph(set_recipes)
        res = []

        for supply in supplies:
            res.extend(bfs(graph, supply, set_recipes))

        return res
