#!/usr/bin/env python3
def not_common_elements(a, b):
    uniqu_el =set()
    for el1 in a:
       if el1 not in b:
           uniqu_el.add(el1)
    for el2 in b:
        if el2 not in a:
            uniqu_el.add(el2)
    return uniqu_el


if __name__=="__main__":
    set_a = {"API", "requests", "Selenium", "Python", "Behave"}
    set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
    elements = not_common_elements(set_a, set_b)
    [print(x) for x in sorted(list(elements))]

