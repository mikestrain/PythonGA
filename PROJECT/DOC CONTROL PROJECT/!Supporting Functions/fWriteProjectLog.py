# %%
from datetime import datetime
dt_string = datetime.now().strftime(r"%Y/%m/%d")

def fWriteProjectLog(Queue):

    project_dict = {}
    file_list = []

    for u_number in Queue:

        project = Queue[u_number][-1]['doc_project']
        try: project_dict[project].append(u_number) # there has been a previous entry
        except: project_dict[project] = [u_number]  # this is the first file for this project

    with open("Project_Running_Totals.txt", "a") as my_file:
        for pj in project_dict:
            line_to_write = (dt_string + ',' + str(pj) + ',' + str(len(project_dict[pj])) + ',' + str(project_dict[pj]) + '\n')
            my_file.writelines(line_to_write)


# %%
