#!/bin/python2
from imports import *


def main_wrapper(argv):
    assert (len(argv) == 2)

    dBase = shelve.open(argv[0])
    dProject = deepcopy(dBase["dProject"])
    intervalData = deepcopy(dBase["intervalData"])

    if "OfSc" in dProject.keys():
        dProject["Satd"] = {}
        dProject["Satd"] = dProject["OfSc"]
        del dProject["OfSc"]

    if "dProjRef" in dBase.keys():
        dProjRef = deepcopy(dBase["dProjRef"])
    else:
        dProjRef = DProjectNew()

    if "dVar" in dBase.keys():
        dVar = deepcopy(dBase["dVar"])
    else:
        dVar = DVar(dProject["chKeyRS"])

    for key in DVar(dProject["chKeyRS"]).keys():
        if key not in dVar.keys():
            dVar[key] = DVar(dProject["chKeyRS"])[key]

    base = {}
    base["dProject"] = dProject
    base["intervalData"] = intervalData
    base["dProjRef"] = dProjRef
    base["dVar"] = dVar
    with open(argv[1], "w") as fd:
        yaml.dump(
            base,
            fd,
        )


if __name__ == "__main__":
    main_wrapper(sys.argv)
