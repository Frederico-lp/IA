from algorithms import *
from utils import *

if __name__ == "__main__":

    team = read_dataset("a")

    sol = Solution(team)

    print("Random solution: ", sol.solution)

    sol1, hill_evals = sol.hill_climbing()
    print("Best value with hill climbing was ", sol1)

    sol2, annealing_evals = sol.simulated_annealing()
    print("Best value with simulated annealing was ", sol2)


    size_of_pop = int(input("Input the desired population size: "))

    parents_algorithm = int(input("Select one of the following algorithms to select the parents: \n1) tournament selection \n2) roulette_selection\n"))

    crossover_algorithm = int(input("Select one of the following algorithms to select the crossover function: \n1)First half of parent 1 and second half of parent 2 \n2)First half of parent 2 and second half of parent 1 \n3)Randomly choose between 1) and 2)\n"))

    sol3, genetic_evals = sol.genetic_algorithm(size_of_pop, parents_algorithm, crossover_algorithm)
    print("Best value with genetic algorithm was ", sol3)

    sol4, tabu_evals = sol.tabu_search()
    print("Best value with tabu search was ", sol4)

    plt.plot(hill_evals, 'g', label='Hill Climbing')
    plt.plot(annealing_evals, 'b', label='Simulated Annealing')
    plt.plot(genetic_evals, 'r', label='Genetic Algorithm')
    plt.plot(tabu_evals, 'k', label='Tabu Search')

    plt.title('Title')

    plt.xlabel('iteration')

    plt.ylabel('evaluation')

    plt.legend()

    plt.show()


