from bokeh.plotting import figure,output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')

# Generamos la primera figura    
    fig =  figure()
    
    total_vals = int(input('Cuantos valores quires graficar: '))
    x_vals =  list(range(total_vals))

#Generaomos lista de y

    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor y para la {x} '))
        y_vals.append(val)
    
    fig.line(x_vals, y_vals, line_width = 2)

#Le decimos a Bokeh que nos muestre el la figura
    show(fig)
