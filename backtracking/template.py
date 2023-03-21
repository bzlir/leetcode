# res = []
# def backtracking(self,path, choices):

#     if self.accept(path, choices):
#         res.append(path)
#         return

#     # drill down
#     for cur_candidate in choices:
#         self.make_choice()
#         self.backtracking(path, choices)
#         self.reject()