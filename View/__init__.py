CONSOLE = 1
IOS = 2

mode = 1

if (mode == CONSOLE):
    from View.console import show_translate_variant
elif (mode == IOS):
    from View.ios import show_translate_variant