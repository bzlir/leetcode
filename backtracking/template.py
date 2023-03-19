def backtracking(self, data, candidate):
    # pruning
    if self.reject(data, candidate):
        return

    # reach the end
    if self.accept(data, candidate):
        return self.output(data, candidate)

    # drill down
    for cur_candidate in self.all_extension(data, candidate):
        # or you can choose to prune here, recursion depth - 1
        if not self.should_to_be_pruned(cur_candidate):
            self.backtracking(data, cur_candidate)