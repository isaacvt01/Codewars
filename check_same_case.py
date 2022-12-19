def same_case(a, b):

    if a == b:
        return 1
    elif a:
        return -1

    elif a(str) != b(str):
        return 0

print(same_case("has","hola"))