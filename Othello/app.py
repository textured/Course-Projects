import tkinter
import othello
import classes


class ErrorMessage:
    def __init__(self):
        """ Produces a toplevel error message if board settings are not valid """
        self.toplevel = tkinter.Toplevel()
        self.toplevel.geometry('300x150')

        self.label1 = tkinter.Label(self.toplevel, text='Invalid settings, please try again.', font=('Menlo,20'))
        self.label1.grid(row=0, column=0, sticky=tkinter.S + tkinter.E + tkinter.W)

        self.button = tkinter.Button(self.toplevel, text='Ok', width=10, command=self.toplevel.destroy)
        self.button.grid(row=1, column=0, sticky=tkinter.N)

        self.toplevel.rowconfigure(0, weight=1)
        self.toplevel.rowconfigure(1, weight=1)
        self.toplevel.columnconfigure(0, weight=1)

    def show(self):
        self.toplevel.grab_set()
        self.toplevel.wait_window()


class OthelloApp:
    def __init__(self):
        """ Initializes the root window/main menu of the gui """
        self.root_window = tkinter.Tk()
        self.BG_COLOR = '#FFFFFF'
        self.root_window.title('A Game of Othello')
        self.root_window.configure(bg=self.BG_COLOR)

        self.title = tkinter.Label(self.root_window, text='A Game of Othello', font=('Menlo', 36), pady='60',
                                   padx=150, background=self.BG_COLOR)

        self.title.grid(row=0, column=0)

        self.start_button = tkinter.Button(self.root_window, text='Start game', command=self.options_window,
                                   font='Menlo', width=20, highlightbackground=self.BG_COLOR)

        self.start_button.grid(row=1, column=0, sticky=tkinter.N + tkinter.S, pady=(0, 40))

        self.quit_button = tkinter.Button(self.root_window, text='Quit', command=self._exit_game,
                                  font='Menlo', width=20, highlightbackground=self.BG_COLOR)

        self.quit_button.grid(row=2, column=0, sticky=tkinter.N + tkinter.S, pady=(0, 120))

        self.root_window.columnconfigure(0, weight=1)

    def clear_window(self) -> None:
        """ Clears window of all child widgets """
        for child in self.root_window.winfo_children():
            child.destroy()

    def options_window(self) -> None:
        """ Displays the options menu """
        self.clear_window()
        self.checkbox_var = tkinter.IntVar()
        self.checkbox_var2 = tkinter.IntVar()
        self.checkbox_var3 = tkinter.IntVar()

        self.title = tkinter.Label(text='Board Settings', font=('Menlo', 36), background=self.BG_COLOR)
        self.title.grid(row=0, columnspan=2, pady=(80, 25), padx=200)

        self.full_label = tkinter.Label(text='FULL', font =('Menlo', 24), background=self.BG_COLOR)
        self.full_label.grid(row=1, columnspan=3, sticky=tkinter.N + tkinter.W + tkinter.E + tkinter.S, pady=(0,15))

        self.label_1 = tkinter.Label(text='Enter number of rows (even):', anchor='w', background=self.BG_COLOR)
        self.label_1.grid(row=2,column=0,sticky=tkinter.E)

        self.label_2 = tkinter.Label(text='Enter number of columns (even):', background=self.BG_COLOR)
        self.label_2.grid(row=3, column=0, sticky=tkinter.E, pady=(5, 0))

        self.label_3 = tkinter.Label(text='Color to move first:', background=self.BG_COLOR)
        self.label_3.grid(row=4, column=0, sticky=tkinter.E, pady=(5, 0))

        self.label_4 = tkinter.Label(text='Arrangement of color:', background=self.BG_COLOR)
        self.label_4.grid(row=5,  column=0, sticky=tkinter.E, pady=(5,0))

        self.label_5 = tkinter.Label(text='How the game is won:', background=self.BG_COLOR)
        self.label_5.grid(row=6, column=0, sticky=tkinter.E, pady=(5, 0))

        # Entries
        self.entry_1 = tkinter.Entry( self.root_window, width=30, highlightbackground=self.BG_COLOR)
        self.entry_1.grid(row=2,column=1,sticky=tkinter.W)

        self.entry_2 = tkinter.Entry( self.root_window, width=30, highlightbackground=self.BG_COLOR)
        self.entry_2.grid(row=3, column=1,sticky=tkinter.W, pady=(5,0))

        # button frames
        self.button_frame = tkinter.Frame( self.root_window, bg=self.BG_COLOR)
        self.button_frame.grid(row=4, column=1, sticky=tkinter.W)

        self.button_frame2 = tkinter.Frame( self.root_window, bg=self.BG_COLOR)
        self.button_frame2.grid(row=5, column=1, sticky=tkinter.W)

        self.button_frame3 = tkinter.Frame( self.root_window, bg=self.BG_COLOR)
        self.button_frame3.grid(row=6, column=1, sticky=tkinter.W)

        # Check boxes
        self.check_box1 = tkinter.Radiobutton(self.button_frame, text='Black',
                                              value=1,background=self.BG_COLOR, variable=self.checkbox_var)
        self.check_box1.grid(row=0, column=0, sticky=tkinter.W, pady=(5,0))

        self.check_box2 = tkinter.Radiobutton(self.button_frame, text='White',
                                              value=2, background=self.BG_COLOR, variable=self.checkbox_var)
        self.check_box2.grid(row=0, column=1, sticky=tkinter.W, pady=(5,0))


        self.check_box3 = tkinter.Radiobutton(self.button_frame2, text='Black',
                                              value=1, background=self.BG_COLOR, variable=self.checkbox_var2)
        self.check_box3.grid(row=0, column=0, sticky=tkinter.W, pady=(5, 0))

        self.check_box4 = tkinter.Radiobutton(self.button_frame2, text='White',
                                              value=2, background=self.BG_COLOR, variable=self.checkbox_var2)
        self.check_box4.grid(row=0, column=1, sticky=tkinter.W, pady=(5, 0))


        self.check_box5 = tkinter.Radiobutton(self.button_frame3, text='Most discs wins',
                                              value=1, background=self.BG_COLOR, variable=self.checkbox_var3)
        self.check_box5.grid(row=0, column=0, sticky=tkinter.W, pady=(5, 0))

        self.check_box6 = tkinter.Radiobutton(self.button_frame3, text='Least discs wins',
                                              value=2, background=self.BG_COLOR, variable=self.checkbox_var3)
        self.check_box6.grid(row=0, column=1, sticky=tkinter.W, pady=(5, 0))

        self.back_button = tkinter.Button( self.root_window, text='Create board',
                                           command=self.create_board, highlightbackground=self.BG_COLOR)
        self.back_button.grid(row=7,columnspan=2, pady=(25,50))

        self.root_window.columnconfigure(0, weight=1)
        self.root_window.columnconfigure(1, weight=1)

    def create_board(self) -> None:
        """ Draws the canvas for the board and initializes the game """
        self.board_rows = int(self.entry_1.get())
        self.board_columns = int(self.entry_2.get())
        self.first_color = int(self.checkbox_var.get())
        self.arrangement = int(self.checkbox_var2.get())
        self.game_rule = int(self.checkbox_var3.get())

        self.turn_var = tkinter.StringVar()
        self.score_var = tkinter.StringVar()

        if self.board_rows % 2 != 0 or self.board_columns % 2 != 0:
            self._error_message()
            self.options_window()
        elif self.first_color != 1 and self.first_color != 2:
            self._error_message()
            self.options_window()
        elif self.arrangement != 1 and self.arrangement != 2:
            self._error_message()
            self.options_window()
        elif self.game_rule != 1 and self.game_rule != 2:
            self._error_message()
            self.options_window()
        else:
            self.clear_window()
            if self.first_color == 1:
                self.first_color = 'Black'
            elif self.first_color == 2:
                self.first_color = 'White'

            if self.arrangement == 1:
                self.arrangement = 'Black'
            elif self.arrangement == 2:
                self.arrangement = 'White'

            if self.game_rule == 1:
                self.game_rule = '>'
            elif self.game_rule == 2:
                self.game_rule = '<'

            self.game = classes.Game()
            self.game.row(self.board_rows)
            self.game.col(self.board_columns)
            self.turn = classes.Turn(self.first_color)
            self.board = othello.create_board(self.game, self.arrangement)

            self.turn_var.set('Player Turn: {}'.format(self.turn.get_turn()))
            self.score_var.set('Black: {}  White: {}'.format(self.game.get_black_count(self.board),
                                                             self.game.get_white_count(self.board)))

            self.root_window.configure(background='white')

            self.score_label = tkinter.Label(self.root_window, font=('Menlo', 24), textvariable=self.score_var)
            self.score_label.grid(row=0, columnspan=2, sticky=tkinter.W+tkinter.E)

            self.turn_label = tkinter.Label(self.root_window,
                                             font=('Menlo', 24), textvariable=self.turn_var)
            self.turn_label.grid(row=1,columnspan=2, sticky=tkinter.W+tkinter.E)

            self.canvas = tkinter.Canvas(self.root_window, background='#66BB6A',
                                         width=600, height=600, highlightcolor='black')
            self.canvas.grid(row=2, columnspan=4, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W, padx= 10, pady=10)

            self.canvas_width = self.canvas.winfo_width()
            self.canvas_height = self.canvas.winfo_height()

            self._draw_lines()
            self._draw_circles()

            self.canvas.bind('<Configure>', self._on_canvas_resized)
            self.canvas.bind('<Button-1>', self._on_canvas_clicked)

            self.root_window.columnconfigure(0, weight=1)
            self.root_window.rowconfigure(2, weight=1)

            self.canvas.columnconfigure(0, weight=1)
            self.canvas.rowconfigure(2, weight=1)

    def _draw_lines(self) -> None:
        """ Draws the grid for the board based on row and column """
        self.row_distance = (self.canvas_height/int(self.board_rows))
        point_y = self.row_distance-1
        for line in range(self.board_rows):
            self.canvas.create_line(0, point_y, self.canvas_width, point_y)
            point_y += self.row_distance

        self.col_distance = (self.canvas_width/int(self.board_columns))
        point_x = self.col_distance-1
        for line in range(self.board_columns):
            self.canvas.create_line(point_x, 0, point_x, self.canvas_height)
            point_x += self.col_distance

    def _draw_circles(self) -> None:
        """ Draws the discs based on current state of the game """
        for row in range(self.game.row):
            for col in range(self.game.col):
                if self.board[row][col] == 'Black':
                    self._draw_black_circle(row, col)
                elif self.board[row][col] == 'White':
                    self._draw_white_circle(row, col)

    def _draw_black_circle(self, row, col) -> None:
        """ Draws black discs based on location """
        col += 1
        row += 1
        x_bot_right = (col/self.board_columns) * self.canvas_width
        y_bot_right = (row/self.board_rows) * self.canvas_height

        x_top_left = x_bot_right-self.col_distance
        y_top_left = y_bot_right-self.row_distance

        self.canvas.create_oval(x_top_left+15, y_top_left+15, x_bot_right-15, y_bot_right-15, fill='black')

    def _draw_white_circle(self, row, col) -> None:
        """ Draws white discs based on location """
        col += 1
        row += 1
        x_bot_right = (col/self.board_columns) * self.canvas_width
        y_bot_right = (row/self.board_rows) * self.canvas_height

        x_top_left = x_bot_right-self.col_distance
        y_top_left = y_bot_right-self.row_distance

        self.canvas.create_oval(x_top_left+15, y_top_left+15, x_bot_right-15, y_bot_right-15, fill='white')

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        """ Redraws board and entities based on canvas resized """
        self.canvas.delete(tkinter.ALL)

        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

        self._draw_lines()
        self._draw_circles()

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        """ Makes moves based on mouse click and progresses game state """
        self.x, self.y = event.x, event.y
        column_distance = self.col_distance
        row_distance = self.row_distance
        col = 1
        row = 1

        while True:
            if self.x <= column_distance:
                break
            else:
                column_distance += self.col_distance
                col += 1
        while True:
            if self.y <= row_distance:
                break
            else:
                row_distance += self.row_distance
                row += 1

        while self.game.state == 'ACTIVE':
            try:
                if othello.check_move(self.game, self.turn, self.board, row, col):
                    self.turn.set_move(self.turn.get_turn())
                    othello.make_move(self.game, self.turn, self.board, row, col)

                    self.canvas.delete(tkinter.ALL)
                    self._draw_lines()
                    self._draw_circles()

                    self.score_var.set('Black: {}  White: {}'.format(self.game.get_black_count(self.board),
                                                                     self.game.get_white_count(self.board)))

                    self.turn.increment()

                    if othello.check_for_valid_turns(self.game, self.turn, self.board) is False:
                        self.turn.set_no_move(self.turn.get_turn())
                        self.turn.increment()
                        if othello.check_for_valid_turns(self.game, self.turn, self.board) is False:
                            self.turn.set_no_move(self.turn.get_turn())

                    if self.turn.black_no_move is True and self.turn.white_no_move is True:
                        self._game_over()
                        break

                    if self.game.get_white_count(self.board) + \
                            self.game.get_black_count(self.board) == self.game.row * self.game.col:
                            self._game_over()
                            break

                    self.turn_var.set('Player Turn: {}'.format(self.turn.get_turn()))

                    break

            except classes.InvalidMoveError:
                return

    def _game_over(self) -> None:
        """ Sets game over screen """
        self.canvas.delete(tkinter.ALL)
        self.turn_var.set(self.game.game_rule(self.board, self.game_rule))
        self._draw_lines()
        self._draw_circles()

    def _error_message(self) -> None:
        """ Creates error message toplevel class and calls it """
        self.error = ErrorMessage()
        self.error.show()

    def _exit_game(self) -> None:
        """ Destroys the root window and exits app """
        self.root_window.destroy()

    def run(self) -> None:
        """ Run the app """
        self.root_window.mainloop()

if __name__ == '__main__':
    application = OthelloApp()
    application.run()
