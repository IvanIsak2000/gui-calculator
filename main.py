import os 
import dearpygui.dearpygui as dpg 

dpg.create_context()
dpg.setup_dearpygui()
dpg.create_viewport(title='Calculator', width=450, height=500)

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

            e = elements
            global result 
            result = eval("".join(str(i) for i in e ))
            elements.clear()
            os.system('cls')
            return print(result)
        
        elif symbol =='clear':

            elements.clear()
            os.system('cls')

        elif symbol == 'del':
            elements = elements[:-1]
            os.system('cls')
            print("".join(str(i) for i in elements))

        elif symbol.isdigit():
            elements.append(symbol)
            os.system('cls')
            print("".join(str(i) for i in elements))
            
        else:
            elements.append(symbol)
            os.system('cls')
            print("".join(str(i) for i in elements))
            
    except Exception as err:
        return print(err)

        
with dpg.window(label="",tag = 'Primary Window'):

    with dpg.group(horizontal= True):
        dpg.add_button(label="1", width=100, height = 80, callback = calculate, tag = '1')
        dpg.add_button(label="2", width=100, height = 80,callback = calculate, tag = '2')
        dpg.add_button(label="3", width=100, height = 80, callback = calculate, tag = '3')
        dpg.add_button(label="+", width=100, height = 80, callback = calculate , tag = '+')

    with dpg.group(horizontal= True):
        dpg.add_button(label="4", width=100, height = 80, callback = calculate, tag ='4')
        dpg.add_button(label="5", width=100, height = 80, callback = calculate, tag ='5')
        dpg.add_button(label="6", width=100, height = 80, callback = calculate, tag ='6')
        dpg.add_button(label="-", width=100, height = 80, callback = calculate, tag = '-')

    with dpg.group(horizontal= True):
        dpg.add_button(label="7", width=100, height = 80, callback = calculate, tag = '7')
        dpg.add_button(label="8", width=100, height = 80, callback = calculate, tag = '8')
        dpg.add_button(label="9", width=100, height = 80, callback = calculate, tag = '9')
        dpg.add_button(label="/", width=100, height = 80, callback = calculate, tag = '/')

    with dpg.group(horizontal= True):
        delete = dpg.add_button(label="DEL", width=100, height = 80, callback = calculate, tag = 'del')
        dpg.bind_item_theme(delete, primarybtn_red_theme)
        dpg.add_button(label="0", width=100, height = 80, callback = calculate, tag = '0')
        clear = dpg.add_button(label="CLEAR", width=100, height = 80, callback = calculate, tag = 'clear')
        dpg.bind_item_theme(clear, primarybtn_red_theme)
        dpg.add_button(label="*", width=100, height = 80, callback = calculate, tag = '*')

    with dpg.group(horizontal= True):
        equals  = dpg.add_button(label="=", width=316, height = 80, callback = calculate, tag = '=')
        dpg.bind_item_theme(equals, primarybtn_green_theme)
        dpg.add_button(label="%", width=100, height = 80, callback = calculate, tag = '%')

# dpg.setup_dearpygui()
dpg.set_primary_window("Primary Window", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

