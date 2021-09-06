from tkinter import *

def main():
    root = Tk()
    root.title('Matrix Multiplier')

    #The input boxes for the right and left matrix sizes
    left_matrix_size = Entry(root, width=30)
    left_matrix_size.grid(row=0, column=0)
    left_matrix_size.insert(0, 'Enter left matrix size here (e.g., 2x3)')

    right_matrix_size = Entry(root, width=30)
    right_matrix_size.grid(row=1, column=0)
    right_matrix_size.insert(0, 'Enter right matrix size here (e.g., 3x2)')

    def size_submit():
        #Checking of the inputs are valid
        for i in range(1, 10):
            for j in range(1, 10):
                for k in range(1, 10):
                    if left_matrix_size.get().strip().lower() == f'{str(i)}x{str(j)}' and right_matrix_size.get().strip().lower() == f'{str(j)}x{str(k)}':
                        #Creating new window and disabling submit button for matrix sizes
                        new_window = Tk()
                        new_window.title('Left Matrix')
                        size_button['state'] = 'disabled'
                        left_matrix_entries(new_window)
                        
        if size_button['state'] != 'disabled':
            error_label = Label(root, text='Please enter proper matrix sizes!')
            error_label.grid(row=4, column=0)

    #The submit button for the matrix sizes
    size_button = Button(root, text='Submit', command=size_submit)
    size_button.grid(row=3, column=0)

    #The function to get the left matrix from the user
    def left_matrix_entries(new_window):
        left_matrix_input = []
        left_matrix_dimensions = left_matrix_size.get().strip().lower().split('x')

        #Creating the input boxes for the matrix
        for i in range(0, int(left_matrix_dimensions[0])): 
            left_matrix_input.insert(i, [])
            for j in range(0, int(left_matrix_dimensions[1])): 
                left_matrix_input[i].insert(j, Entry(new_window))
                left_matrix_input[i][j].grid(row=i, column=j)
        
        def left_matrix_submit():
            count = 0
            
            for i in range(0, int(left_matrix_dimensions[0])): 
                for j in range(0, int(left_matrix_dimensions[1])): 
                    if not left_matrix_input[i][j].get().isnumeric():
                        error_label = Label(new_window, text='Please enter a number in each matrix entry!')
                        error_label.grid(row=int(left_matrix_dimensions[0]) + 1, column=0)
                    else:
                        count += 1

            if count == (int(left_matrix_dimensions[0]) * int(left_matrix_dimensions[1])):
                #Creating new window and disabling the submit button for the left matrix
                newer_window = Tk()
                newer_window.title('Right Matrix')
                left_matrix_button['state'] = 'disabled'
                right_matrix_entries(newer_window, left_matrix_input)

        #Left matrix submit button
        left_matrix_button = Button(new_window, text='Submit', command=left_matrix_submit)
        left_matrix_button.grid(row=int(left_matrix_dimensions[0]), column=round((int(left_matrix_dimensions[1])/2)))

    #The function to get the right input from the user
    def right_matrix_entries(newer_window, left_matrix_input):
        right_matrix_input = []
        right_matrix_dimensions = right_matrix_size.get().strip().lower().split('x')

        #Creating the input boxes for the matrix
        for i in range(0, int(right_matrix_dimensions[0])): 
            right_matrix_input.insert(i, [])
            for j in range(0, int(right_matrix_dimensions[1])): 
                right_matrix_input[i].insert(j, Entry(newer_window))
                right_matrix_input[i][j].grid(row=i, column=j)
     
        def right_matrix_submit():
            count = 0

            for i in range(0, int(right_matrix_dimensions[0])): 
                for j in range(0, int(right_matrix_dimensions[1])): 
                    if not right_matrix_input[i][j].get().isnumeric():
                        error_label = Label(newer_window, text='Please enter an number in each matrix entry!')
                        error_label.grid(row=int(right_matrix_dimensions[0]) + 1, column=0)
                    else:
                        count += 1

            if count == (int(right_matrix_dimensions[0]) * int(right_matrix_dimensions[1])):
                #Creating new window and disabling the submit button for the right matrix
                newest_window = Tk()
                newest_window.title('Calculation')
                right_matrix_button['state'] = 'disabled'
                calculation(newest_window, left_matrix_input, right_matrix_input)
            else:
                error_label = Label(newer_window, text='Please enter an number in each matrix entry!')
                error_label.grid(row=int(right_matrix_dimensions[0]) + 1, column=0)
        
        #Right matrix submit button
        right_matrix_button = Button(newer_window, text='Submit', command=right_matrix_submit)
        right_matrix_button.grid(row=int(right_matrix_dimensions[0]), column=round((int(right_matrix_dimensions[1])/2)))

    def calculation(newest_window, left_matrix_input, right_matrix_input):

        matrix = []
        
        #Creating a matrix of the correct size to contain the final matrix entries
        for a in range(len(left_matrix_input)):
            matrix.insert(a, [])

        #Calculation of the individual entries in the final matrix and insertion into the matrix
        for i in range(len(right_matrix_input[0])):
            for j in range(len(left_matrix_input)):
                entry = 0
                for k in range(len(right_matrix_input)):
                    entry += float(left_matrix_input[j][k].get()) * float(right_matrix_input[k][i].get())
                matrix[j].insert(i, Label(newest_window, text=str(entry)))
                matrix[j][i].grid(row=j, column=i)

        def close():
            exit()

        #Button to close the entire program
        close_button = Button(newest_window, text='Close', command=close)
        close_button.grid(row=j + 1, column=round(int(i/2)))

    root.mainloop()

if __name__=='__main__':
    main() 
    