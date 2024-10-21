#!/usr/bin/python3 
def common_elements(a, b):
    set_common = set()
    for item in a:
        if item in b:
            set_common.add(item)
    return set_common



if __name__=="__main__":
    set_a = { "API", "requests", "Selenium", "Python", "Behave"}
    set_b = { "Selenium", "Java", "Cucumber", "Maven", "API"}
    same_element = common_elements(set_a, set_b)
    [print(x) for x in sorted(list(same_element))]
