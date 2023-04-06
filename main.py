import dearpygui.dearpygui as dpg 

dpg.create_context()
dpg.create_viewport(title='Calculator', width=450, height=500)

with dpg.theme() as primarybtn_blue_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (16, 194, 75), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 0, 0), category=dpg.mvThemeCat_Core)

def calculate(number):
    print(number)
    if number.isdigit():
        print(type(int(number)))
        
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
        dpg.add_button(label="DEL", width=100, height = 80, callback = calculate)
        dpg.add_button(label="0", width=100, height = 80, callback = calculate, tag = '0')
        dpg.add_button(label="CLEAR", width=100, height = 80, callback = calculate)
        dpg.add_button(label="*", width=100, height = 80, callback = calculate, tag = '*')

    with dpg.group(horizontal= True):
        equals  = dpg.add_button(label="=", width=316, height = 80, callback = calculate)
        dpg.bind_item_theme(equals, primarybtn_blue_theme)
        dpg.add_button(label="%", width=100, height = 80, callback = calculate, tag = '%')

dpg.setup_dearpygui()
dpg.set_primary_window("Primary Window", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
