import os 
import dearpygui.dearpygui as dpg 

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.theme() as primarybtn_green_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (16, 194, 75), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 0, 0), category=dpg.mvThemeCat_Core)

with dpg.theme() as primarybtn_red_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (155, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 0, 0), category=dpg.mvThemeCat_Core)

elements = []

def calculate(symbol: str):
    global elements
    try:
        if symbol == '=':
            global result 
            result = eval("".join(str(i) for i in elements ))
            elements.clear()
            return dpg.set_value("input", result)
        
        elif symbol =='clear':
            elements.clear()
            dpg.set_value("input", 0)

        elif symbol == 'del':
            elements = elements[:-1]
            dpg.set_value("input", "".join(str(i) for i in elements))

        elif symbol.isdigit():
            elements.append(symbol)
            dpg.set_value("input", "".join(str(i) for i in elements))
            
        else:
            elements.append(symbol)
            dpg.set_value("input", "".join(str(i) for i in elements))
            
    except Exception as err:
        return dpg.set_value("input", err)

with dpg.window() as main_window:
    dpg.add_text("0", tag="input")
    dpg.add_spacer(height=10)
    with dpg.group(horizontal= True):
        dpg.add_button(label="7", width=100, height = 100, callback = calculate, tag = '7')
        dpg.add_button(label="8", width=100, height = 100, callback = calculate, tag = '8')
        dpg.add_button(label="9", width=100, height = 100, callback = calculate, tag = '9')
        dpg.add_button(label="%", width=100, height = 100, callback = calculate , tag = '%')
        dpg.add_button(label="root", width=100, height = 100, callback = calculate , tag = '**0.5')

    with dpg.group(horizontal= True):
        dpg.add_button(label="4", width=100, height = 100, callback = calculate, tag ='4')
        dpg.add_button(label="5", width=100, height = 100, callback = calculate, tag ='5')
        dpg.add_button(label="6", width=100, height = 100, callback = calculate, tag ='6')
        dpg.add_button(label="*", width=100, height = 100, callback = calculate, tag = '*')        
        dpg.add_button(label="÷", width=100, height = 100, callback = calculate, tag = '/')

    with dpg.group(horizontal= True):
        dpg.add_button(label="1", width=100, height = 100, callback = calculate, tag = '1')
        dpg.add_button(label="2", width=100, height = 100,callback = calculate, tag = '2')
        dpg.add_button(label="3", width=100, height = 100, callback = calculate, tag = '3')
        dpg.add_button(label="+", width=100, height = 100, callback = calculate, tag = '+')
        dpg.add_button(label="-", width=100, height = 100, callback = calculate, tag = '-')        

    with dpg.group(horizontal= True):
        dpg.add_button(label="0", width=100, height = 100, callback = calculate, tag = '0')
        dpg.add_button(label="00", width=100, height = 100, callback = calculate, tag = '00')
        dpg.add_button(label=".", width=100, height = 100, callback = calculate, tag = '.')
        dpg.add_button(label="(", width=100, height = 100, callback = calculate, tag = '(')
        dpg.add_button(label=")", width=100, height = 100, callback = calculate, tag = ')')

    with dpg.group(horizontal= True):
        equals  = dpg.add_button(label="=", width=317, height = 100, callback = calculate, tag = '=')
        dpg.bind_item_theme(equals, primarybtn_green_theme)
        delete = dpg.add_button(label="DEL", width=100, height = 100, callback = calculate, tag = 'del')
        dpg.bind_item_theme(delete, primarybtn_red_theme)
        clear = dpg.add_button(label="CLEAR", width=100, height = 100, callback = calculate, tag = 'clear')
        dpg.bind_item_theme(clear, primarybtn_red_theme)

dpg.set_viewport_title("GUI-Calculator")
dpg.set_primary_window(main_window, True)
dpg.set_viewport_resizable(False)
dpg.set_viewport_width(575)
dpg.set_viewport_height(605)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


