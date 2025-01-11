import pandas as pd


def main(name, n_level):
    df = pd.read_csv(f"{name}.csv", header=None)
    df = df.transpose()

    js_arrays = {}
    for i in range(n_level):
        js_arrays[i] = "["

    for i in df:
        df_i = df[i]
        js_arrays[df_i[3]] += f"['{df_i[0]}','{df_i[1]}','{df_i[2]}'],\n"

    for i in js_arrays:
        js_arrays[i] = js_arrays[i].removesuffix(",\n")
        js_arrays[i] += "]"

    js = f"{name}=[\n"
    for i in js_arrays:
        js += f"{js_arrays[i]},\n"
    js = js.removesuffix(",\n")
    js += "];\n"

    with open(f"{name}.js", "w") as js_file:
        js_file.write(js)


if __name__ == "__main__":
    main("terms", 10)
