from dicts import plot_vars, x_vars, y_vars

with open('prompts.txt', 'r') as f_in, open('prompts_processed.txt', 'w') as f_out:
    for line in f_in:
        formatted_lines = []
        for plot_type in plot_vars:
            for x_ax in x_vars:
                for y_ax in y_vars:
                    f_line = line.format(plot_vars = plot_type["words"], x_vars = x_ax["words"], y_vars = y_ax["words"])
                    f_line = f_line.strip().strip('f"').strip('"') + '\n'
                    formatted_lines.append(f_line)
        f_out.writelines(formatted_lines)