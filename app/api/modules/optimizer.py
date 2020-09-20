import itertools
import numpy as np
from . import GMapsClient


class Optimizer():
    def __init__(self):
        self.key = "AIzaSyAawqXhPMAidvfDLqPs_cRn9gXVPsT59bs"
        self.gmapsClient = GMapsClient()

    def construct_cost_matrix(self, demanders_list, suppliers_list):
        demander_count = len(demanders_list)
        cost_matrix = np.ones((demander_count, demander_count + 1))

        for row in list(range(0, demander_count)):
            current_demander = demanders_list[row]
            current_demander_asphalt_demand = current_demander["amount"]
            for col in list(range(0, demander_count + 1)):
                if (col == 0):
                    current_travel_time = self.gmapsClient.predict_travel_time(
                        suppliers_list[0], current_demander)
                    cost_matrix[
                        row,
                        col] = current_demander_asphalt_demand / current_travel_time
                elif (col == row + 1):
                    cost_matrix[row, col] = 0
                else:
                    current_travel_time = self.gmapsClient.predict_travel_time(
                        demanders_list[row - 1], demanders_list[row])
                    cost_matrix[
                        row,
                        col] = current_demander_asphalt_demand / current_travel_time

        return cost_matrix

    def start_optimization(self, demanders_list, suppliers_list):

        demander_count = len(demanders_list)
        iterable = list(range(1, demander_count + 1))

        all_combos = itertools.permutations(iterable, demander_count)
        all_combos = list(all_combos)
        all_combos = np.asarray(all_combos)
        print(all_combos, flush=True)

        cost_matrix = self.construct_cost_matrix(demanders_list,
                                                 suppliers_list)
        cost_sum_matrix = np.zeros(all_combos.shape)
        print(cost_matrix, flush=True)
        num_rows, num_cols = cost_sum_matrix.shape
        print(cost_sum_matrix.shape[0], flush=True)
        print(list(range(0, num_rows)), flush=True)

        for col in list(range(0, num_cols)):
            for row in list(range(0, num_rows)):

                current_node = all_combos[row, col]
                if (col == 0):
                    cost_sum_matrix[row, col] = cost_matrix[col, 0]
                else:
                    past_node = all_combos[row, col - 1]
                    cost_sum_matrix[row, col] = cost_sum_matrix[
                        row, col - 1] + cost_matrix[current_node - 1,
                                                    past_node]

        print(cost_sum_matrix, flush=True)
