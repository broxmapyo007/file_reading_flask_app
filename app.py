from flask import Flask, request, render_template
import os
import chardet

app = Flask(__name__)


def read_ls(name, s, e):  # filename,start,end
    # print("file ", os.listdir("files"))
    print(s, e)
    con = ""
    con2 = []
    if name + ".txt" in os.listdir("files"):
        fname = f"files/{name}.txt"
        # print("open : ", fname)
        result = chardet.detect(open(fname, "rb").read())
        charenc = result["encoding"]
        with open(fname, encoding=charenc, errors="ignore") as ff:
            content = ff.readlines()
        if s:
            s = int(s)
        else:
            s = 0
        if e:
            e = int(e)
        else:
            e = len(content)
        if s > e:
            s, e = e, s
        for i in content[s : e + 1]:
            con += i + "\n"
            con2.append(i)
        print(con2)
        return con2
    return "Wrong file,no data"


@app.route("/", defaults={"name": "file1"})
# eg of url :"http://127.0.0.1:5000/file4?start=0&end=10"
@app.route("/<string:name>", methods=["GET"])
def index(name):
    st, en = "", ""
    if "start" in request.args.keys():
        st = request.args["start"]
    if "end" in request.args.keys():
        en = request.args["end"]
    if request.method == "GET":
        fc = ""
        if name:
            if st != "" or en != "":
                fc = read_ls(name, st, en)
            else:
                fc = read_ls(name, 0, 0)
        return render_template(
            "index.html", fname=name, file_c=fc, s=st, e=en
        )  # file name,ile content,start,end
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
